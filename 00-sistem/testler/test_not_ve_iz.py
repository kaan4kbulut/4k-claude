"""T-049: not.py kapanış kaydı (16. denetim) ve dosya_izi sandbox yer tutucuları. Depo kopyasında koşar."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import betik, kopya_olustur  # noqa: E402


class NotVeIz(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()

    def tearDown(self):
        self.temizle()

    def test_not_py_sonrasi_kontrol_temiz(self):
        kod, cikti = betik(self.kok, "not.py", "gozlem", "deneme gözlemi", "test metni")
        self.assertEqual(kod, 0, cikti)
        kod, cikti = betik(self.kok, "kontrol.py", "--kisa")
        self.assertEqual(kod, 0, cikti)

    def test_yer_tutucu_izde_yok(self):
        os.symlink("/dev/null", os.path.join(self.kok, ".claude", "yer-tutucu.json"))
        sys.path.insert(0, os.path.join(self.kok, "00-sistem", "scripts"))
        import yscommon as yc
        self.assertNotIn(".claude/yer-tutucu.json", yc.dosya_izi(self.kok))


if __name__ == "__main__":
    unittest.main()
