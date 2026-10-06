#!/usr/bin/env python3
"""PreToolUse hook — yikici-koruma (Bash | Edit | Write | MultiEdit | NotebookEdit).

Kural değil engel: Claude'un tercihine bırakılmaz.
  - Edit/Write/MultiEdit/NotebookEdit: hedef (sembolik bağlar çözülerek) proje kökü altında ve izinli köklerden birinde
    olmalı. İzinli kökler: CLAUDE.md, AGENTS.md, README.md, .gitignore, .claude/, 00-sistem/, 01-gelen/, 10-insan/,
    20-sirket/, 30-devlet/, 40-ic-ses/, 90-arsiv/. ANAYASA.md her zaman reddedilir (yalnız insan düzenler).
  - Bash, komut konumunda (satır başı, ; && || | $( ` sonrası, xargs/env/exec/nohup ardından):
      reddet: rm -r/-R/--recursive, find -delete / -exec rm, shutil.rmtree / os.remove / unlink betikleri,
              git reset --hard, git push --force / -f / +refspec, git clean -f, git checkout -- ., DROP/TRUNCATE,
              chmod 777, curl|sh, sudo, mkfs, dd if=, ANAYASA.md'ye ya da 30-devlet/normlar'a kabukla yazma
              (> >> tee sed -i perl -i cp mv truncate), proje dışına yönlendirme (/dev/null, /dev/stdout, /dev/stderr hariç).
      sor:    tek dosya rm (özyinelemesiz) — sahibi onaylar; tercih edilen yol arşive taşımaktır (90-arsiv).
  - Yanlış pozitif önleme: git commit mesajı (-m/--message) ve cat/tee/git'e verilen heredoc gövdesi veri sayılır,
    taranmaz; grep/rg'nin arama deseni de komut değildir (sudo vb. yalnız komut konumunda aranır).
Bash eşleşmesi settings.json'da metinseldir ("git -C x push" kaçar); bu hook tam komutu ayrıştırır.
Metin eşleştirmesi bir taban çizgisidir, sandbox'ın yerini tutmaz (bkz. SISTEM.md kurulum notları).
Çıktı: permissionDecision deny|ask + neden. İzinliyse sessizce 0.
"""
import json
import os
import re
import sys

IZINLI_KOKLER = (
    "CLAUDE.md", "AGENTS.md", "README.md", ".gitignore",
    ".claude", "00-sistem", "01-gelen", "10-insan", "20-sirket", "30-devlet", "40-ic-ses", "90-arsiv",
)

# Komut konumu: satır başı ya da bir ayraç/sarmalayıcıdan sonra.
KK = r"(?:^|[;&|(`\n]|\$\()\s*(?:(?:xargs|env|exec|nohup|time|command|builtin)\s+(?:-\S+\s+)*)*"

REDDET = [
    (KK + r"rm\s+(?:\S+\s+)*?(-[a-zA-Z]*[rR][a-zA-Z]*|--recursive)\b", "rm -r / rm -rf yasak; arşive taşı (90-arsiv), silme"),
    (r"\bfind\b[^;&|]*\s(-delete\b|-exec(dir)?\s+rm\b)", "find -delete / -exec rm yasak; arşive taşı"),
    (r"\b(shutil\.rmtree|os\.remove|os\.unlink|os\.rmdir|\.unlink\(|\.rmdir\(|fs\.rm(Sync)?\(|fs\.unlink)", "betikle silme yasak; arşive taşı"),
    (KK + r"git\s+(?:-[cC]\s+\S+\s+)*reset\s+--hard", "git reset --hard yasak; commit'ler geri alma noktasıdır"),
    (KK + r"git\s+(?:-[cC]\s+\S+\s+)*push\b[^;&|]*(--force|--force-with-lease|\s-[a-zA-Z]*f\b|\s\+\S+)", "force push yasak (+refspec dahil)"),
    (KK + r"git\s+(?:-[cC]\s+\S+\s+)*clean\s+-[a-zA-Z]*f", "git clean -f yasak"),
    (KK + r"git\s+(?:-[cC]\s+\S+\s+)*checkout\s+(\S+\s+)?--\s+\.", "git checkout -- . yasak (tüm değişiklikleri siler)"),
    (r"\b(DROP\s+(TABLE|DATABASE|SCHEMA)|TRUNCATE\s+TABLE)\b", "DROP/TRUNCATE yasak"),
    (KK + r"chmod\s+(-R\s+)?0?777\b", "chmod 777 yasak"),
    (r"\b(curl|wget)\b[^|;&]*\|\s*(sudo\s+)?(sh|bash|zsh|fish|python3?)\b", "indir-ve-çalıştır yasak"),
    (KK + r"sudo\b", "sudo yasak"),
    (KK + r"(mkfs(\.\w+)?|dd\s+if=)", "disk işlemleri yasak"),
]

SOR = [
    (KK + r"rm\s+(?!-)\S", "tek dosya silme sahibinin onayını ister; tercih: 90-arsiv'e taşı (git mv)"),
    (KK + r"rm\s+-[a-zA-Z]*f[a-zA-Z]*\s", "rm -f sahibinin onayını ister; tercih: 90-arsiv'e taşı"),
]

