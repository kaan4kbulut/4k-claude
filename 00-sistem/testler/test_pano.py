"""pano.py regresyon testleri (T-034). Depo kopyasında koşar."""
import html
import os
import re
import sys
import unittest
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import betik, kopya_olustur, oku, yaz  # noqa: E402

CIKTI = "00-sistem/.kosu/pano"
EKRANLAR = ("pano.html", "saglik.html", "talimatlar.html", "gunluk.html", "kararlar.html")


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
        # Ayrıştırıcıyla: gerçek <script>/<style> etiketi, style ya da on* özniteliği, http(s) kaynağı (src/href) yok.
        # Düz metindeki "style=" ya da URL (ör. talimat metni) kaçışlanmış içeriktir, kaynak değildir (T-050).
        class Denetci(HTMLParser):
            def __init__(self):
                super().__init__()
                self.ihlal = []

            def handle_starttag(self, etiket, oz):
                if etiket in ("script", "style", "iframe"):
                    self.ihlal.append(etiket)
                for ad, deger in oz:
                    if ad == "style" or ad.startswith("on"):
                        self.ihlal.append(f"{etiket}[{ad}]")
                    if ad in ("src", "href") and re.match(r"\s*(https?:|//)", deger or "", re.I):
                        self.ihlal.append(f"{etiket}[{ad}={deger}]")

        self.uret()
        for ad in EKRANLAR:
            d = Denetci()
            d.feed(oku(self.kok, f"{CIKTI}/{ad}"))
            self.assertEqual(d.ihlal, [], ad)

    def test_yeni_ekranlar_kaynakla_ayni(self):
        self.uret()
        tal = oku(self.kok, "00-sistem/TALIMATLAR.md")
        idler = re.findall(r"(?m)^## (T-\d+) — ", tal)
        t = oku(self.kok, f"{CIKTI}/talimatlar.html")
        self.assertEqual(t.count('class="card" id="T-'), len(idler))
        self.assertIn(f'id="{idler[-1]}"', t)
        satir = [s for s in oku(self.kok, "00-sistem/GUNLUK.md").splitlines()
                 if re.match(r"\d{4}-\d\d-\d\d \d\d:\d\d \[\w+\] \S+", s)]
        self.assertIn(f"· {len(satir)} satır", oku(self.kok, f"{CIKTI}/gunluk.html"))
        k = oku(self.kok, f"{CIKTI}/kararlar.html")
        for no in re.findall(r"(?m)^- (K-\d+) · ", oku(self.kok, "00-sistem/KARARLAR.md")):
            self.assertIn(f'id="{no}"', k)

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
        self.assertEqual(sorted(os.listdir(os.path.join(self.kok, CIKTI))), ["css", *sorted(EKRANLAR)])

    def test_arguman_reddedilir(self):
        kod, _ = betik(self.kok, "pano.py", "--yaz")
        self.assertEqual(kod, 2)


if __name__ == "__main__":
    unittest.main()
