"""durus-kapisi (Stop) regresyon testleri (T-027). Depo kopyasında koşar: hook iz dosyası ve GUNLUK yazar."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import hook, kopya_olustur, oku, yaz  # noqa: E402

HOOK = "durus-kapisi.py"
KANIT = "Bitti.\n\n## Kanıt\n- `python3 00-sistem/scripts/kontrol.py --kisa` → 0 (Bütünlük tam)\n"


class DurusKapisi(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()
        self.sayac = 0
        # Gerçek depoda açık bir kapı (ASK.md) varsa kopya onu taşır ve hook serbest bırakır; testler kendi
        # durumunu kurar, ASK.md'yi isteyen test kendisi yazar (T-046: KP-004 açıkken 3 test düşmüştü).
        ask = os.path.join(self.kok, "00-sistem", "ASK.md")
        if os.path.exists(ask):
            os.replace(ask, ask + ".gercek")

    def tearDown(self):
        self.temizle()

    def dur(self, mesaj="Tamam.", aktif=False, sid="test-oturum"):
        _, veri, _ = hook(self.kok, HOOK, {"session_id": sid, "last_assistant_message": mesaj,
                                          "stop_hook_active": aktif, "cwd": self.kok})
        return (veri or {}).get("decision") == "block"

    def kod_degistir(self):
        self.sayac += 1
        yaz(self.kok, "00-sistem/scripts/test_yardimci.py", f"# deneme {self.sayac}\n")

    def test_ilk_durma_taban_alir(self):
        self.kod_degistir()
        self.assertFalse(self.dur())  # iz yok → taban, serbest
        self.assertTrue(os.path.exists(os.path.join(self.kok, "00-sistem", ".kosu", "durus-izi.json")))

    def test_degisiklik_yoksa_serbest(self):
        self.dur()
        self.assertFalse(self.dur())

    def test_kanitsiz_kod_degisikligi_engellenir(self):
        self.dur()
        self.kod_degistir()
        self.assertTrue(self.dur("Bitti, betiği düzelttim."))

    def test_kanitli_kod_degisikligi_serbest(self):
        self.dur()
        self.kod_degistir()
        self.assertFalse(self.dur(KANIT))

    def test_bos_kanit_basligi_yetmez(self):
        self.dur()
        self.kod_degistir()
        self.assertTrue(self.dur("Bitti.\n\n## Kanıt\nkontrol ettim, doğru.\n"))

    def test_yalniz_wiki_degisikligi_kontrol_temizse_serbest(self):
        self.dur()
        yol = "40-ic-ses/nerede-kaldik.md"
        yaz(self.kok, yol, oku(self.kok, yol) + "\n")
        self.assertFalse(self.dur("Not düştüm."))

    def test_kisa_ara_soru_serbest(self):
        self.dur()
        self.kod_degistir()
        self.assertFalse(self.dur("Hangi dosyayı kastettiniz?"))

    def test_ask_dosyasi_serbest_birakir(self):
        self.dur()
        self.kod_degistir()
        yaz(self.kok, "00-sistem/ASK.md", "# Tek soru\n")
        self.assertFalse(self.dur("Kapı açtım."))

    def test_dongu_korumasi_ikinci_denemede_birakir_ve_kaydeder(self):
        self.dur()
        self.kod_degistir()
        self.assertTrue(self.dur("Bitti."))
        self.assertFalse(self.dur("Bitti.", aktif=True))
        self.assertIn("kanıtsız durma", oku(self.kok, "00-sistem/GUNLUK.md").splitlines()[-1])


if __name__ == "__main__":
    unittest.main()
