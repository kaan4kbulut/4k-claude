#!/usr/bin/env python3
"""kontrol.py — Yeni Sistem bütünlük denetimi (yalnız okur, hiçbir şeyi düzeltmez).

Kullanım:
  python3 00-sistem/scripts/kontrol.py            tam rapor (≤ 40 satır yapılı özet + hata listesi)
  python3 00-sistem/scripts/kontrol.py --kisa     yalnız özet ve ilk 15 hata
  python3 00-sistem/scripts/kontrol.py --json     JSON çıktı
  python3 00-sistem/scripts/kontrol.py --strict   uyarıları da hata say
Çıkış kodu: 0 temiz, 1 hata var (Stop hook'u bunu kullanır).

13 denetim (SEMA.md §11):
 1 frontmatter: var, ayrıştırılır, zorunlu alanlar türe göre tam, enum geçerli, tarih ISO
 2 id tekil
 3 kat ↔ klasör ve tür ↔ klasör uyumu
 4 HARITA.md'de tek satır (şablon, arşiv, ham hariç)
 5 kırık bağ (dayandigi / besledigi / ust / gövde wikilink hedefi yok)
 6 tek yönlü bağ (A.dayandigi ∋ B ama B.besledigi ∌ A, ve tersi)
 7 ust var, MOC türünde ve MOC bu sayfayı listeliyor
 8 GUNLUK.md'de kayıt var
 9 talimat TALIMATLAR.md'de var; durum ≠ taslak ise talimat kapali/bekliyor
10 ADR simetrisi (yerine_gecti ⇔ yerine_gecen)
11 bayat (uyarı): son_gozden_gecirme > 60 gün, alindi > 90 gün (TAZELIK), gecerli_bitis geçmiş ama durum aktif
12 boyut: CLAUDE.md ≤ 200 satır, SKILL.md ≤ 500, HARITA ≤ 200 sayfa satırı
13 kanıtsız tamam: tur gorev, kanban tamam, kanit boş
Ek: SEMA.md ile sayfa.schema.json tür listesi uyumu.
"""
import json
import os
import re
import sys
from datetime import date, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yscommon as yc  # noqa: E402

TUR_KLASOR = {
    "gozlem": ["40-ic-ses/gozlemler"], "fikir": ["40-ic-ses/fikirler"], "yansima": ["40-ic-ses/yansimalar"],
    "kavram": ["40-ic-ses/kavramlar"], "arastirma-notu": ["40-ic-ses/arastirma-notlari"],
    "karar": ["30-devlet/kararlar"], "kural": ["30-devlet/normlar/kurallar"], "yonerge": ["30-devlet/normlar/yonergeler"],
    "kapi": ["30-devlet/kapilar"], "bulgu": ["30-devlet/denetim/bulgular"], "eylem-plani": ["30-devlet/denetim/eylem-planlari"],
    "gorev": ["20-sirket/gorevler"], "rol": ["20-sirket/roller"], "sop": ["20-sirket/sop"], "alan-paketi": ["20-sirket/alan-paketleri"],
    "cikti": ["10-insan/ciktilar"], "kaynak": ["10-insan/kaynaklar", "00-sistem/arastirma"],
    "referans": ["00-sistem", "10-insan/araclar", "20-sirket", "30-devlet/normlar", "40-ic-ses"],
    "anayasa": ["30-devlet/normlar"], "moc": ["40-ic-ses", "30-devlet", "20-sirket", "10-insan"], "ham": ["01-gelen"],
}


def tarih(s):
    try:
        return datetime.strptime(str(s)[:10], "%Y-%m-%d").date()
    except Exception:  # noqa: BLE001
        return None


# ---------- mini şema doğrulayıcı (jsonschema yoksa) ----------
def _tip_uyar(val, tip):
    if isinstance(tip, list):
        return any(_tip_uyar(val, t) for t in tip)
    return {"string": isinstance(val, str), "integer": isinstance(val, int) and not isinstance(val, bool),
            "number": isinstance(val, (int, float)) and not isinstance(val, bool), "boolean": isinstance(val, bool),
            "array": isinstance(val, list), "object": isinstance(val, dict)}.get(tip, True)


