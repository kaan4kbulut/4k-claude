"""test-kurulum.py regresyon testleri (T-035). Depo kopyasını git deposu yapıp ondan test kopyası kurar."""
import json
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import kopya_olustur, oku, yaz  # noqa: E402

GIT = ["git", "-c", "user.name=test", "-c", "user.email=test@example.invalid", "-c", "commit.gpgsign=false"]


@unittest.skipIf(os.environ.get("FOURK_DOGRULAMA_ICINDE"), "test-kurulum doğrulamasının içinde: iç içe kurulum olmaz")
class TestKurulum(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()
        self.yer = os.path.join(os.path.dirname(self.kok), "test-yeri")
        self.kasa = os.path.join(self.yer, "kasa")
        for k in (["init", "-q", "-b", "master"], ["add", "-A"], ["commit", "-qm", "ilk"]):
            subprocess.run(GIT + k, cwd=self.kok, check=True, capture_output=True)

    def tearDown(self):
        self.temizle()

    def calistir(self, *arg, ek=None):
        env = dict(os.environ, FOURK_TEST_KOK=self.yer, FOURK_TEST_DOGRULAMA="kisa", **(ek or {}))
        r = subprocess.run([sys.executable, os.path.join(self.kok, "00-sistem", "scripts", "test-kurulum.py"), *arg],
                           capture_output=True, text=True, env=env, timeout=300)
        return r.returncode, r.stdout + r.stderr

    def commit(self, yol, metin, mesaj):
        yaz(self.kok, yol, metin)
        subprocess.run(GIT + ["add", "-A"], cwd=self.kok, check=True, capture_output=True)
        subprocess.run(GIT + ["commit", "-qm", mesaj], cwd=self.kok, check=True, capture_output=True)

    def sha(self, kok):
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=kok, capture_output=True, text=True).stdout.strip()

    def test_kurulum_izole_ve_isaretli(self):
        kod, cikti = self.calistir("guncelle")
        self.assertEqual(kod, 0, cikti)
        self.assertTrue(os.path.isfile(os.path.join(self.kasa, ".test-kopyasi")))
        uzak = subprocess.run(["git", "remote"], cwd=self.kasa, capture_output=True, text=True).stdout.strip()
        self.assertEqual(uzak, "")  # gerçek depoya push edemez
        self.assertEqual(json.loads(oku(self.yer, "kurulum.json"))["commit"], self.sha(self.kok))
        durum = subprocess.run(["git", "status", "--porcelain"], cwd=self.kasa, capture_output=True, text=True).stdout
        self.assertEqual(durum, "")  # işaret dosyası git'e görünmez

    def test_dogrulamayi_gecemeyen_surum_gecmez(self):
        self.calistir("guncelle")
        once = self.sha(self.kasa)
        self.commit("40-ic-ses/bozuk.md", "frontmatter yok\n", "bozuk")
        kod, cikti = self.calistir("guncelle")
        self.assertEqual(kod, 1, cikti)
        self.assertEqual(self.sha(self.kasa), once)
        self.assertTrue(any(a.startswith("basarisiz-") for a in os.listdir(os.path.join(self.yer, "surumler"))))

    def test_guncelle_ve_geri(self):
        self.calistir("guncelle")
        ilk = self.sha(self.kasa)
        il = oku(self.kok, "00-sistem/ILERLEME.md")
        self.commit("00-sistem/ILERLEME.md", il + "\n", "ikinci")
        kod, cikti = self.calistir("guncelle")
        self.assertEqual(kod, 0, cikti)
        self.assertNotEqual(self.sha(self.kasa), ilk)
        kod, cikti = self.calistir("geri")
        self.assertEqual(kod, 0, cikti)
        self.assertEqual(self.sha(self.kasa), ilk)
        self.assertEqual(len(os.listdir(os.path.join(self.yer, "surumler"))), 1)  # yerinden çıkan silinmedi

    def test_uzak_bag_kalirsa_gecmez(self):
        # ortamdan gelen git ayarı kaldırılamayan bir uzak depo bağı yaratır: kopya geçmemeli
        kod, cikti = self.calistir("guncelle", ek={"GIT_CONFIG_COUNT": "1", "GIT_CONFIG_KEY_0": "remote.gercek.url",
                                                    "GIT_CONFIG_VALUE_0": self.kok})
        self.assertEqual(kod, 1, cikti)
        self.assertIn("uzak depo bağı", cikti)
        self.assertFalse(os.path.isdir(self.kasa))

    def test_pano_test_isareti(self):
        kod, cikti = self.calistir("pano", "--acma")
        self.assertEqual(kod, 0, cikti)
        self.assertIn("TEST", oku(self.kasa, "00-sistem/.kosu/pano/pano.html"))


if __name__ == "__main__":
    unittest.main()
