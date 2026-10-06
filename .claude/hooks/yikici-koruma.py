#!/usr/bin/env python3
"""PreToolUse hook — yikici-koruma (Bash | Edit | Write | MultiEdit).

Kural değil engel: Claude'un tercihine bırakılmaz.
  - Edit/Write/MultiEdit: hedef dosya proje kökü altında ve izinli köklerden birinde olmalı.
    İzinli kökler: CLAUDE.md, AGENTS.md, README.md, .gitignore, .claude/, 00-sistem/, 01-gelen/, 10-insan/, 20-sirket/,
    30-devlet/, 40-ic-ses/, 90-arsiv/. ANAYASA.md her zaman reddedilir (yalnız insan düzenler).
  - Bash: yıkıcı kalıplar reddedilir: rm -rf / rm -r, git reset --hard, git push --force/-f, git clean -f, git checkout -- .,
    DROP TABLE/DATABASE, TRUNCATE, chmod 777, curl|sh / wget|sh, > veya >> ile 30-devlet/normlar altına yazma,
    kat klasörleri dışına yönlendirme (/etc, ~, /usr, /tmp hariç proje dışı yollar).
Bash eşleşmesi settings.json'da metinseldir ("git -C x push" kaçar); bu hook tam komutu ayrıştırır.
Çıktı: permissionDecision deny + neden. İzinliyse sessizce 0.
"""
import json
import os
import re
import sys

IZINLI_KOKLER = (
    "CLAUDE.md", "AGENTS.md", "README.md", ".gitignore",
    ".claude", "00-sistem", "01-gelen", "10-insan", "20-sirket", "30-devlet", "40-ic-ses", "90-arsiv",
)

YIKICI = [
    (r"\brm\s+(-[a-zA-Z]*r[a-zA-Z]*|--recursive)\b", "rm -r / rm -rf yasak; arşive taşı (90-arsiv), silme"),
    (r"\bgit\s+(-C\s+\S+\s+)?reset\s+--hard", "git reset --hard yasak; commit'ler geri alma noktasıdır"),
    (r"\bgit\s+(-C\s+\S+\s+)?push\s+.*(--force|-f\b|--force-with-lease)", "force push yasak"),
    (r"\bgit\s+(-C\s+\S+\s+)?clean\s+-[a-zA-Z]*f", "git clean -f yasak"),
    (r"\bgit\s+(-C\s+\S+\s+)?checkout\s+--\s+\.", "git checkout -- . yasak (tüm değişiklikleri siler)"),
    (r"\b(DROP\s+(TABLE|DATABASE|SCHEMA)|TRUNCATE\s+TABLE)\b", "DROP/TRUNCATE yasak"),
    (r"\bchmod\s+(-R\s+)?777\b", "chmod 777 yasak"),
    (r"\b(curl|wget)\b[^|]*\|\s*(sudo\s+)?(sh|bash|zsh|fish)\b", "indir-ve-çalıştır yasak"),
    (r">{1,2}\s*\S*30-devlet/normlar/", "normlar klasörüne kabuk yönlendirmesiyle yazılmaz; /yeni-parca veya /degistir kullan"),
    (r">{1,2}\s*\S*ANAYASA\.md", "ANAYASA.md yalnız insan düzenler"),
    (r"\bsudo\b", "sudo yasak"),
    (r"\bmkfs\b|\bdd\s+if=", "disk işlemleri yasak"),
]


def reddet(neden):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": f"yikici-koruma: {neden}",
        }
    }, ensure_ascii=False))
    sys.exit(0)


def yol_izinli(kok, hedef):
    if not hedef:
        return True, ""
    mutlak = os.path.abspath(os.path.join(kok, hedef)) if not os.path.isabs(hedef) else os.path.abspath(hedef)
    kok_m = os.path.abspath(kok)
    if not (mutlak == kok_m or mutlak.startswith(kok_m + os.sep)):
        return False, f"proje kökü dışına yazma: {hedef}"
    goreli = os.path.relpath(mutlak, kok_m)
    if goreli.endswith("ANAYASA.md") and "30-devlet" in goreli:
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
    arac = girdi.get("tool_name", "")
    ti = girdi.get("tool_input", {}) or {}

    if arac in ("Edit", "Write", "MultiEdit"):
        hedef = ti.get("file_path") or ti.get("path") or ""
        ok, neden = yol_izinli(kok, hedef)
        if not ok:
            reddet(neden)
        sys.exit(0)

    if arac == "Bash":
        komut = ti.get("command", "") or ""
        for kalip, neden in YIKICI:
            if re.search(kalip, komut, re.I):
                reddet(f"{neden} — komut: {komut[:160]}")
        # yönlendirme ile proje dışına yazma
        for m in re.finditer(r">{1,2}\s*([^\s;&|]+)", komut):
            hedef = m.group(1).strip("'\"")
            if hedef in ("/dev/null",):
                continue
            if hedef.startswith("/") or hedef.startswith("~"):
                if not os.path.abspath(os.path.expanduser(hedef)).startswith(os.path.abspath(kok)):
                    reddet(f"proje dışına yönlendirme: {hedef}")
        sys.exit(0)

    sys.exit(0)


if __name__ == "__main__":
    main()
