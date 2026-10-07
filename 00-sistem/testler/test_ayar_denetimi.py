"""ayar-denetimi (ConfigChange) regresyon testleri (T-027).

Depo kopyasında ve boş bir sahte ev dizininde (HOME) koşar; gerçek ~/.claude/settings.json okunmaz.
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import hook, kopya_olustur, oku, yaz  # noqa: E402

HOOK = "ayar-denetimi.py"
AYAR = ".claude/settings.json"


class AyarDenetimi(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()
        self.ev = tempfile.mkdtemp(prefix="4k-ev-", dir=os.path.dirname(self.kok))
        self.ayar = json.loads(oku(self.kok, AYAR))

    def tearDown(self):
        self.temizle()

    def degis(self, kaynak="project_settings", dosya=AYAR):
        _, veri, _ = hook(self.kok, HOOK, {"hook_event_name": "ConfigChange", "source": kaynak,
                                          "file_path": os.path.join(self.kok, dosya)}, ev=self.ev)
        return (veri or {}).get("decision") == "block"

    def kaydet(self, ayar):
        yaz(self.kok, AYAR, json.dumps(ayar, ensure_ascii=False, indent=2))

    def test_mevcut_ayar_gecer(self):
        self.assertFalse(self.degis())

    def test_sandbox_kapatma_engellenir(self):
        self.ayar["sandbox"]["enabled"] = False
        self.kaydet(self.ayar)
        self.assertTrue(self.degis())

    def test_zorunlu_deny_silme_engellenir(self):
        self.ayar["permissions"]["deny"].remove("Bash(rm -rf *)")
        self.kaydet(self.ayar)
        self.assertTrue(self.degis())

    def test_koruma_hooku_silme_engellenir(self):
        del self.ayar["hooks"]["PreToolUse"]
        self.kaydet(self.ayar)
        self.assertTrue(self.degis())

    def test_genis_allow_engellenir(self):
        self.ayar["permissions"]["allow"].append("Bash")
        self.kaydet(self.ayar)
        self.assertTrue(self.degis())

    def test_kullanici_ayarinda_tum_hooklari_kapatma_engellenir(self):
        yaz(self.ev, ".claude/settings.json", json.dumps({"disableAllHooks": True}))
        self.assertTrue(self.degis("user_settings", os.path.join(self.ev, ".claude/settings.json")))

    def test_bozuk_json_engellenir(self):
        yaz(self.kok, AYAR, "{bozuk")
        self.assertTrue(self.degis())

    def test_zararsiz_degisiklik_gecer_ve_kaydedilir(self):
        self.ayar["permissions"]["allow"].append("Bash(python3 00-sistem/scripts/yeni.py*)")
        self.kaydet(self.ayar)
        self.assertFalse(self.degis())


if __name__ == "__main__":
    unittest.main()
