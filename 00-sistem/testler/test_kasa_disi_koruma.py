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
                  f"cd {KOK} && python3 00-sistem/scripts/gunluk.py yeni T-1 x",
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

    def test_adi_4k_claude_gecen_dis_yollar_serbest(self):
        # T-036: 7 Ekim taramasında yaşanan yanlış pozitifler; hedef gerçek depo değil
        is_klasoru = os.path.join(DIS, "Work", "isler", "2026-10-07-4k-claude-devam")
        for k in (f"cp /tmp/istem.txt {is_klasoru}/",
                  f"mkdir -p {DIS}/Work/arsiv/pano && mv {DIS}/Downloads/4k-claude-pano-tasarim.zip {DIS}/Work/arsiv/pano/",
                  f"unzip -o {DIS}/Downloads/4k-claude-pano-tasarim.zip -d /tmp/x",
                  "git ls-remote https://github.com/kaan4kbulut/4k-claude.git",
                  f'grep -rn -e "Downloads/4k-claude" {DIS}/.config > /tmp/sonuc.txt'):
            with self.subTest(komut=k):
                self.assertEqual(bash(k), "izin")

    def test_tirnak_ici_boru_ayirici_degil(self):
        self.assertEqual(bash(f'grep -rn "sudo\\|rm -rf" {KOK}/.claude/hooks'), "izin")
        self.assertEqual(bash(f"grep 'a|b' {KOK}/CLAUDE.md | wc -l"), "izin")
        self.assertEqual(bash(f'echo "x|y" | tee {KOK}/00-sistem/x.md'), "deny")

    def test_yeni_okur_komutlar(self):
        for k in (f"unzip -l {KOK}/x.zip", f"sha256sum {KOK}/CLAUDE.md", f"md5sum {KOK}/CLAUDE.md",
                  f"cmp {KOK}/CLAUDE.md {KOK}/AGENTS.md", f"git -C {KOK} ls-remote origin",
                  f"cd {KOK} && sha256sum -c /tmp/once.sha | grep -c OK"):
            with self.subTest(komut=k):
                self.assertEqual(bash(k), "izin")
        self.assertEqual(bash(f"unzip -o /tmp/x.zip -d {KOK}/01-gelen"), "deny")

    def test_zincir_ve_dongu(self):
        self.assertEqual(bash(f"for f in {KOK}/CLAUDE.md {KOK}/AGENTS.md; do wc -l \"$f\"; done"), "izin")
        self.assertEqual(bash(f"for f in a b; do touch {KOK}/$f; done"), "deny")
        self.assertEqual(bash(f"ls {KOK} && cp /tmp/x {KOK}/x"), "deny")
        self.assertEqual(bash(f"cd {KOK} && ls && cd /tmp && touch y"), "izin")  # yazım depo dışında
        self.assertEqual(bash(f"cd /tmp && touch y && cd {KOK} && touch z"), "deny")
        self.assertEqual(bash("touch $HOME/x", cwd=KOK), "deny")  # dizin depoda

    def test_gomulu_komut_reddedilir(self):
        # T-036 denetci: eski sürüm ham metni tarıyordu; tırnak içi gömülü komutlar yeni ayrıştırıcıda kaçmasın
        for k in (f"python3 -c \"open('{KOK}/x','w')\"",
                  f"bash -c 'touch {KOK}/x'",
                  f'sh -c "echo a > {KOK}/x"',
                  f"awk 'BEGIN{{system(\"touch {KOK}/x\")}}'",
                  f'cd "$(echo {KOK})" && touch x'):
            with self.subTest(komut=k):
                self.assertEqual(bash(k), "deny")
        self.assertEqual(bash(f"grep -c 'x' {KOK}-test/CLAUDE.md > /tmp/x"), "izin")  # benzer ad depo değil
        rel = os.path.relpath(KOK, DIS)
        for k in (f"python3 -c \"open('{rel}/x','w')\"",          # göreli, tırnak içi
                  f"sh -c 'cd {rel} && touch x'",
                  f"D={rel}; cd $D; touch x",                      # komut içi değişken
                  f"export D={KOK} && touch $D/x",
                  f"touch {os.path.dirname(KOK)}/{os.path.basename(KOK)[:4]}*/x",  # glob
                  f"echo 'touch {KOK}/a' | bash",                    # boru ile yorumlayıcıya betik
                  f"echo 'cd {os.path.dirname(KOK)}; touch {os.path.basename(KOK)}/a' | sh"):
            with self.subTest(komut=k):
                self.assertEqual(bash(k), "deny")

    def test_degisken_ve_esittir_ile_yol(self):
        rel = os.path.relpath(KOK, DIS)
        self.assertEqual(bash(f"touch $HOME/{rel}/x", ), "deny" if os.path.expanduser("~") == DIS else "izin")
        self.assertEqual(bash(f"python3 x.py --cikti={KOK}/x.md"), "deny")

    def test_bozuk_girdi_sessiz(self):
        env = dict(os.environ, CLAUDE_PROJECT_DIR=DIS, FOURK_KASA=KOK)
        r = subprocess.run([sys.executable, HOOK], input="bozuk", capture_output=True, text=True, env=env, timeout=30)
        self.assertEqual((r.returncode, r.stdout.strip()), (0, ""))


if __name__ == "__main__":
    unittest.main()
