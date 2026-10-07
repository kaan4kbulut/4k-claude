"""kontrol.py ve gunluk.py regresyon testleri (T-027). Depo kopyasında koşar; her test bir denetimi bozar."""
import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import betik, kopya_olustur, oku, yaz  # noqa: E402


class Kontrol(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()

    def tearDown(self):
        self.temizle()

    def kontrol(self):
        return betik(self.kok, "kontrol.py", "--kisa")

    def degistir(self, yol, eski, yeni):
        s = oku(self.kok, yol)
        self.assertIn(eski, s, f"test kurulumu: {yol} içinde {eski!r} yok")
        yaz(self.kok, yol, s.replace(eski, yeni, 1))

    def bozuk(self, beklenen):
        kod, cikti = self.kontrol()
        self.assertEqual(kod, 1, cikti)
        self.assertIn(beklenen, cikti)

    def test_temiz_kopya_gecer(self):
        kod, cikti = self.kontrol()
        self.assertEqual(kod, 0, cikti)

    def test_haritada_olmayan_sayfa(self):
        h = oku(self.kok, "00-sistem/HARITA.md")
        yaz(self.kok, "00-sistem/HARITA.md", "\n".join(s for s in h.splitlines() if "KP-003-github" not in s) + "\n")
        self.bozuk("haritada yok")

    def test_tek_yonlu_bag(self):
        self.degistir("30-devlet/kapilar/KP-002-kr-001-yayimi.md", "besledigi: []",
                      "besledigi: [40-ic-ses/nerede-kaldik.md]")
        self.bozuk("tek yönlü bağ")

    def test_kirik_bag(self):
        self.degistir("30-devlet/kapilar/KP-002-kr-001-yayimi.md", "besledigi: []", "besledigi: [40-ic-ses/yok.md]")
        self.bozuk("kırık bağ")

    def test_frontmatter_yok(self):
        yaz(self.kok, "40-ic-ses/gozlemler/frontmattersiz.md", "# Başlık\n")
        self.bozuk("frontmatter yok")

    def test_kat_uyusmazligi(self):
        self.degistir("30-devlet/kapilar/KP-002-kr-001-yayimi.md", "kat: 3", "kat: 2")
        self.bozuk("kat uyuşmazlığı")

    def test_birden_cok_acik_talimat(self):
        s = oku(self.kok, "00-sistem/TALIMATLAR.md")
        yaz(self.kok, "00-sistem/TALIMATLAR.md", s + "\n## T-998 — deneme\n- Durum: acik\n\n## T-999 — deneme\n- Durum: acik\n")
        self.bozuk("birden çok açık talimat")

    def test_son_kapanis_nerede_kaldikta_yok(self):
        s = oku(self.kok, "00-sistem/TALIMATLAR.md")
        son = sorted(re.findall(r"^## (T-\d+)", s, re.M), key=lambda t: int(t[2:]))[-1]
        n = int(son[2:]) + 1
        yeni = f"T-{n:03d}"
        yaz(self.kok, "00-sistem/TALIMATLAR.md",
            re.sub(r"- Durum: acik", "- Durum: kapali", s) + f"\n## {yeni} — deneme\n- Durum: kapali\n")
        g = oku(self.kok, "00-sistem/GUNLUK.md")
        yaz(self.kok, "00-sistem/GUNLUK.md", g + f"2099-01-01 00:00 [oturum] {yeni} — kapandı — deneme\n")
        ilerleme = oku(self.kok, "00-sistem/ILERLEME.md")
        yaz(self.kok, "00-sistem/ILERLEME.md", re.sub(r"^aktif_talimat:.*$", f"aktif_talimat: yok — {yeni} kapandı",
                                                     ilerleme, count=1, flags=re.M))
        self.bozuk(f"son kapanan {yeni} yazılmamış")

    def test_kanitsiz_tamam(self):
        yol = "20-sirket/gorevler/G-001-yazici-pazar-arastirmasi.md"
        s, n = re.subn(r"^kanit:\n(?:  - .*\n)+", "kanit: []\n", oku(self.kok, yol), flags=re.M)
        self.assertEqual(n, 1, "test kurulumu: kanit listesi bulunamadı")
        yaz(self.kok, yol, s)
        self.bozuk("kanıtsız tamam")


class Gunluk(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()

    def tearDown(self):
        self.temizle()

    def test_gecersiz_tur_reddedilir(self):
        kod, _ = betik(self.kok, "gunluk.py", "uydurma", "T-001", "not")
        self.assertEqual(kod, 2)

    def test_eksik_arguman_reddedilir(self):
        kod, _ = betik(self.kok, "gunluk.py", "yeni", "T-001")
        self.assertEqual(kod, 2)

    def test_satir_sona_eklenir_ve_saati_sistem_basar(self):
        once = oku(self.kok, "00-sistem/GUNLUK.md")
        kod, _ = betik(self.kok, "gunluk.py", "degisti", "40-ic-ses/nerede-kaldik.md", "çok   boşluklu\nnot")
        self.assertEqual(kod, 0)
        sonra = oku(self.kok, "00-sistem/GUNLUK.md")
        self.assertTrue(sonra.startswith(once))
        self.assertRegex(sonra.splitlines()[-1],
                         r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2} \[degisti\] 40-ic-ses/nerede-kaldik\.md — çok boşluklu not$")


if __name__ == "__main__":
    unittest.main()
