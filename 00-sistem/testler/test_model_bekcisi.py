"""model-bekcisi (PreModelSwitch/PostModelSwitch) regresyon testleri (T-040). Depo kopyasında koşar."""
import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import hook, kopya_olustur, oku  # noqa: E402

HOOK = "model-bekcisi.py"


class ModelBekcisi(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()

    def tearDown(self):
        self.temizle()

    def gecis(self, olay, hedef, **ek):
        return hook(self.kok, HOOK, {"hook_event_name": olay, "from_model": "claude-sonnet-5-5", "to_model": hedef, **ek})

    def karar(self, hedef):
        _, veri, _ = self.gecis("PreModelSwitch", hedef)
        return ((veri or {}).get("hookSpecificOutput") or {}).get("permissionDecision")

    def test_pahali_model_sorulur(self):
        for m in ("claude-fable-5-1", "claude-opus-5-5", {"id": "claude-opus-5-5", "display_name": "Opus 5.5"},
                  {"slug": "claude-fable-5-1"}):
            with self.subTest(m=m):
                self.assertEqual(self.karar(m), "ask")

    def test_ucuz_model_serbest(self):
        for m in ("claude-sonnet-5-5", "claude-haiku-4-5-20251001", ""):
            with self.subTest(m=m):
                self.assertIsNone(self.karar(m))

    def test_gunluk_tek_satir(self):
        once = len(oku(self.kok, "00-sistem/GUNLUK.md").splitlines())
        self.gecis("PreModelSwitch", "claude-opus-5-5")
        self.gecis("PostModelSwitch", "claude-opus-5-5", reason="user_requested\nikinci")
        satirlar = oku(self.kok, "00-sistem/GUNLUK.md").splitlines()
        self.assertEqual(len(satirlar), once + 2)
        for s in satirlar[-2:]:
            self.assertRegex(s, r"^\d{4}-\d\d-\d\d \d\d:\d\d \[ayar\] model — ")
        self.assertIn("user_requested ikinci", satirlar[-1])

    def test_bozuk_girdi_sessiz(self):
        import subprocess
        r = subprocess.run([sys.executable, os.path.join(self.kok, ".claude", "hooks", HOOK)], input="bozuk",
                           capture_output=True, text=True, env=dict(os.environ, CLAUDE_PROJECT_DIR=self.kok))
        self.assertEqual((r.returncode, r.stdout), (0, ""))

    def test_ayar_denetimi_hook_kaydini_zorunlu_tutar(self):
        self.assertTrue(re.search(r'"PreModelSwitch"', oku(self.kok, ".claude/settings.json")))


if __name__ == "__main__":
    unittest.main()
