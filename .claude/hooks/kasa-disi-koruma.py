#!/usr/bin/env python3
"""Kullanıcı düzeyi PreToolUse hook'u — kasa-disi-koruma (T-031).

Sorun: 4k-claude'un korumaları (.claude/settings.json: sandbox, yikici-koruma, durus-kapisi, ayar-denetimi, maliyet
kaydı) yalnız oturum bu klasörde açılınca yüklenir. Ev dizininden açılan bir oturum klasöre korumasız yazabilir
(2026-10-07: 5fd94f32, T-017..T-024, ≈65,80 USD, hiçbir hook çalışmadı).

Bu hook ~/.claude/settings.json'dan her oturumda çalışır ama yalnız 4k-claude hedeflenince devreye girer:
  Oturum kökü (CLAUDE_PROJECT_DIR) 4k-claude ya da altıysa → sessiz (proje hook'ları zaten çalışıyor).
  Değilse:
    Edit/Write/MultiEdit/NotebookEdit hedefi 4k-claude altında → deny.
    Bash: cwd 4k-claude altında ya da komut 4k-claude yolunu anıyorsa → her parça salt okunur olmalı
          (cat, ls, grep, git status/log/diff/show, kontrol.py …); değilse deny. Yönlendirme (> >>) yazma sayılır.
  Başka projelerde hiçbir şey yapmaz. Kendi hatasında sessiz geçer (oturumu kilitlemez).
Kasa yolu: FOURK_KASA ortam değişkeni ya da bu dosyanın iki üst dizini.
"""
import json
import os
import re
import shlex
import sys

KASA = os.path.realpath(os.environ.get("FOURK_KASA")
                        or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
MESAJ = ("4k-claude bu oturumda korumasız: oturum klasör dışında açıldı, bu yüzden projenin sandbox'ı, koruma hook'ları "
         "ve maliyet kaydı yüklenmedi (T-031). Okuma serbest; yazmak için oturumu klasörde açın: `4k-claude` "
         "(ya da `cd ~/Downloads/4k-claude && claude`).")

# Salt okunur komutlar: ilk sözcük → izinli alt komutlar (None = hepsi)
OKUR = {
    "cat": None, "ls": None, "head": None, "tail": None, "grep": None, "rg": None, "egrep": None, "wc": None,
    "stat": None, "du": None, "file": None, "pwd": None, "cd": None, "echo": None, "tree": None, "diff": None,
    "sort": None, "uniq": None, "cut": None, "tr": None, "column": None, "jq": None, "awk": None, "less": None,
    "realpath": None, "readlink": None, "basename": None, "dirname": None, "true": None, "test": None, "[": None,
    "git": {"status", "log", "diff", "show", "branch", "ls-files", "rev-parse", "remote", "blame", "grep",
            "check-ignore", "describe", "shortlog", "cat-file", "config"},
}
OKUR_BETIK = {"kontrol.py", "bayat.py", "ara.py", "maliyet.py"}  # yalnız okur (harita.py --dogrula, scorecard.py ayrıca)


def kasada(yol, cwd):
    if not yol:
        return False
    p = os.path.realpath(os.path.join(cwd, os.path.expanduser(yol)))
    return p == KASA or p.startswith(KASA + os.sep)


def parca_okur(parca):
    try:
        k = shlex.split(parca)
    except ValueError:
        return False
    while k and re.match(r"^\w+=", k[0]):  # ortam ataması
        k = k[1:]
    if not k:
        return True
    ad = os.path.basename(k[0])
    if ad in OKUR:
        alt = OKUR[ad]
        if ad == "git":
            sozcukler = [x for x in k[1:] if not x.startswith("-")]
            # git -C <yol> <alt>: -C'nin değerini atla
            if "-C" in k:
                i = k.index("-C")
                sozcukler = [x for x in k[i + 2:] if not x.startswith("-")]
            if not sozcukler or sozcukler[0] not in alt:
                return False
            if sozcukler[0] == "config" and not any(x in k for x in ("--get", "--list", "-l", "--get-regexp")):
                return False
            return True
        if ad == "awk" and re.search(r"system\s*\(|print\s*>", parca):
            return False
        return True
    if ad in ("sed",):
        return "-i" not in " ".join(k) and not any(x.startswith("-i") for x in k)
    if ad == "find":
        return not any(x in k for x in ("-delete", "-exec", "-execdir", "-fprint", "-fprintf"))
    if ad in ("python3", "python"):
        betik = os.path.basename(k[1]) if len(k) > 1 else ""
        if betik in OKUR_BETIK and "--yaz" not in k:
            return True
        if betik == "harita.py" and "--dogrula" in k:
            return True
        if betik == "scorecard.py" and "--yaz" not in k:
            return True
    return False


def bash_okur(komut):
    if re.search(r"(?<![0-9&])>{1,2}(?!\s*/dev/null|&)", re.sub(r"[0-9]?>&[0-9]", "", komut)):
        return False  # yönlendirme yazmadır
    if re.search(r"<<|`|\$\(", komut):
        return False  # heredoc ve komut ikamesi ayrıştırılmaz: temkinli
    parcalar = [p.strip() for p in re.split(r"\|\||&&|[;|\n]", komut) if p.strip()]
    return all(parca_okur(p) for p in parcalar)


def reddet():
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                             "permissionDecisionReason": MESAJ}}, ensure_ascii=False))
    sys.exit(0)


def main():
    try:
        girdi = json.load(sys.stdin)
        proje = os.environ.get("CLAUDE_PROJECT_DIR") or ""
        if proje and kasada(proje, "/"):
            sys.exit(0)
        cwd = girdi.get("cwd") or os.getcwd()
        arac = girdi.get("tool_name", "")
        ti = girdi.get("tool_input") or {}
        if arac in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
            if kasada(ti.get("file_path") or ti.get("notebook_path") or "", cwd):
                reddet()
            sys.exit(0)
        if arac == "Bash":
            komut = ti.get("command") or ""
            anilan = kasada(".", cwd) or KASA in komut or "4k-claude" in komut
            if anilan and not bash_okur(komut):
                reddet()
    except SystemExit:
        raise
    except Exception:  # noqa: BLE001
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
