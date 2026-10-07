"""kasa-disi-koruma (kullanıcı düzeyi PreToolUse) regresyon testleri (T-031). Hook yalnız okur."""
import json
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import KOK  # noqa: E402

HOOK = os.path.join(KOK, ".claude", "hooks", "kasa-disi-koruma.py")
DIS = os.path.dirname(os.path.dirname(KOK))  # ör. ev dizini: oturumun klasör dışında açıldığı yer


def karar(arac, ti, proje=DIS, cwd=DIS):
    env = dict(os.environ, CLAUDE_PROJECT_DIR=proje, FOURK_KASA=KOK)
    r = subprocess.run([sys.executable, HOOK], input=json.dumps({"tool_name": arac, "tool_input": ti, "cwd": cwd}),
                       capture_output=True, text=True, env=env, timeout=30)
    if r.returncode != 0:
        return f"hata {r.returncode}"
    return json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"] if r.stdout.strip() else "izin"


def bash(komut, **kw):
    return karar("Bash", {"command": komut}, **kw)


class KlasorIcinde(unittest.TestCase):
    def test_proje_kasada_ise_sessiz(self):
        self.assertEqual(karar("Write", {"file_path": os.path.join(KOK, "00-sistem/x.md")}, proje=KOK), "izin")
        self.assertEqual(bash(f"cd {KOK} && git commit -m x", proje=KOK, cwd=KOK), "izin")


class KlasorDisinda(unittest.TestCase):
    def test_kasaya_yazim_reddedilir(self):
        for arac in ("Write", "Edit", "MultiEdit"):
            with self.subTest(arac=arac):
                self.assertEqual(karar(arac, {"file_path": os.path.join(KOK, "40-ic-ses/x.md")}), "deny")
        self.assertEqual(karar("Write", {"file_path": "x.md"}, cwd=KOK), "deny")

    def test_baska_projeye_yazim_serbest(self):
        self.assertEqual(karar("Write", {"file_path": os.path.join(DIS, "baska-proje/x.md")}), "izin")
        self.assertEqual(bash("rm -rf /tmp/baska-proje-deneme"), "izin")  # bu hook'un işi değil

    def test_yazan_bash_reddedilir(self):
        for k in (f"cd {KOK} && git commit -m x",
                  f"echo x >> {KOK}/00-sistem/GUNLUK.md",
                  "cd ~/Downloads/4k-claude && python3 00-sistem/scripts/gunluk.py yeni T-1 x",
                  f"sed -i s/a/b/ {KOK}/CLAUDE.md",
                  f"git -C {KOK} push origin master",
                  f"find {KOK} -name x -delete",
                  f"cat > {KOK}/01-gelen/x.md <<'EOF'\nx\nEOF",
                  f"python3 {KOK}/00-sistem/scripts/scorecard.py --yaz T-031"):
            with self.subTest(komut=k):
                self.assertEqual(bash(k), "deny")

    def test_cwd_kasadaysa_yazim_reddedilir(self):
        self.assertEqual(bash("touch yeni.md", cwd=KOK), "deny")

    def test_okumalar_serbest(self):
        for k in (f"cat {KOK}/CLAUDE.md",
                  f"cd {KOK} && git status --short && git log --oneline | head -5",
                  f"git -C {KOK} diff --stat",
                  f"grep -rn sudo {KOK}/.claude/hooks | head",
                  f"cd {KOK} && python3 00-sistem/scripts/kontrol.py --kisa 2>&1 | tail -3",
                  f"cd {KOK} && python3 00-sistem/scripts/harita.py --dogrula",
                  f"sed -n 1,20p {KOK}/00-sistem/ILERLEME.md",
                  f"ls -la {KOK} 2>/dev/null"):
            with self.subTest(komut=k):
                self.assertEqual(bash(k), "izin")

    def test_bozuk_girdi_sessiz(self):
        env = dict(os.environ, CLAUDE_PROJECT_DIR=DIS, FOURK_KASA=KOK)
        r = subprocess.run([sys.executable, HOOK], input="bozuk", capture_output=True, text=True, env=env, timeout=30)
        self.assertEqual((r.returncode, r.stdout.strip()), (0, ""))


if __name__ == "__main__":
    unittest.main()