def _kosul_uyar(fm, kosul):
    props = kosul.get("properties", {})
    for k, kural in props.items():
        v = fm.get(k)
        if "const" in kural and v != kural["const"]:
            return False
        if "enum" in kural and v not in kural["enum"]:
            return False
        if "not" in kural:
            n = kural["not"]
            if "enum" in n and v in n["enum"]:
                return False
            if "const" in n and v == n["const"]:
                return False
    return True


def sema_dogrula(fm, sema):
    hatalar = []
    for z in sema.get("required", []):
        if z not in fm or fm[z] is None:
            hatalar.append(f"zorunlu alan eksik: {z}")
    for k, kural in sema.get("properties", {}).items():
        if k not in fm or fm[k] is None:
            continue
        v = fm[k]
        if "type" in kural and not _tip_uyar(v, kural["type"]):
            hatalar.append(f"tip hatası: {k}={v!r} ({kural['type']})")
            continue
        if "enum" in kural and v not in kural["enum"]:
            hatalar.append(f"geçersiz değer: {k}={v!r} (izinli: {', '.join(map(str, kural['enum']))})")
        if "pattern" in kural and isinstance(v, str) and not re.search(kural["pattern"], v):
            hatalar.append(f"biçim hatası: {k}={v!r}")
        if "minLength" in kural and isinstance(v, str) and len(v) < kural["minLength"]:
            hatalar.append(f"çok kısa: {k}")
        if "minimum" in kural and isinstance(v, (int, float)) and v < kural["minimum"]:
            hatalar.append(f"küçük: {k}={v}")
        if "maximum" in kural and isinstance(v, (int, float)) and v > kural["maximum"]:
            hatalar.append(f"büyük: {k}={v}")
        if kural.get("type") == "array" and "items" in kural and isinstance(v, list):
            it = kural["items"]
            for i, eleman in enumerate(v):
                if it.get("type") == "object" and isinstance(eleman, dict):
                    for z in it.get("required", []):
                        if z not in eleman:
                            hatalar.append(f"{k}[{i}] eksik alan: {z}")
                elif it.get("type") == "string" and not isinstance(eleman, str):
                    hatalar.append(f"{k}[{i}] metin değil")
    for kosul in sema.get("allOf", []):
        if "if" in kosul and _kosul_uyar(fm, kosul["if"]):
            for z in kosul.get("then", {}).get("required", []):
                if z not in fm or fm[z] is None:
                    hatalar.append(f"türe göre zorunlu alan eksik: {z}")
    return hatalar


