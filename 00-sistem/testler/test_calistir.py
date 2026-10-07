"""calistir.sh (gözetimsiz koşu) güvenlik bayrakları (T-048). Yalnız okur."""
import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import KOK  # noqa: E402


class Calistir(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(KOK, "00-sistem", "scripts", "calistir.sh"), encoding="utf-8") as f:
            self.metin = f.read()

    def test_workflow_kapali(self):
        self.assertRegex(self.metin, r"--disallowedTools\s+Workflow\b")

    def test_tavanlar_ve_soru_yok(self):
        for bayrak in ("--max-turns", "--max-budget-usd", "--permission-prompts none"):
            self.assertIn(bayrak, self.metin)
        self.assertNotIn("bypassPermissions", self.metin)

    def test_disallowed_listesi_sonraki_bayrakla_biter(self):
        # --disallowedTools çok değerli: hemen ardından bir -- bayrağı gelmeli ki istem metni araç adı sanılmasın
        self.assertRegex(self.metin, r"--disallowedTools Workflow \\\n\s+--")


if __name__ == "__main__":
    unittest.main()
