#!/usr/bin/env python3
"""gunluk.py — GUNLUK.md'ye tek satır ekler; zaman damgasını sistem saati basar.

Kullanım:
  python3 00-sistem/scripts/gunluk.py <tur> <yol|T-xxx> "<not>"
Örnek:
  python3 00-sistem/scripts/gunluk.py yeni 40-ic-ses/fikirler/F-0002-x.md "fikir kaydedildi; merdiven 1"

Neden: model saati bilmez; elle yazılan damga uydurma olur (CLAUDE.md kural 5) ve günlük sırası bozulur.
Satır biçimi SEMA §8: `YYYY-MM-DD HH:MM [tur] yol — not`. Yalnız sona ekler; hiçbir satırı değiştirmez.
Çıkış: 0 yazıldı, 2 geçersiz girdi.
"""
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yscommon as yc  # noqa: E402

TURLER = ("yeni", "degisti", "arsiv", "karar", "kapi", "hata", "durdu", "ayar", "oturum", "uyku")


def main():
    if len(sys.argv) != 4:
        print(__doc__.strip().splitlines()[2])
        sys.exit(2)
    tur, yol, not_ = sys.argv[1], sys.argv[2].strip(), " ".join(sys.argv[3].split())
    if tur not in TURLER:
        print(f"geçersiz tür: {tur} (izinli: {', '.join(TURLER)})")
        sys.exit(2)
    if not yol or not not_:
        print("yol ve not boş olamaz")
        sys.exit(2)
    satir = f"{datetime.now().strftime('%Y-%m-%d %H:%M')} [{tur}] {yol} — {not_}"
    with open(os.path.join(yc.kok_bul(), "00-sistem", "GUNLUK.md"), "a", encoding="utf-8") as f:
        f.write(satir + "\n")
    print(satir)


if __name__ == "__main__":
    main()
