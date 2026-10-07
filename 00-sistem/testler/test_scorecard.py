"""scorecard.py regresyon testleri (T-029). Depo kopyasında koşar."""
import json
import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import betik, kopya_olustur, oku, yaz  # noqa: E402

SC = "20-sirket/SCORECARD.md"


class Scorecard(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()

    def tearDown(self):
        self.temizle()

    def json(self):
        kod, cikti = betik(self.kok, "scorecard.py", "--json")
        self.assertIn(kod, (0, 1), cikti)
        return json.loads(cikti)

    def test_sekiz_gosterge(self):
        g = self.json()["gostergeler"]
        self.assertEqual(sorted(g), [f"S{i}" for i in range(1, 9)])

    def test_gecersiz_talimat_reddedilir(self):
        kod, _ = betik(self.kok, "scorecard.py", "--yaz", "deneme")
        self.assertEqual(kod, 2)

    def test_ayni_hafta_iki_kez_yazilinca_tek_satir(self):
        hafta = self.json()["hafta"]
        surum_once = re.search(r"^surum: (\S+)", oku(self.kok, SC), re.M).group(1)
        for _ in range(2):
            kod, cikti = betik(self.kok, "scorecard.py", "--yaz", "T-999")
            self.assertIn(kod, (0, 1), cikti)
        s = oku(self.kok, SC)
        self.assertEqual(len(re.findall(rf"^\| {hafta} \|", s, re.M)), 1)
        a, b = surum_once.split(".")
        self.assertRegex(s, rf"(?m)^surum: {a}\.{int(b) + 2}$")
        kod, cikti = betik(self.kok, "kontrol.py", "--kisa")
        self.assertEqual(kod, 0, cikti)

    def test_tavan_asan_oturum_hedef_disi(self):
        m = oku(self.kok, "00-sistem/MALIYET.csv").rstrip("\n")
        bugun = __import__("datetime").date.today().isoformat()
        yaz(self.kok, "00-sistem/MALIYET.csv", m + f"\ntest-oturum,{bugun} 10:00,1,0,0,0,0,claude-opus-5-5,other,99.0\n")
        s5 = self.json()["gostergeler"]["S5"]
        self.assertFalse(s5["hedefte"])
        self.assertIn("test-oturum", s5["not"])

    def test_kayitsiz_kapanis_s1_dusurur(self):
        s = oku(self.kok, "00-sistem/TALIMATLAR.md")
        bugun = __import__("datetime").date.today().isoformat()
        yaz(self.kok, "00-sistem/TALIMATLAR.md",
            s + f"\n## T-997 — deneme\n- Tarih: {bugun}\n- Durum: kapali\n- Kapanış notu: deneme\n")
        s1 = self.json()["gostergeler"]["S1"]
        self.assertFalse(s1["hedefte"])
        self.assertIn("T-997", s1["not"])


if __name__ == "__main__":
    unittest.main()
