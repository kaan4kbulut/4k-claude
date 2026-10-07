#!/usr/bin/env python3
"""scorecard.py — SCORECARD sistem göstergelerini (S1–S8) dosyalardan hesaplar (T-029).

Kullanım:
  python3 00-sistem/scripts/scorecard.py                 bu haftanın değerleri ve hedef dışı olanlar
  python3 00-sistem/scripts/scorecard.py --yaz T-xxx     20-sirket/SCORECARD.md haftalık satırını yazar (aynı hafta güncellenir)
  python3 00-sistem/scripts/scorecard.py --json          JSON çıktı
Pencere: bugün dahil son 7 gün. Hafta etiketi ISO (2026-W41).
Ölçülemeyen gösterge "ölçülmüyor" yazar ve nedenini söyler; uydurma sayı yok (CLAUDE.md kural 5).
Çıkış: 0 hedefte, 1 hedef dışı gösterge var, 2 geçersiz girdi.
"""
import csv
import json
import os
import re
import subprocess
import sys
from datetime import date, datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yscommon as yc  # noqa: E402

SCORECARD = "20-sirket/SCORECARD.md"


def gun(s):
    try:
        return datetime.strptime(str(s)[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def oku(kok, yol):
    try:
        with open(os.path.join(kok, yol), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def talimatlar(kok):
    """{T-xxx: {tarih, durum, kapanis}}"""
    t, mevcut = {}, None
    for s in oku(kok, "00-sistem/TALIMATLAR.md").splitlines():
        m = re.match(r"^## (T-\d+)", s)
        if m:
            mevcut = m.group(1)
            t[mevcut] = {"tarih": None, "durum": "?", "kapanis": ""}
            continue
        if not mevcut:
            continue
        for alan, anahtar in (("Tarih", "tarih"), ("Durum", "durum"), ("Kapanış notu", "kapanis")):
            m = re.match(rf"^- {alan}:\s*(.*)$", s)
            if m:
                t[mevcut][anahtar] = gun(m.group(1)) if anahtar == "tarih" else m.group(1).strip()
    return t


def tavan(kok):
    m = re.search(r"^\| Orkestratör.*?oturum:\s*([\d.]+)\s*USD", oku(kok, "30-devlet/normlar/MODEL-POLITIKASI.md"), re.M)
    return float(m.group(1)) if m else None


def olc(kok, bugun):
    bas = bugun - timedelta(days=6)
    pencere = lambda d: d is not None and bas <= d <= bugun  # noqa: E731
    gunluk = oku(kok, "00-sistem/GUNLUK.md").splitlines()
    sayfalar = [(y, fm or {}) for y, fm, _, _ in yc.sayfalari_tara(kok)]
    g = {}

    # S1 kanıtla kapanan talimat %: kapanış notu dolu ve GUNLUK'te [oturum] T-xxx satırı olan
    kapali = {k: v for k, v in talimatlar(kok).items() if v["durum"] == "kapali" and pencere(v["tarih"])}
    if kapali:
        kanitli = [k for k, v in kapali.items()
                   if v["kapanis"] and any(re.match(rf"^\S+ \S+ \[oturum\] {k} ", s) for s in gunluk)]
        eksik = sorted(set(kapali) - set(kanitli), key=lambda k: int(k[2:]))
        g["S1"] = (round(100 * len(kanitli) / len(kapali)), len(kanitli) == len(kapali),
                   f"{len(kanitli)}/{len(kapali)}" + (f"; kaydı eksik: {', '.join(eksik)}" if eksik else ""))
    else:
        g["S1"] = ("—", True, "pencerede kapanan talimat yok")

    # S2 kontrol.py hata sayısı (ölçüm anı)
    r = subprocess.run([sys.executable, os.path.join(kok, "00-sistem", "scripts", "kontrol.py"), "--json"],
                       cwd=kok, capture_output=True, text=True, timeout=120)
    try:
        n = len(json.loads(r.stdout)["hata"])
        g["S2"] = (n, n == 0, "ölçüm anı (haftalık ortalama için her gün koşulmalı)")
    except (ValueError, KeyError):
        g["S2"] = ("ölçülmüyor", False, "kontrol.py --json okunamadı")

    # S3 açık görev ortalama yaşı (gün)
    acik = [gun(fm.get("olusturma")) for y, fm in sayfalar
            if fm.get("tur") == "gorev" and fm.get("kanban") not in ("tamam", "iptal")]
    yaslar = [(bugun - d).days for d in acik if d]
    if yaslar:
        ort = round(sum(yaslar) / len(yaslar), 1)
        g["S3"] = (ort, ort <= 7, f"{len(yaslar)} açık görev")
    else:
        g["S3"] = ("—", True, "açık görev yok")

    # S4 gelen kutusu: pencerede gelen notların 48 saatte işlenen yüzdesi
    gelen = [fm for y, fm in sayfalar if y.startswith("01-gelen/") and pencere(gun(fm.get("olusturma")))]
    if gelen:
        hizli = [fm for fm in gelen if fm.get("islendi") in (True, "true")
                 and gun(fm.get("islenme_tarihi")) and (gun(fm["islenme_tarihi"]) - gun(fm["olusturma"])).days <= 2]
        yuzde = round(100 * len(hizli) / len(gelen))
        g["S4"] = (yuzde, yuzde >= 90, f"{len(hizli)}/{len(gelen)}")
    else:
        g["S4"] = ("—", True, "pencerede gelen not yok")

    # S5 haftalık USD; hedef: hiçbir oturum MODEL-POLITIKASI oturum tavanını aşmaz
    t = tavan(kok)
    usd, asan = 0.0, []
    try:
        with open(os.path.join(kok, "00-sistem", "MALIYET.csv"), encoding="utf-8") as f:
            for satir in csv.DictReader(f):
                if not pencere(gun(satir.get("tarih"))):
                    continue
                m = re.match(r"^\s*([\d.]+)", satir.get("usd_tahmin") or "")
                if m:
                    v = float(m.group(1))
                    usd += v
                    if t is not None and v > t:
                        asan.append(f"{satir['session_id']} {v:.2f}")
        g["S5"] = (round(usd, 2), not asan, (f"tavanı aşan oturum: {', '.join(asan)}" if asan else "tavan aşımı yok")
                   + f" (tavan {t:g} USD/oturum)" if t is not None else "")
    except OSError:
        g["S5"] = ("ölçülmüyor", False, "MALIYET.csv yok")

    # S6 Stop hook engelleri: [durdu] ve 'kanıtsız durma' satırları
    n6 = sum(1 for s in gunluk if pencere(gun(s[:10])) and ("[durdu]" in s or "kanıtsız durma" in s))
    g["S6"] = (n6, True, "eğilim göstergesi (↓); önceki haftayla karşılaştır")

    # S7 flip sayacı: GUNLUK'te [konum] türü yok; ölçüm altyapısı kurulmadan sayı uydurulmaz
    g["S7"] = ("ölçülmüyor", True, "GUNLUK'te [konum] satır türü yok (SEMA §8)")

    # S8 açık bulgu sayısı ve en eski yaşı
    bulgular = [gun(fm.get("olusturma")) for y, fm in sayfalar
                if fm.get("tur") == "bulgu" and fm.get("durum") not in ("kapali", "arsiv", "reddedildi", "yerine-gecildi")]
    if bulgular:
        en_eski = max((bugun - d).days for d in bulgular if d)
        g["S8"] = (f"{len(bulgular)} / {en_eski} gün", False, "açık bulgu var")
    else:
        g["S8"] = ("0 / —", True, "açık bulgu yok (denetim hiç koşmadıysa bu bilgi değildir)")
    return g


def hafta(bugun):
    y, w, _ = bugun.isocalendar()
    return f"{y}-W{w:02d}"


def yaz(kok, g, bugun, talimat):
    yol = os.path.join(kok, SCORECARD)
    s = oku(kok, SCORECARD)
    h = hafta(bugun)
    issues = [f"{k}: {v[0]} — {v[2]}" for k, v in g.items() if not v[1]]
    satir = f"| {h} | " + " | ".join(str(g[k][0]) for k in sorted(g)) + f" | {'; '.join(k for k, v in g.items() if not v[1]) or '—'} |"
    if re.search(rf"^\| {h} \|.*$", s, re.M):
        s = re.sub(rf"^\| {h} \|.*$", satir, s, count=1, flags=re.M)
    else:
        bas = "| Hafta | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | Issues |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        if bas not in s:
            raise SystemExit("SCORECARD haftalık tablo başlığı bulunamadı")
        i = s.index(bas) + len(bas)
        while s[i:].startswith("| "):
            i = s.index("\n", i) + 1
        s = s[:i] + satir + "\n" + s[i:]
    s = re.sub(r"(### Issues \(off-track\)\n)(?:- .*\n)+",
               lambda m: m.group(1) + "".join(f"- {h} {x}\n" for x in issues) if issues else m.group(1) + "- —\n", s, count=1)
    m = re.search(r"^surum: (\d+)\.(\d+)$", s, re.M)
    yeni = f"{m.group(1)}.{int(m.group(2)) + 1}"
    s = s.replace(m.group(0), f"surum: {yeni}", 1)
    s = re.sub(r"^guncelleme: .*$", f"guncelleme: {bugun.isoformat()}", s, count=1, flags=re.M)
    s = s.rstrip("\n") + f"\n| {yeni} | {bugun.isoformat()} | {talimat} | Haftalık kayıt {h} (scorecard.py) |\n"
    with open(yol, "w", encoding="utf-8") as f:
        f.write(s)
    subprocess.run([sys.executable, os.path.join(kok, "00-sistem", "scripts", "gunluk.py"), "degisti", SCORECARD,
                    f"{yeni} — haftalık kayıt {h}: hedef dışı {len(issues)}"], cwd=kok, capture_output=True)
    return h, yeni


def main():
    arg = sys.argv[1:]
    kok = yc.kok_bul()
    bugun = date.today()
    talimat = None
    if "--yaz" in arg:
        i = arg.index("--yaz")
        talimat = arg[i + 1] if i + 1 < len(arg) else ""
        if not re.fullmatch(r"T-\d{3,}", talimat or ""):
            print("--yaz bir talimat numarası ister: --yaz T-xxx")
            sys.exit(2)
    g = olc(kok, bugun)
    dis = [k for k, v in g.items() if not v[1]]
    if "--json" in arg:
        print(json.dumps({"hafta": hafta(bugun), "gostergeler": {k: {"deger": v[0], "hedefte": v[1], "not": v[2]}
                                                                for k, v in g.items()}}, ensure_ascii=False, indent=1))
    else:
        print(f"Scorecard {hafta(bugun)} (son 7 gün):")
        for k in sorted(g):
            v = g[k]
            print(f"  {k} {'  ' if v[1] else '✗ '}{v[0]} — {v[2]}")
        print(f"Hedef dışı: {', '.join(dis) or 'yok'}")
    if talimat:
        h, yeni = yaz(kok, g, bugun, talimat)
        print(f"SCORECARD.md yazıldı: {h}, sürüm {yeni}")
    sys.exit(1 if dis else 0)


if __name__ == "__main__":
    main()
