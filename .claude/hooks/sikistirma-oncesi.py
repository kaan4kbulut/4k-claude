#!/usr/bin/env python3
"""PreCompact hook — sikistirma-oncesi.

Bağlam sıkıştırılmadan önce ILERLEME.md'nin güncel olduğundan emin olur.
Kural: ILERLEME.md, kat klasörleri ve 00-sistem altındaki en son değiştirilmiş .md dosyasından daha eski olamaz.
Eskiyse çıkış kodu 2 ile sıkıştırmayı ENGELLER ve stderr'e ne yapılacağını yazar
(Claude ILERLEME.md'yi yazdıktan sonra sıkıştırma yeniden denenir).
Otomatik sıkıştırmada bu engel "önce ilerleme yaz" demektir; manuel /compact'ta da aynı.
Tolerans: 90 saniye (aynı adımda yazılan dosyalar için).
"""
import json
import os
import sys

KATLAR = ("00-sistem", "01-gelen", "10-insan", "20-sirket", "30-devlet", "40-ic-ses")


def en_yeni_md(kok):
    en = 0.0
    yol_en = ""
    for kat in KATLAR:
        d = os.path.join(kok, kat)
        for dirpath, _dirs, files in os.walk(d):
            for f in files:
                if f.endswith(".md") and f != "ILERLEME.md" and f != "GUNLUK.md":
                    p = os.path.join(dirpath, f)
                    try:
                        m = os.path.getmtime(p)
                    except OSError:
                        continue
                    if m > en:
                        en, yol_en = m, p
    return en, yol_en


def main():
    try:
        girdi = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        girdi = {}
    kok = os.environ.get("CLAUDE_PROJECT_DIR") or girdi.get("cwd") or os.getcwd()
    ilerleme = os.path.join(kok, "00-sistem", "ILERLEME.md")
    if not os.path.exists(ilerleme):
        sys.stderr.write("4k-claude: 00-sistem/ILERLEME.md yok. Sıkıştırmadan önce aktif talimat, kapı, açık soru, değişen dosyalar ve sıradaki adımı yaz.\n")
        sys.exit(2)
    en, yol_en = en_yeni_md(kok)
    try:
        ilerleme_m = os.path.getmtime(ilerleme)
    except OSError:
        ilerleme_m = 0
    if en - ilerleme_m > 90:
        sys.stderr.write(
            "4k-claude: ILERLEME.md, son değişen dosyadan eski (" + os.path.relpath(yol_en, kok) + "). "
            "Sıkıştırmadan önce ILERLEME.md'yi güncelle: aktif_talimat, kapi, acik_soru, degisen_dosyalar, siradaki.\n"
        )
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
