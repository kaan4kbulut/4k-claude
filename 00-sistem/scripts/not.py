#!/usr/bin/env python3
"""not.py — hafif yol: İç Ses'e gözlem ya da ham fikir (M0) notunu altı adımın hepsini tek komutla yaparak ekler.

Kullanım:
  python3 00-sistem/scripts/not.py gozlem "<başlık>" "<ne görüldü>" [--kaynak <yol|URL>] [--onem 1-10]
  python3 00-sistem/scripts/not.py fikir "<başlık>" "<tek cümle>"
Çıkış kodu: 0 eklendi (kontrol.py temiz); 1 kontrol.py hata verdi; 2 kullanım hatası; 3 KR-001 yürürlükte değil.

KR-001 (hafif yol) kuralına dayanır ve yalnız o kural `durum: kabul` iken çalışır (kural yayımı sahibinin imzasıdır,
IMZA-MATRISI A4). Anayasa Madde 3.2 "küçük işte yol kısalır, atlanmaz": bu betik adımları atlamaz, otomatikleştirir:
  1 KAYIT       TALIMATLAR.md'ye yeni T-xxx (niyet + başarı ölçütü), sonunda kapatır
  2 AMAÇ + KAT  kat 4, amaç cümlesi başlıktan
  3 YER + AD    40-ic-ses/gozlemler/YYYY-MM-DD-<ad>.md ya da 40-ic-ses/fikirler/F-xxxx-<ad>.md (numara sıradaki)
  4 ŞABLON      00-sistem/sablonlar/<tur>.md alanlarıyla; bilinmeyen alan "belirlenmedi"
  5 BAĞLAR      ust MOC-ic-ses ve MOC'ta satır (gözlemler listesi ya da merdiven M0 satırı)
  6 KAPANIŞ     HARITA (harita.py --uret), GUNLUK (gunluk.py), talimat kapanışı, kontrol.py --kisa
Kapsam dışı (tam yol gerekir): merdiven ≥ 1 fikir, karar, görev, kaynak ve bağlı (dayandigi) sayfalar.
"""
import json
import os
import re
import subprocess
import sys
import unicodedata
from datetime import datetime

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(os.path.dirname(BURASI))
KURAL = os.path.join(KOK, "30-devlet", "normlar", "kurallar", "KR-001-hafif-yol.md")
TR = str.maketrans({"ş": "s", "Ş": "s", "ı": "i", "İ": "i", "ğ": "g", "Ğ": "g", "ü": "u", "Ü": "u",
                    "ö": "o", "Ö": "o", "ç": "c", "Ç": "c", "â": "a", "î": "i", "û": "u"})


def ascii_metin(s):
    return unicodedata.normalize("NFKD", s.translate(TR)).encode("ascii", "ignore").decode()


def slug(s, n=40):
    t = re.sub(r"[^a-z0-9]+", "-", ascii_metin(s).lower()).strip("-")
    return t[:n].rstrip("-") or "not"


def yaml_dizgi(s):
    return json.dumps(s, ensure_ascii=False)


def kural_yururlukte():
    try:
        with open(KURAL, encoding="utf-8") as f:
            return re.search(r"^durum:\s*kabul\s*$", f.read(), re.M) is not None
    except FileNotFoundError:
        return False


def calistir(*komut):
    return subprocess.run([sys.executable, *komut], cwd=KOK, capture_output=True, text=True)


