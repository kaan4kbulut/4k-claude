#!/usr/bin/env python3
"""ara-olcum.py — ara.py'nin Türkçe isabet ölçümü (yalnız okur; dizini değiştirmez).

Kullanım:
  python3 00-sistem/scripts/ara-olcum.py              üç kip: kelime (BM25), vektor, hibrit
  python3 00-sistem/scripts/ara-olcum.py --kip vektor
  python3 00-sistem/scripts/ara-olcum.py --json
Çıkış: 0. Ölçüt: isabet@1 ve isabet@3 (beklenen sayfa ilk 1 / ilk 3 sonuçta mı).

Sorgular sayfa başlıklarını kopyalamaz; günlük Türkçeyle, çekimli sözcüklerle sorulur (anlamsal aramayı sınamak için).
Wiki büyüdükçe sorgu kümesi genişletilmeli; ölçüm sonucu 40-ic-ses/arastirma-notlari'na yazılır.
"""
import json
import os
import subprocess
import sys
import time

BURASI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURASI)
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location("ara", os.path.join(BURASI, "ara.py"))
ara = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ara)

SORGULAR = [
    ("hangi model ne kadar pahalı, token fiyatları", "30-devlet/normlar/MODEL-POLITIKASI.md"),
    ("kim neyi imzalamak zorunda, yetki devri nasıl yapılır", "30-devlet/normlar/IMZA-MATRISI.md"),
    ("bir modelin başka bir modelin cevabını puanlaması", "30-devlet/normlar/HAKEM-KURALLARI.md"),
    ("sistemin değiştirilemeyen temel maddeleri", "30-devlet/normlar/ANAYASA.md"),
    ("ilk aşamada rol ajanlarının açılmaması kararı", "30-devlet/kararlar/K-001-pilotta-kadro-yok.md"),
    ("danışman ayrı bir ajan olarak mı çalışmalı", "30-devlet/kararlar/K-002-danisman-zihin-islevi.md"),
    ("sistemin isminin değiştirilmesi", "30-devlet/kararlar/K-003-ad-degisikligi-4k-claude.md"),
    ("kabuk komutlarını işletim sistemi düzeyinde kısıtlama onayı", "30-devlet/kapilar/KP-001-sandbox-acilisi.md"),
    ("yazıcı satın alıp para kazanma düşüncesi", "40-ic-ses/fikirler/F-0001-yazici-isi-fikri.md"),
    ("son oturumda nerede kalmıştık", "40-ic-ses/nerede-kaldik.md"),
    ("üç boyutlu baskı işinde filament ve dilimleme", "20-sirket/alan-paketleri/3d-uretim.md"),
    ("haftalık toplantıların düzeni ve takvimi", "20-sirket/RITIM.md"),
    ("performans göstergeleri ve haftalık ölçümler", "20-sirket/SCORECARD.md"),
    ("kurulu araçlar, ödeme kargo muhasebe yetenekleri", "10-insan/araclar/ARAC-KAYDI.md"),
    ("sayfa başlığındaki zorunlu alanlar ve türleri", "00-sistem/SEMA.md"),
    ("klasörler nerede, sistemde nasıl gezinilir", "00-sistem/SISTEM.md"),
    ("kancalar, alt ajanlar ve beceriler nasıl çalışıyor", "00-sistem/arastirma/01-claude-code-mekanikleri.md"),
    ("sesli sohbette konuşma sırası ve dalkavukluk", "00-sistem/arastirma/08-ic-ses-yontemleri.md"),
    ("Sayıştay, iç denetim ve bakanlıkların yapısı", "00-sistem/arastirma/07-devlet-yapilari.md"),
    ("bilgi grafı ve yerel arama araçlarının taraması", "00-sistem/arastirma/10-yenilikci-teknolojiler.md"),
]
KIPLER = {"kelime": "search", "vektor": "vsearch", "hibrit": "query"}


def yol_coz(qmd_yolu):
    """qmd://devlet/normlar/X.md → 30-devlet/normlar/X.md"""
    g = qmd_yolu.replace("qmd://", "", 1)
    ad, _, kalan = g.partition("/")
    klasor = {k[0]: k[1] for k in ara.KOLEKSIYONLAR}.get(ad, ad)
    return f"{klasor}/{kalan}"


def calistir(kip, sorgu):
    r = subprocess.run([ara.QMD, KIPLER[kip], sorgu, "-n", "3", "--json"], cwd=ara.KOK, env=ara.ortam(),
                       capture_output=True, text=True)
    try:
        return [yol_coz(x["file"]) for x in json.loads(r.stdout or "[]")]
    except json.JSONDecodeError:
        return []


def main():
    arg = sys.argv[1:]
    kipler = [arg[arg.index("--kip") + 1]] if "--kip" in arg else list(KIPLER)
    sonuc = {}
    for kip in kipler:
        b = time.time()
        ayrinti = []
        for sorgu, beklenen in SORGULAR:
            bulunan = calistir(kip, sorgu)
            sira = bulunan.index(beklenen) + 1 if beklenen in bulunan else None
            ayrinti.append({"sorgu": sorgu, "beklenen": beklenen, "sira": sira, "ilk": bulunan[:1]})
        n = len(SORGULAR)
        sonuc[kip] = {"isabet1": sum(1 for a in ayrinti if a["sira"] == 1) / n,
                      "isabet3": sum(1 for a in ayrinti if a["sira"]) / n,
                      "bos": sum(1 for a in ayrinti if not a["ilk"]),
                      "sure_sn": round(time.time() - b, 1), "ayrinti": ayrinti}
    if "--json" in arg:
        print(json.dumps(sonuc, ensure_ascii=False, indent=1))
        return
    print(f"{'kip':8} {'isabet@1':>9} {'isabet@3':>9} {'boş':>4} {'süre':>7}")
    for kip, s in sonuc.items():
        print(f"{kip:8} {s['isabet1']:>9.0%} {s['isabet3']:>9.0%} {s['bos']:>4} {s['sure_sn']:>6}s")
    for kip, s in sonuc.items():
        kacan = [a for a in s["ayrinti"] if not a["sira"]]
        if kacan:
            print(f"  {kip} kaçırdı: " + "; ".join(f"«{a['sorgu'][:38]}» → {a['ilk'][0] if a['ilk'] else 'boş'}" for a in kacan[:6]))


if __name__ == "__main__":
    main()
