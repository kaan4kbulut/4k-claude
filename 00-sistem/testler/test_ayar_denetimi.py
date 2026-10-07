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

    # T-039 / K-006: eklenti, workflow, managed settings
    def baslat(self, yonetilen=None):
        yol = os.path.join(self.ev, "managed.json" if yonetilen is not None else "olmayan.json")
        if yonetilen is not None:
            yaz(self.ev, "managed.json", json.dumps(yonetilen))
        eski = os.environ.get("FOURK_MANAGED")
        os.environ["FOURK_MANAGED"] = yol
        try:
            _, veri, _ = hook(self.kok, HOOK, {"hook_event_name": "SessionStart", "source": "startup"}, ev=self.ev)
        finally:
            os.environ.pop("FOURK_MANAGED") if eski is None else os.environ.__setitem__("FOURK_MANAGED", eski)
        return ((veri or {}).get("hookSpecificOutput") or {}).get("additionalContext") or ""

    IYI = {"pluginConfigs": {"cc-plugin-sec-default@builtin": {"options": {"allowManagedModsOnly": True}}}}

    def test_onaysiz_eklenti_engellenir(self):
        yaz(self.ev, ".claude/settings.json", json.dumps({"enabledPlugins": {"kotu-mod@pazar": True}}))
        self.assertTrue(self.degis("user_settings", os.path.join(self.ev, ".claude/settings.json")))

    def test_tabandaki_eklenti_ve_kapatma_gecer(self):
        yaz(self.ev, ".claude/settings.json", json.dumps(
            {"enabledPlugins": {"pyright-lsp@claude-plugins-official": True, "baska@pazar": False}}))
        self.assertFalse(self.degis("user_settings", os.path.join(self.ev, ".claude/settings.json")))

    def test_marketplace_ve_plugin_config_engellenir(self):
        for alan, deger in (("extraKnownMarketplaces", {"pazar": {"source": {"source": "github", "repo": "x/y"}}}),
                            ("pluginConfigs", {"x@y": {"options": {}}}), ("prependPlugins", ["x"])):
            with self.subTest(alan=alan):
                a = dict(self.ayar)
                a[alan] = deger
                self.kaydet(a)
                self.assertTrue(self.degis())

    def test_imzali_eklenti_gecer(self):
        yaz(self.kok, "30-devlet/kapilar/KP-999-deneme.md", "---\nsonuc: go\n---\n")
        yaz(self.kok, ".claude/ayar-imzasi.json", json.dumps({"istisnalar": [
            {"degismez": "eklenti:enabledPlugins:yeni@pazar", "kapi": "30-devlet/kapilar/KP-999-deneme.md"}]}))
        yaz(self.ev, ".claude/settings.json", json.dumps({"enabledPlugins": {"yeni@pazar": True}}))
        self.assertFalse(self.degis("user_settings", os.path.join(self.ev, ".claude/settings.json")))

    def test_oturum_basi_managed_ve_workflow(self):
        self.assertEqual(self.baslat(self.IYI), "")
        self.assertIn("managed settings yok", self.baslat())
        self.assertIn("allowManagedModsOnly", self.baslat({"pluginConfigs": {}}))
        kotu = json.loads(json.dumps(self.IYI))
        kotu["pluginConfigs"]["cc-plugin-sec-default@builtin"]["options"]["allowModsToOverrideDenyRules"] = True
        self.assertIn("deny kuralını aşmasına", self.baslat(kotu))
        yaz(self.kok, ".claude/workflows/deneme.js", "export const meta = {}\n")
        self.assertIn("onaysız workflow", self.baslat(self.IYI))

    def test_env_ile_hook_yolu_yonlendirme_engellenir(self):
        for anahtar in ("FOURK_MANAGED", "FOURK_KASA"):
            with self.subTest(anahtar=anahtar):
                a = json.loads(json.dumps(self.ayar))
                a.setdefault("env", {})[anahtar] = "/tmp/sahte.json"
                self.kaydet(a)
                self.assertTrue(self.degis())

    def test_dizin_ayar_dosyasi_engellenir(self):
        os.makedirs(os.path.join(self.ev, ".claude", "settings.json"))
        self.assertTrue(self.degis("user_settings", os.path.join(self.ev, ".claude/settings.json")))

    def test_zararsiz_degisiklik_gecer_ve_kaydedilir(self):
        self.ayar["permissions"]["allow"].append("Bash(python3 00-sistem/scripts/yeni.py*)")
        self.kaydet(self.ayar)
        self.assertFalse(self.degis())


if __name__ == "__main__":
    unittest.main()