def main():
    arg = sys.argv[1:]
    if len(arg) < 3 or arg[0] not in ("gozlem", "fikir"):
        print(__doc__.strip().splitlines()[2] + "\n" + __doc__.strip().splitlines()[3])
        sys.exit(2)
    if not kural_yururlukte():
        print("Hafif yol kapalı: KR-001 yürürlükte değil (durum: kabul değil). Kural yayımı sahibinin imzasıdır "
              "(IMZA-MATRISI A4). O zamana kadar /yeni-parca ile tam yol kullanılır.")
        sys.exit(3)
    tur, baslik, metin = arg[0], arg[1].strip(), arg[2].strip()
    if not baslik or not metin or len(baslik) > 120 or len(metin) > 4000:
        print("Başlık 1-120, metin 1-4000 karakter olmalı.")
        sys.exit(2)
    kaynak = arg[arg.index("--kaynak") + 1] if "--kaynak" in arg else "sahibi (sohbet)"
    onem = int(arg[arg.index("--onem") + 1]) if "--onem" in arg else 5
    if not 1 <= onem <= 10:
        print("--onem 1-10 olmalı.")
        sys.exit(2)

    simdi = datetime.now()
    tarih, saat = f"{simdi:%Y-%m-%d}", f"{simdi:%Y%m%d-%H%M}"
    tal_yol = os.path.join(KOK, "00-sistem", "TALIMATLAR.md")
    talimatlar = open(tal_yol, encoding="utf-8").read()
    tno = f"T-{max(int(n) for n in re.findall(r'^## T-(\d+)', talimatlar, re.M)) + 1:03d}"

    # 3 YER + AD
    if tur == "fikir":
        mevcut = [int(m) for m in re.findall(r"F-(\d{4})-", " ".join(os.listdir(os.path.join(KOK, "40-ic-ses", "fikirler"))))]
        fno = f"F-{max(mevcut, default=0) + 1:04d}"
        ad = f"{fno}-{slug(baslik)}"
        goreli = f"40-ic-ses/fikirler/{ad}.md"
    else:
        ad = f"{tarih}-{slug(baslik)}"
        goreli = f"40-ic-ses/gozlemler/{ad}.md"
    yol = os.path.join(KOK, goreli)
    if os.path.exists(yol):
        print(f"Aynı adda sayfa var: {goreli}")
        sys.exit(2)

    # 1 KAYIT
    with open(tal_yol, "a", encoding="utf-8") as f:
        f.write(f"\n## {tno} — Hafif yol: {tur} \"{baslik}\"\n- Tarih: {tarih}\n"
                f"- Niyet: KR-001 hafif yoluyla 40-ic-ses'e {tur} notu eklemek.\n"
                f"- Başarı ölçütü: {goreli} var; HARITA, MOC ve GUNLUK satırı; kontrol.py sıfır hata.\n"
                f"- Sınırlar: Değerlendirme yok; yalnız kayıt (KR-001).\n- Kat: 4\n- Kapı: cift-yonlu\n- Durum: acik\n"
                f"- Doğurduğu dosyalar:\n- Kapanış notu:\n")

    # 2 AMAÇ + KAT, 4 ŞABLON
    a_baslik = ascii_metin(baslik).replace('"', "'")
    if tur == "gozlem":
        amac = f"Bu gozlem, {tarih} tarihinde fark edilen '{a_baslik}' olgusunu kaynagiyla kaydetmek icin var."
        ozel = f"kaynaklar: [{yaml_dizgi(kaynak)}]\nonem: {onem}\n"
        govde = (f"# Gözlem: {baslik}\n\n## Amaç\n{amac}\n\n## İçerik\n### Ne görüldü\n{metin}\n\n### Bağlam\nbelirlenmedi\n\n"
                 f"### İşaretler\nbelirlenmedi\n\n### Olası sonraki adım\nbelirlenmedi\n\n")
    else:
        amac = f"Bu fikir, '{a_baslik}' onerisini kaydetmek ve olgunlastirmak icin var (merdiven 0, ham)."
        ozel = (f"merdiven: 0\ncynefin: belirlenmedi\nguven: dusuk\nkaynaklar: []\ndokunus_sayisi: 1\n"
                f"son_dokunus: {yaml_dizgi(tarih)}\nkapi: belirlenmedi\n")
        govde = (f"# Fikir {fno}: {baslik}\n\n## Amaç\n{amac}\n\n## İçerik\n### Tek cümle\n{metin}\n\n"
                 "### Çerçeve (üçüncü şahıs)\nbelirlenmedi\n\n### Neden şimdi\nbelirlenmedi\n\n### Kanıt\n- henüz yok\n"
                 "### Karşı-kanıt\n- aranmadı\n\n### Açık sorular (M3 için ≤2)\n- belirlenmedi\n\n")
    fm = (f"---\nid: {saat}-{slug(baslik, 30)}\nad: {ad.lower()}\ntur: {tur}\nkat: 4\nsurum: 0.1\ndurum: taslak\n"
          f"amac: {yaml_dizgi(amac)}\nolusturma: {tarih}\nguncelleme: {tarih}\nyazar: claude\ntalimat: {tno}\n"
          f"dayandigi: []\nbesledigi: []\nust: 40-ic-ses/MOC-ic-ses.md\n{ozel}etiketler: [hafif-yol]\n---\n\n")
    bag = (f"## Bağlar\n### Dayandığı\n### Beslediği\n### Gelen\n- ← [[40-ic-ses/MOC-ic-ses]] — "
           f"{'gözlemler listesi' if tur == 'gozlem' else 'merdiven tablosu, M0'}\n\n"
           f"## Günlük\n| Sürüm | Tarih | Talimat | Değişiklik |\n| --- | --- | --- | --- |\n"
           f"| 0.1 | {tarih} | {tno} | Oluşturuldu (hafif yol, KR-001) |\n")
    with open(yol, "w", encoding="utf-8") as f:
        f.write(fm + govde + bag)

    # 5 BAĞLAR: MOC satırı
    moc_yol = os.path.join(KOK, "40-ic-ses", "MOC-ic-ses.md")
    moc = open(moc_yol, encoding="utf-8").read()
    wiki = f"[[{goreli[:-3]}]] — {baslik}"
    if tur == "gozlem":
        bas = moc.index("### Gözlemler (son 30 gün)\n") + len("### Gözlemler (son 30 gün)\n")
        moc = moc[:bas] + f"- {wiki} ({tarih})\n" + moc[bas:].replace("- —\n", "", 1) if moc[bas:].startswith("- —\n") \
            else moc[:bas] + f"- {wiki} ({tarih})\n" + moc[bas:]
    else:
        m = re.search(r"^\| M0 ham \| (.*) \|$", moc, re.M)
        eski = m.group(1)
        yeni = wiki if eski.strip() == "—" else f"{eski}<br>{wiki}"
        moc = moc[:m.start(1)] + yeni + moc[m.end(1):]
    with open(moc_yol, "w", encoding="utf-8") as f:
        f.write(moc)

    # 6 KAPANIŞ
    calistir(os.path.join(BURASI, "harita.py"), "--uret")
    calistir(os.path.join(BURASI, "gunluk.py"), "yeni", goreli, f"hafif yol (KR-001): {baslik[:80]}")
    calistir(os.path.join(BURASI, "gunluk.py"), "degisti", "40-ic-ses/MOC-ic-ses.md", f"{tno}: {ad} satırı")
    talimatlar = open(tal_yol, encoding="utf-8").read()
    i = talimatlar.index(f"## {tno} —")
    t = talimatlar[i:]
    t = t.replace("- Durum: acik", "- Durum: kapali", 1).replace("- Doğurduğu dosyalar:\n", f"- Doğurduğu dosyalar: {goreli}\n", 1)
    t = t.replace("- Kapanış notu:", "- Kapanış notu: hafif yol (not.py); altı adım otomatik.", 1)
    with open(tal_yol, "w", encoding="utf-8") as f:
        f.write(talimatlar[:i] + t)
    calistir(os.path.join(BURASI, "gunluk.py"), "oturum", tno, "kapandı — hafif yol")
    k = calistir(os.path.join(BURASI, "kontrol.py"), "--kisa")
    print(f"## Kanıt\n- sayfa: {goreli} ({tno})\n- `python3 00-sistem/scripts/kontrol.py --kisa` → {k.returncode}: "
          f"{k.stdout.strip().splitlines()[0] if k.stdout.strip() else k.stderr.strip()[:200]}")
    if k.returncode:
        print(k.stdout.strip())
    sys.exit(1 if k.returncode else 0)


if __name__ == "__main__":
    main()
