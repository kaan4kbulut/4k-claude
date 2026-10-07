"""kontrol.py 17. denetim: kanban değişimi GUNLUK'süz (T-046). Depo kopyasını git deposu yapar."""
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import betik, kopya_olustur, oku, yaz  # noqa: E402

GIT = ["git", "-c", "user.name=test", "-c", "user.email=test@example.invalid", "-c", "commit.gpgsign=false"]
KART = "20-sirket/gorevler/G-001-yazici-pazar-arastirmasi.md"


class KanbanKaydi(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()
        for k in (["init", "-q"], ["add", "-A"], ["commit", "-qm", "ilk"]):
            subprocess.run(GIT + k, cwd=self.kok, check=True, capture_output=True)

    def tearDown(self):
        self.temizle()

    def kanban_degistir(self):
        s = oku(self.kok, KART)
        yaz(self.kok, KART, s.replace("\nkanban: tamam\n", "\nkanban: kontrol\n", 1))

    def test_kayitsiz_kanban_degisimi_hata(self):
        self.kanban_degistir()
        kod, cikti = betik(self.kok, "kontrol.py", "--kisa")
        self.assertEqual(kod, 1, cikti)
        self.assertIn("kanban değişti (tamam → kontrol)", cikti)

    def test_gunlukle_kaydedilen_degisim_gecer(self):
        self.kanban_degistir()
        kod, _ = betik(self.kok, "gunluk.py", "degisti", KART, "kanban tamam → kontrol (test)")
        self.assertEqual(kod, 0)
        kod, cikti = betik(self.kok, "kontrol.py", "--kisa")
        self.assertNotIn("kanban değişti", cikti)


if __name__ == "__main__":
    unittest.main()
