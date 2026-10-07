"""kapanis-kaydi hook'u regresyon testleri (T-036). Depo kopyasında koşar."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import hook, kopya_olustur, oku  # noqa: E402

GUNLUK = "00-sistem/GUNLUK.md"


class KapanisKaydi(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()

    def tearDown(self):
        self.temizle()

    def test_cok_satirli_hata_tek_satir(self):
        once = oku(self.kok, GUNLUK).splitlines()
        hook(self.kok, "kapanis-kaydi.py", {"hook_event_name": "PostToolUseFailure", "session_id": "s1",
                                             "tool_name": "Bash", "error": "Exit code 1\nYour disk quota is full\n\nsatır 3"})
        sonra = oku(self.kok, GUNLUK).splitlines()
        self.assertEqual(len(sonra), len(once) + 1)
        self.assertRegex(sonra[-1], r"^\d{4}-\d\d-\d\d \d\d:\d\d \[hata\] Bash — Exit code 1 · Your disk quota is full · satır 3$")


if __name__ == "__main__":
    unittest.main()
