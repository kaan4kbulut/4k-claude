"""pano.py regresyon testleri (T-034). Depo kopyasında koşar."""
import html
import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import betik, kopya_olustur, oku, yaz  # noqa: E402

CIKTI = "00-sistem/.kosu/pano"


class Pano(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()

    def tearDown(self):
        self.temizle()

    def uret(self):
        kod, cikti = betik(self.kok, "pano.py")
        self.assertEqual(kod, 0, cikti)
        return oku(self.kok, f"{CIKTI}/pano.html"), oku(self.kok, f"{CIKTI}/saglik.html")

    def test_iki_ekran_ve_css(self):
        self.uret()
        for ad in ("css/4k-claude.css", "css/pano.css", "css/saglik.css"):
            self.assertTrue(os.path.isfile(os.path.join(self.kok, CIKTI, ad)), ad)

    def test_betik_stil_ag_yok(self):
        for h in self.uret():
            self.assertIsNone(re.search(r"<script|style=|https?:", h, re.I))

    def test_ilerleme_alanlari_panoda(self):
        il = oku(self.kok, "00-sistem/ILERLEME.md")
        for alan, deger in (("aktif_talimat", "T-998"), ("kapi", "KP-999"), ("acik_soru", "S-997")):
            il = re.sub(rf"(?m)^{alan}: .*$", f"{alan}: {deger} — deneme {alan}", il)
        yaz(self.kok, "00-sistem/ILERLEME.md", il)
        p, _ = self.uret()
        for deger in ("T-998", "KP-999", "S-997"):
            self.assertIn(f">{deger}<", p)
        sira = re.search(r"(?m)^siradaki: (.*)$", il).group(1)
        self.assertIn(html.escape(sira), p)

    def test_nerede_kaldik_bloklari(self):
        nk = oku(self.kok, "40-ic-ses/nerede-kaldik.md")
        for blok in ("Konuşulan", "Açık", "Sonraki"):
            nk = nk.replace(f"**{blok}**\n", f"**{blok}**\n- deneme-{blok}-satiri\n", 1)
        yaz(self.kok, "40-ic-ses/nerede-kaldik.md", nk)
        p, _ = self.uret()
        for blok in ("Konuşulan", "Açık", "Sonraki"):
            self.assertIn(f"deneme-{blok}-satiri", p)

    def test_metin_kacislanir(self):
        il = oku(self.kok, "00-sistem/ILERLEME.md")
        yaz(self.kok, "00-sistem/ILERLEME.md", re.sub(r"(?m)^kapi: .*$", 'kapi: <b onx="1">K</b>', il))
        p, _ = self.uret()
        self.assertNotIn("<b onx", p)
        self.assertIn("&lt;b", p)

    def test_bozuk_girdide_cokmez(self):
        yaz(self.kok, "00-sistem/MALIYET.csv", "a,b\n1,2\n")
        yaz(self.kok, "00-sistem/ILERLEME.md", "bozuk\n")
        p, _ = self.uret()
        self.assertIn("belirlenmedi", p)

    def test_saglik_ozeti_kontrol_ile_ayni(self):
        _, s = self.uret()
        _, kisa = betik(self.kok, "kontrol.py", "--kisa")
        self.assertIn(html.escape(kisa.strip().splitlines()[0]), s)

    def test_depoya_yazmaz(self):
        sys.path.insert(0, os.path.join(self.kok, "00-sistem", "scripts"))
        import yscommon as yc
        once = yc.dosya_izi(self.kok)
        self.uret()
        fark = [y for y in yc.iz_farki(once, yc.dosya_izi(self.kok)) if not y.startswith(CIKTI + "/")]
        self.assertEqual(fark, [])
        self.assertEqual(sorted(os.listdir(os.path.join(self.kok, CIKTI))), ["css", "pano.html", "saglik.html"])

    def test_arguman_reddedilir(self):
        kod, _ = betik(self.kok, "pano.py", "--yaz")
        self.assertEqual(kod, 2)


if __name__ == "__main__":
    unittest.main()
