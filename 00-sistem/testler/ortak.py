"""Testlerin ortak yardımcıları (T-027).

Testler deponun geçici bir kopyasında koşar; gerçek depoya hiçbir şey yazmaz.
Kopyaya .git, .araclar, .venv, .obsidian ve 00-sistem/.kosu alınmaz.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HARIC = {".git", ".araclar", ".venv", ".obsidian", ".kosu", "__pycache__"}


def kopya_olustur():
    """Deponun geçici kopyası; (kok, temizle) döner."""
    tmp = tempfile.mkdtemp(prefix="4k-test-")
    hedef = os.path.join(tmp, "4k-claude")
    shutil.copytree(KOK, hedef, ignore=lambda d, adlar: [a for a in adlar if a in HARIC])
    return hedef, lambda: shutil.rmtree(tmp, ignore_errors=True)


def hook(kok, ad, girdi, ev=None):
    """Hook'u JSON girdiyle çalıştırır; (çıkış kodu, ayrıştırılmış çıktı ya da None, ham çıktı) döner."""
    env = dict(os.environ, CLAUDE_PROJECT_DIR=kok)
    if ev:
        env["HOME"] = ev
    r = subprocess.run([sys.executable, os.path.join(kok, ".claude", "hooks", ad)], input=json.dumps(girdi),
                       capture_output=True, text=True, cwd=kok, env=env, timeout=90)
    cikti = r.stdout.strip()
    try:
        veri = json.loads(cikti) if cikti else None
    except json.JSONDecodeError:
        veri = None
    return r.returncode, veri, cikti


def betik(kok, ad, *arg):
    """00-sistem/scripts/<ad> çalıştırır; (çıkış kodu, stdout+stderr) döner."""
    r = subprocess.run([sys.executable, os.path.join(kok, "00-sistem", "scripts", ad), *arg],
                       capture_output=True, text=True, cwd=kok, timeout=120)
    return r.returncode, r.stdout + r.stderr


def oku(kok, yol):
    with open(os.path.join(kok, yol), encoding="utf-8") as f:
        return f.read()


def yaz(kok, yol, metin):
    p = os.path.join(kok, yol)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(metin)