def main():
    arg = sys.argv[1:]
    kisa, as_json, strict = "--kisa" in arg, "--json" in arg, "--strict" in arg
    kok = yc.kok_bul()
    bugun = date.today()
    hatalar, uyarilar = [], []

    def hata(yol, mesaj):
        hatalar.append((yol, mesaj))

    def uyari(yol, mesaj):
        uyarilar.append((yol, mesaj))

    # şema
    sema_yol = os.path.join(kok, "00-sistem", "sema", "sayfa.schema.json")
    try:
        with open(sema_yol, encoding="utf-8") as f:
            sema = json.load(f)
    except Exception as e:  # noqa: BLE001
        print(f"HATA: şema okunamadı: {e}")
        sys.exit(1)

    # SEMA.md ↔ schema tür listesi
    sema_md = os.path.join(kok, "00-sistem", "SEMA.md")
    try:
        with open(sema_md, encoding="utf-8") as f:
            sema_metin = f.read()
        md_turler = set(re.findall(r"^\| `([a-z-]+)` \| [0-9]", sema_metin, re.M))
        js_turler = set(sema["properties"]["tur"]["enum"])
        for t in js_turler - md_turler:
            uyari("00-sistem/SEMA.md", f"şema JSON'daki tür SEMA.md §2'de yok: {t}")
        for t in md_turler - js_turler:
            hata("00-sistem/SEMA.md", f"SEMA.md §2'deki tür şema JSON'da yok: {t}")
    except Exception:  # noqa: BLE001
        uyari("00-sistem/SEMA.md", "SEMA.md okunamadı; tür uyumu denetlenemedi")

    sayfalar = yc.sayfalari_tara(kok)
    fm_map = {}  # goreli_yol -> fm
    govde_map = {}
    for yol, fm, govde, err in sayfalar:
        if err:
            hata(yol, err)
            continue
        if fm is None:
            # frontmatter'sız .md sayfası taranan klasörde
            hata(yol, "frontmatter yok (her sayfa şablonla doğar)")
            continue
        fm_map[yol] = fm
        govde_map[yol] = govde

    # 1 şema
    for yol, fm in fm_map.items():
        for h in sema_dogrula(fm, sema):
            hata(yol, h)
        for alan in ("olusturma", "guncelleme", "alindi", "son_gozden_gecirme", "sunset", "gecerli_bitis"):
            if fm.get(alan) and not tarih(fm[alan]):
                hata(yol, f"tarih ISO değil: {alan}={fm[alan]}")

    # 2 id tekil
    ids = {}
    for yol, fm in fm_map.items():
        i = fm.get("id")
        if i in ids:
            hata(yol, f"id tekrarı: {i} (ayrıca {ids[i]})")
        ids[i] = yol

    # 3 kat ↔ klasör, tür ↔ klasör
    for yol, fm in fm_map.items():
        kk = yc.kat_from_yol(yol)
        if fm.get("kat") is not None and kk is not None and fm["kat"] != kk:
            hata(yol, f"kat uyuşmazlığı: frontmatter {fm['kat']}, klasör {kk}")
        t = fm.get("tur")
        if t in TUR_KLASOR:
            klasor = os.path.dirname(yol)
            if not any(klasor == k or klasor.startswith(k + "/") or k.startswith(klasor) and klasor in k for k in TUR_KLASOR[t]):
                if not any(klasor.startswith(k) for k in TUR_KLASOR[t]):
                    hata(yol, f"tür {t} için yanlış klasör: {klasor} (beklenen: {', '.join(TUR_KLASOR[t])})")

    # 4 HARITA
    harita_yol = os.path.join(kok, "00-sistem", "HARITA.md")
    harita_satirlar = []
    try:
        with open(harita_yol, encoding="utf-8") as f:
            harita_satirlar = [s for s in f.read().splitlines() if s.startswith("- [[")]
    except FileNotFoundError:
        hata("00-sistem/HARITA.md", "yok")
    harita_hedefler = {}
    for s in harita_satirlar:
        m = re.match(r"^- \[\[([^\]|#]+)", s)
        if m:
            h = yc.normalize_yol(m.group(1))
            harita_hedefler[h] = harita_hedefler.get(h, 0) + 1
    for yol, fm in fm_map.items():
        if fm.get("tur") == "ham" or fm.get("durum") == "arsiv":
            continue
        n = harita_hedefler.get(yc.normalize_yol(yol), 0)
        if n == 0:
            hata(yol, "haritada yok (HARITA.md)")
        elif n > 1:
            hata(yol, f"haritada {n} kez")
    for h in harita_hedefler:
        if not yc.hedef_var(kok, h):
            hata("00-sistem/HARITA.md", f"haritada olmayan dosya: {h}")
    if len(harita_satirlar) > 200:
        hata("00-sistem/HARITA.md", f"{len(harita_satirlar)} satır > 200; MOC'lara böl (harita.py)")

    # 5 kırık bağ + 6 karşılıklılık + 7 ust
    def liste(v):
        if v is None:
            return []
        return v if isinstance(v, list) else [v]

    for yol, fm in fm_map.items():
        for alan in ("dayandigi", "besledigi"):
            for h in liste(fm.get(alan)):
                if not isinstance(h, str) or not h:
                    hata(yol, f"{alan}: geçersiz giriş {h!r}")
                    continue
                if not yc.hedef_var(kok, h):
                    hata(yol, f"kırık bağ ({alan}): {h}")
        ust = fm.get("ust")
        if ust:
            if not yc.hedef_var(kok, ust):
                hata(yol, f"ust hedefi yok: {ust}")
            else:
                ust_n = yc.normalize_yol(ust) + ".md"
                ufm = fm_map.get(ust_n)
                if ufm is None or ufm.get("tur") != "moc":
                    hata(yol, f"ust MOC değil: {ust}")
                else:
                    g = govde_map.get(ust_n, "")
                    if f"[[{yc.normalize_yol(yol)}" not in g:
                        hata(ust_n, f"MOC bu sayfayı listelemiyor: {yol}")
        # gövde wikilinkleri
        for m in re.finditer(r"\[\[([^\]|#]+)", govde_map.get(yol, "")):
            h = m.group(1).strip()
            if h.startswith("http") or "..." in h or h.endswith("/") or "/" not in h:
                continue  # dış link, yer tutucu ("[[hedef]]", "[[yol]]") ya da kök dışı örnek
            if not yc.hedef_var(kok, h):
                hata(yol, f"kırık wikilink: [[{h}]]")

    for yol, fm in fm_map.items():
        for h in liste(fm.get("dayandigi")):
            if not isinstance(h, str):
                continue
            hn = yc.normalize_yol(h) + ".md"
            if hn in fm_map:
                ters = [yc.normalize_yol(x) for x in liste(fm_map[hn].get("besledigi")) if isinstance(x, str)]
                if yc.normalize_yol(yol) not in ters:
                    hata(yol, f"tek yönlü bağ: {yol} → {hn} (hedefin besledigi alanında yok)")
        for h in liste(fm.get("besledigi")):
            if not isinstance(h, str):
                continue
            hn = yc.normalize_yol(h) + ".md"
            if hn in fm_map:
                ters = [yc.normalize_yol(x) for x in liste(fm_map[hn].get("dayandigi")) if isinstance(x, str)]
                if yc.normalize_yol(yol) not in ters:
                    hata(yol, f"tek yönlü bağ: {yol} ← {hn} (hedefin dayandigi alanında yok)")

    # 8 GUNLUK
    gunluk_yol = os.path.join(kok, "00-sistem", "GUNLUK.md")
    gunluk = ""
    try:
        with open(gunluk_yol, encoding="utf-8") as f:
            gunluk = f.read()
    except FileNotFoundError:
        hata("00-sistem/GUNLUK.md", "yok")
    for yol, fm in fm_map.items():
        if fm.get("tur") == "ham":
            continue
        if yol not in gunluk and yc.normalize_yol(yol) not in gunluk:
            hata(yol, "günlükte kaydı yok (GUNLUK.md)")

    # 9 talimat
    talimat_yol = os.path.join(kok, "00-sistem", "TALIMATLAR.md")
    talimat_durum = {}
    try:
        with open(talimat_yol, encoding="utf-8") as f:
            mevcut = None
            for s in f.read().splitlines():
                m = re.match(r"^## (T-\d+)", s)
                if m:
                    mevcut = m.group(1)
                    talimat_durum[mevcut] = "?"
                m2 = re.match(r"^- Durum:\s*(\S+)", s)
                if m2 and mevcut:
                    talimat_durum[mevcut] = m2.group(1).lower()
    except FileNotFoundError:
        hata("00-sistem/TALIMATLAR.md", "yok")
    for yol, fm in fm_map.items():
        t = fm.get("talimat")
        if t not in talimat_durum:
            hata(yol, f"talimat TALIMATLAR.md'de yok: {t}")
        elif fm.get("durum") not in ("taslak", None) and talimat_durum[t] not in ("kapali", "bekliyor"):
            uyari(yol, f"sayfa {fm.get('durum')} ama talimat {t} hâlâ {talimat_durum[t]}")

    # 10 ADR simetrisi
    for yol, fm in fm_map.items():
        yg = fm.get("yerine_gecen")
        if yg:
            hn = yc.normalize_yol(yg) + ".md"
            if hn in fm_map and yc.normalize_yol(fm_map[hn].get("yerine_gecti") or "") != yc.normalize_yol(yol):
                hata(yol, f"supersede simetrik değil: {hn}.yerine_gecti ≠ {yol}")
            if fm.get("durum") != "yerine-gecildi":
                hata(yol, "yerine_gecen dolu ama durum yerine-gecildi değil")
        yt = fm.get("yerine_gecti")
        if yt:
            hn = yc.normalize_yol(yt) + ".md"
            if hn in fm_map and yc.normalize_yol(fm_map[hn].get("yerine_gecen") or "") != yc.normalize_yol(yol):
                hata(yol, f"supersede simetrik değil: {hn}.yerine_gecen ≠ {yol}")

    # 11 bayat (uyarı)
    for yol, fm in fm_map.items():
        sg = tarih(fm.get("son_gozden_gecirme"))
        if sg and (bugun - sg).days > 60:
            uyari(yol, f"bayat: son gözden geçirme {(bugun - sg).days} gün önce")
        al = tarih(fm.get("alindi"))
        if al and (bugun - al).days > 90:
            uyari(yol, f"TAZELIK: alındı {(bugun - al).days} gün önce, yeniden kontrol et")
        gb = tarih(fm.get("gecerli_bitis"))
        if gb and gb < bugun and fm.get("durum") in ("aktif", "kabul"):
            hata(yol, "gecerli_bitis geçmiş ama durum aktif/kabul")

    # 12 boyut
    cl = os.path.join(kok, "CLAUDE.md")
    try:
        n = sum(1 for _ in open(cl, encoding="utf-8"))
        if n > 200:
            hata("CLAUDE.md", f"{n} satır > 200")
    except FileNotFoundError:
        hata("CLAUDE.md", "yok")
    for dirpath, _d, files in os.walk(os.path.join(kok, ".claude", "skills")):
        for f in files:
            if f == "SKILL.md":
                p = os.path.join(dirpath, f)
                n = sum(1 for _ in open(p, encoding="utf-8"))
                if n > 500:
                    hata(os.path.relpath(p, kok), f"{n} satır > 500")

    # 13 kanıtsız tamam
    for yol, fm in fm_map.items():
        if fm.get("tur") == "gorev" and fm.get("kanban") == "tamam":
            k = fm.get("kanit")
            if not k:
                hata(yol, "kanıtsız tamam: kanban tamam ama kanit boş")

    # ---------- rapor ----------
    bag_sayisi = sum(len(liste(fm.get("dayandigi"))) for fm in fm_map.values())
    ciktikod = 1 if hatalar or (strict and uyarilar) else 0
    if as_json:
        print(json.dumps({"sayfa": len(fm_map), "bag": bag_sayisi, "hata": [{"yol": y, "mesaj": m} for y, m in hatalar],
                          "uyari": [{"yol": y, "mesaj": m} for y, m in uyarilar], "cikis": ciktikod}, ensure_ascii=False, indent=1))
        sys.exit(ciktikod)
    if not hatalar:
        print(f"Bütünlük tam: {len(fm_map)} sayfa, {bag_sayisi} bağ, {len(harita_satirlar)} harita satırı. Uyarı: {len(uyarilar)}.")
    else:
        print(f"BÜTÜNLÜK HATASI: {len(hatalar)} hata, {len(uyarilar)} uyarı ({len(fm_map)} sayfa, {bag_sayisi} bağ).")
    sinir = 15 if kisa else 40
    for y, m in hatalar[:sinir]:
        print(f"  HATA  {y}: {m}")
    if len(hatalar) > sinir:
        print(f"  … {len(hatalar) - sinir} hata daha (tam liste: --json)")
    if not kisa:
        for y, m in uyarilar[:15]:
            print(f"  uyarı {y}: {m}")
        if len(uyarilar) > 15:
            print(f"  … {len(uyarilar) - 15} uyarı daha")
    sys.exit(ciktikod)


if __name__ == "__main__":
    main()