KORUNAN = r"(ANAYASA\.md|30-devlet/normlar/)"
YAZAN = r"(>{1,2}|\btee\b|\bsed\s+(-[a-zA-Z]*\s+)*-[a-zA-Z]*i|\bperl\s+(-\S+\s+)*-[a-zA-Z]*i|\bcp\b|\bmv\b|\btruncate\b|\binstall\b|open\([^)]*['\"][wa])"


def karar(tur, neden):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": tur,
            "permissionDecisionReason": f"yikici-koruma: {neden}",
        }
    }, ensure_ascii=False))
    sys.exit(0)


def veri_kisimlarini_cikar(komut):
    """Commit mesajlarını, cat/tee/git heredoc gövdelerini ve grep/rg desenlerini çıkarır (veri, komut değil)."""
    k = re.sub(r"(\bgit\b[^;&|\n]*\bcommit\b[^;&|\n]*?)(-m|--message)(=|\s+)(\"(?:[^\"\\]|\\.)*\"|'[^']*'|\$\(cat\s+<<.*?\))",
               r"\1\2 MESAJ", komut, flags=re.S)
    # heredoc: yalnız cat/tee/git'e verilen gövde veridir; bash/sh/python'a verilen gövde komuttur, kalır
    def heredoc(m):
        return m.group(1) + " HEREDOC\n" if re.search(r"\b(cat|tee|git)\b", m.group(1)) else m.group(0)
    k = re.sub(r"([^\n]*<<-?\s*['\"]?(\w+)['\"]?[^\n]*)\n.*?\n\s*\2\s*(?=\n|$)", heredoc, k, flags=re.S)
    k = re.sub(r"(\b(?:grep|rg|egrep|fgrep)\b(?:\s+-\S+)*)\s+(\"[^\"]*\"|'[^']*'|\S+)", r"\1 DESEN", k)
    return k


def yol_izinli(kok, hedef):
    if not hedef:
        return True, ""
    mutlak = os.path.realpath(hedef if os.path.isabs(hedef) else os.path.join(kok, hedef))
    kok_m = os.path.realpath(kok)
    if not (mutlak == kok_m or mutlak.startswith(kok_m + os.sep)):
        return False, f"proje kökü dışına yazma: {hedef}"
    goreli = os.path.relpath(mutlak, kok_m)
    if goreli.replace(os.sep, "/") == "30-devlet/normlar/ANAYASA.md":
        return False, "ANAYASA.md yalnız insan tarafından düzenlenir (imza matrisi, seviye 1)"
    ilk = goreli.split(os.sep)[0]
    if goreli in IZINLI_KOKLER or ilk in IZINLI_KOKLER:
        return True, ""
    return False, f"izinli kök dışı yol: {goreli} (kat klasörleri, 00-sistem, 01-gelen, 90-arsiv, .claude)"


def main():
    try:
        girdi = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    kok = os.environ.get("CLAUDE_PROJECT_DIR") or girdi.get("cwd") or os.getcwd()
    cwd = girdi.get("cwd") or kok
    arac = girdi.get("tool_name", "")
    ti = girdi.get("tool_input", {}) or {}

    if arac in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
        hedef = ti.get("file_path") or ti.get("notebook_path") or ti.get("path") or ""
        ok, neden = yol_izinli(kok, hedef)
        if not ok:
            karar("deny", neden)
        sys.exit(0)

    if arac != "Bash":
        sys.exit(0)

    komut = ti.get("command", "") or ""
    tarama = veri_kisimlarini_cikar(komut)
    kisa = komut[:160]
    for kalip, neden in REDDET:
        if re.search(kalip, tarama, re.I | re.M):
            karar("deny", f"{neden} — komut: {kisa}")
    if re.search(KORUNAN, tarama) and re.search(YAZAN, tarama):
        # okuma (cat, grep, git diff) serbest; aynı komutta yazan bir işlem varsa reddet
        for parca in re.split(r"[;&|\n]+", tarama):
            if re.search(KORUNAN, parca) and re.search(YAZAN, parca):
                karar("deny", f"ANAYASA ve normlar kabukla değiştirilmez; /degistir kullan (ANAYASA yalnız insan) — komut: {kisa}")
    for m in re.finditer(r"(?<![<>0-9&])>{1,2}\s*([^\s;&|<>()]+)", tarama):
        hedef = m.group(1).strip("'\"")
        if hedef.startswith("&") or hedef in ("/dev/null", "/dev/stdout", "/dev/stderr"):
            continue
        mutlak = os.path.realpath(os.path.expanduser(hedef) if hedef.startswith(("/", "~")) else os.path.join(cwd, hedef))
        if not (mutlak == os.path.realpath(kok) or mutlak.startswith(os.path.realpath(kok) + os.sep)):
            karar("deny", f"proje dışına yönlendirme: {hedef}")
    for kalip, neden in SOR:
        if re.search(kalip, tarama, re.I | re.M):
            karar("ask", f"{neden} — komut: {kisa}")
    sys.exit(0)


if __name__ == "__main__":
    main()
