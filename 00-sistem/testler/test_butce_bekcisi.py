"""butce-bekcisi (UserPromptSubmit) regresyon testleri (T-028). Depo kopyasında, sahte transcript ile koşar.

Opus 5.5 çıkış fiyatı 20 USD / milyon token (MODEL-POLITIKASI): 50.000 çıkış tokenı = 1 USD. Tavan 5 USD.
"""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import hook, kopya_olustur, oku, yaz  # noqa: E402

HOOK = "butce-bekcisi.py"


class ButceBekcisi(unittest.TestCase):
    def setUp(self):
        self.kok, self.temizle = kopya_olustur()
        self.transcript = os.path.join(self.kok, "00-sistem", ".kosu", "sahte.jsonl")
        self.mesaj = 0
        yaz(self.kok, "00-sistem/.kosu/sahte.jsonl", "")
        self.taban = 0
        self.taban = self.hata_satiri_sayisi()  # gerçek GUNLUK'te önceden yazılmış tavan satırları sayılmaz

    def tearDown(self):
        self.temizle()

    def harca(self, usd):
        self.mesaj += 1
        satir = {"type": "assistant", "message": {"id": f"m{self.mesaj}", "model": "claude-opus-5-5",
                                                  "usage": {"input_tokens": 0, "output_tokens": int(usd * 50_000)}}}
        with open(self.transcript, "a", encoding="utf-8") as f:
            f.write(json.dumps(satir) + "\n")

    def istem(self, sid="s1"):
        kod, veri, ham = hook(self.kok, HOOK, {"hook_event_name": "UserPromptSubmit", "session_id": sid,
                                              "transcript_path": self.transcript, "prompt": "devam"})
        self.assertEqual(kod, 0, ham)
        return ((veri or {}).get("hookSpecificOutput") or {}).get("additionalContext")

    def hata_satiri_sayisi(self):
        return sum("bütçe tavanı aşıldı" in s for s in oku(self.kok, "00-sistem/GUNLUK.md").splitlines()) - self.taban

    def test_tavan_altinda_sessiz(self):
        self.harca(3.0)
        self.assertIsNone(self.istem())

    def test_yuzde_seksende_bir_kez_uyarir(self):
        self.harca(4.5)
        self.assertIn("%80", self.istem())
        self.assertIsNone(self.istem())  # aynı eşik ikinci kez bildirilmez
        self.assertEqual(self.hata_satiri_sayisi(), 0)

    def test_tavan_ve_katlari_uyarir_ve_kaydeder(self):
        self.harca(6.0)
        self.assertIn("tavanı aşıldı", self.istem())
        self.assertIsNone(self.istem())
        self.harca(5.0)  # toplam 11 USD → 2×
        self.assertIn("2×", self.istem())
        self.assertEqual(self.hata_satiri_sayisi(), 2)

    def test_oturumlar_ayri_izlenir(self):
        self.harca(6.0)
        self.assertIsNotNone(self.istem("s1"))
        self.assertIsNotNone(self.istem("s2"))

    def test_tavan_politikadan_okunur(self):
        yol = "30-devlet/normlar/MODEL-POLITIKASI.md"
        yaz(self.kok, yol, oku(self.kok, yol).replace("oturum: 5 USD", "oturum: 20 USD", 1))
        self.harca(6.0)
        self.assertIsNone(self.istem())

    def test_bozuk_girdide_sessiz_gecer(self):
        kod, veri, _ = hook(self.kok, HOOK, {"session_id": "s1", "transcript_path": "/yok/yok.jsonl"})
        self.assertEqual(kod, 0)
        self.assertIsNone(veri)


if __name__ == "__main__":
    unittest.main()
