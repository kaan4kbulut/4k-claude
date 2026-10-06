#!/usr/bin/env python3
"""harita.py — HARITA.md'yi frontmatter'dan üretir ya da doğrular.

  python3 00-sistem/scripts/harita.py --dogrula   eksik/fazla satırları listeler (yalnız okur)
  python3 00-sistem/scripts/harita.py --uret      HARITA.md'yi yeniden yazar (kat başlıkları altında, yol sırasıyla)
Satır biçimi: `- [[yol]] — amaç · tur · kat N · YYYY-MM-DD`
Şablonlar, arşiv ve ham notlar listelenmez. 200 satırı aşınca MOC bölme önerir.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yscommon as yc  # noqa: E402

BASLIKLAR = [("00-sistem", "00-sistem"), ("40-ic-ses", "40-ic-ses"), ("30-devlet", "30-devlet"), ("20-sirket", "20-sirket"), ("10-insan", "10-insan")]


def satir(yol, fm):
    tarih = fm.get("guncelleme") or fm.get("olusturma") or ""
    return f"- [[{yc.normalize_yol(yol)}]] — {fm.get('amac', '')} · {fm.get('tur')} · kat {fm.get('kat')} · {tarih}"


def main():
    kok = yc.kok_bul()
    sayfalar = [(y, fm) for y, fm, g, e in yc.sayfalari_tara(kok) if fm and not e and fm.get("tur") != "ham" and fm.get("durum") != "arsiv"]
    harita_yol = os.path.join(kok, "00-sistem", "HARITA.md")
    if "--uret" in sys.argv:
        bas = ("# Harita — dizin\n\nHer frontmatter'lı sayfa için tek satır: `- [[yol]] — amaç · tur · kat N · YYYY-MM-DD`. "
               "Şablonlar, arşiv ve ham notlar listelenmez. 200 satır tavanı; aşınca MOC'lara bölünür (harita.py uyarır). "
               "Önce burayı oku, sonra yalnız gereken sayfayı aç.\n\n")
        parcalar = [bas]
        for onek, baslik in BASLIKLAR:
            grup = sorted([(y, fm) for y, fm in sayfalar if y.startswith(onek + "/")])
            parcalar.append(f"## {baslik}\n")
            for y, fm in grup:
                parcalar.append(satir(y, fm) + "\n")
            parcalar.append("\n")
        with open(harita_yol, "w", encoding="utf-8") as f:
            f.write("".join(parcalar).rstrip("\n") + "\n")
        print(f"HARITA.md yazıldı: {len(sayfalar)} satır." + (" UYARI: 200 aşıldı, MOC'lara böl." if len(sayfalar) > 200 else ""))
        return
    # doğrula
    try:
        with open(harita_yol, encoding="utf-8") as f:
            mevcut = [s for s in f.read().splitlines() if s.startswith("- [[")]
    except FileNotFoundError:
        print("HARITA.md yok"); sys.exit(1)
    hedefler = {}
    for s in mevcut:
        h = s[4:].split("]]")[0].split("|")[0]
        hedefler[yc.normalize_yol(h)] = hedefler.get(yc.normalize_yol(h), 0) + 1
    eksik = [y for y, fm in sayfalar if yc.normalize_yol(y) not in hedefler]
    fazla = [h for h in hedefler if not yc.hedef_var(kok, h)]
    cift = [h for h, n in hedefler.items() if n > 1]
    print(f"HARITA: {len(mevcut)} satır, {len(sayfalar)} sayfa. Eksik {len(eksik)}, fazla {len(fazla)}, çift {len(cift)}." + (" UYARI: 200 aşıldı." if len(mevcut) > 200 else "") + (" 180+ : MOC bölme zamanı yaklaşıyor." if 180 <= len(mevcut) <= 200 else ""))
    for y in eksik:
        print(f"  eksik: {y}")
    for h in fazla:
        print(f"  fazla: {h}")
    for h in cift:
        print(f"  çift : {h}")
    sys.exit(1 if (eksik or fazla or cift) else 0)


if __name__ == "__main__":
    main()
