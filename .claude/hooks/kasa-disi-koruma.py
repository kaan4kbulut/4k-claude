#!/usr/bin/env python3
"""Kullanıcı düzeyi PreToolUse hook'u — kasa-disi-koruma (T-031).

Sorun: 4k-claude'un korumaları (.claude/settings.json: sandbox, yikici-koruma, durus-kapisi, ayar-denetimi, maliyet
kaydı) yalnız oturum bu klasörde açılınca yüklenir. Ev dizininden açılan bir oturum klasöre korumasız yazabilir
(2026-10-07: 5fd94f32, T-017..T-024, ≈65,80 USD, hiçbir hook çalışmadı).

Bu hook ~/.claude/settings.json'dan her oturumda çalışır ama yalnız 4k-claude hedeflenince devreye girer:
  Oturum kökü (CLAUDE_PROJECT_DIR) 4k-claude ya da altıysa → sessiz (proje hook'ları zaten çalışıyor).
  Değilse:
    Edit/Write/MultiEdit/NotebookEdit hedefi 4k-claude altında → deny.
    Bash: komut tırnağa duyarlı parçalara bölünür (| || && ; &); `cd` sonraki parçaların dizinini değiştirir.
          Gerçek depoya (realpath) dokunan her parça — dizini depoda ya da bir sözcüğü/yönlendirme hedefi depoda —
          salt okunur olmalı (cat, ls, grep, sha256sum, git status/log/diff/ls-remote, kontrol.py …); değilse deny.
          Yönlendirme (> >>) yazma sayılır. Adında "4k-claude" geçen başka yollar (zip, iş klasörü, URL) etkilenmez (T-036).
  Başka projelerde hiçbir şey yapmaz. Kendi hatasında sessiz geçer (oturumu kilitlemez).
Kasa yolu: FOURK_KASA ortam değişkeni ya da bu dosyanın iki üst dizini.
"""
import glob
import json
import os
import re
import shlex
import sys

KASA = os.path.realpath(os.environ.get("FOURK_KASA")
                        or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
MESAJ = ("4k-claude bu oturumda korumasız: oturum klasör dışında açıldı, bu yüzden projenin sandbox'ı, koruma hook'ları "
         "ve maliyet kaydı yüklenmedi (T-031). Okuma serbest; yazmak için oturumu klasörde açın: `4k-claude` "
         "(ya da `cd ~/Work/4k-claude && claude`).")

# Salt okunur komutlar: ilk sözcük → izinli alt komutlar (None = hepsi)
OKUR = {
    "cat": None, "ls": None, "head": None, "tail": None, "grep": None, "rg": None, "egrep": None, "wc": None,
    "stat": None, "du": None, "file": None, "pwd": None, "cd": None, "echo": None, "tree": None, "diff": None,
    "sort": None, "uniq": None, "cut": None, "tr": None, "column": None, "jq": None, "awk": None, "less": None,
    "realpath": None, "readlink": None, "basename": None, "dirname": None, "true": None, "test": None, "[": None,
    "sha256sum": None, "sha1sum": None, "md5sum": None, "cmp": None, "date": None, "printf": None, "which": None,
    "unzip": None,  # yalnız -l/-t/-v/-Z ile (parca_okur)
    "git": {"status", "log", "diff", "show", "branch", "ls-files", "rev-parse", "remote", "blame", "grep",
            "check-ignore", "describe", "shortlog", "cat-file", "config", "ls-remote"},
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
        if ad == "unzip":
            return any(x in ("-l", "-t", "-v", "-Z", "-lv") for x in k[1:])
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


AYIRAC = {"|", "||", "&&", ";", "&", ";;", "|&"}
YAZ_YON = {">", ">>", ">|", "&>", "&>>"}
KABUK_SOZ = {"do", "then", "else", "elif", "if", "while", "until", "!", "{", "(", "time"}
KAPANIS = {"done", "fi", "}", ")", "esac"}


def sozcukler(komut):
    """Tırnağa duyarlı sözcükler; ayırıcılar ve yönlendirmeler ayrı sözcük (T-036: tırnak içi | boru değildir)."""
    lex = shlex.shlex(komut.replace("\n", " ; "), posix=True, punctuation_chars=True)
    lex.whitespace_split = True
    return list(lex)


def parcalar(komut):
    """[[sözcük, …], …] — ayırıcılarla bölünmüş basit komutlar."""
    p, simdiki = [], []
    for s in sozcukler(komut):
        if s in AYIRAC:
            if simdiki:
                p.append(simdiki)
            simdiki = []
        else:
            simdiki.append(s)
    if simdiki:
        p.append(simdiki)
    return p


def genislet(s, d):
    """$AD / ${AD}: önce bu komutta atanan değişkenler (D=…; cd $D), sonra ortam; bilinmeyen olduğu gibi kalır."""
    return re.sub(r"\$\{?([A-Za-z_]\w*)\}?", lambda m: d.get(m.group(1), os.environ.get(m.group(1), m.group(0))), s)


ADI = re.escape(os.path.basename(KASA))
GOMULU_AD = re.compile(rf"(?:^|[\s/'\"=`;(]){ADI}(?=$|[/\s'\"`;)])")


YORUMLAYICI = re.compile(r"^(?:(?:ba|z|da|k)?sh|python[\d.]*|perl|ruby|node|php|lua)$")


def gomulu_betik(s, onceki, yorumlayici):
    """Başka bir kabuğa/yorumlayıcıya verilen betik metni: yorumlayıcının -c/-e argümanı ya da boşluk içeren sözcük
    (grep -e desen betik değildir)."""
    return (yorumlayici and onceki in ("-c", "-e", "--command", "--eval")) or bool(re.search(r"\s", s))


def glob_kasada(a, cwd):
    """İlk joker bileşenine kadar aç (dosya henüz yoksa da dizin eşleşsin): touch ~/Work/4k-c*/x."""
    p = os.path.join(cwd, os.path.expanduser(a)).split(os.sep)
    i = next(n for n, b in enumerate(p) if any(c in b for c in "*?["))
    return any(kasada(os.path.join(g, *p[i + 1:]), cwd) for g in glob.glob(os.sep.join(p[:i + 1])))


def yol_mu_kasada(s, cwd, d=None):
    """Sözcük ya da içine gömülü bir yol (python3 -c "open('…')", bash -c '… > yol', --opt=yol, glob) depoda mı."""
    if cwd is None:
        return True  # dizin bilinmiyor (cd -, cd $X): temkinli
    s = genislet(s, d or {})
    adaylar = [s] + ([s.split("=", 1)[1]] if "=" in s else [])
    adaylar += re.findall(r"(?:~|/|\.\.?/)[^\s'\"(),;<>|&=]*", s)
    for a in adaylar:
        if not a or re.match(r"^[a-z]+://", a):
            continue
        if kasada(a, cwd):
            return True
        if any(c in a for c in "*?[") and glob_kasada(a, cwd):
            return True
    return False


def parca_incele(k, cwd, d=None):
    """(kasaya dokunuyor mu, salt okur mu, sonraki cwd) — tek basit komut için. d: komut içi değişkenler."""
    d = {} if d is None else d
    dokunur, yazar, temiz = cwd is None or kasada(".", cwd), False, []
    j = 1 if k and k[0] in ("export", "declare", "local", "readonly") else 0
    while j < len(k) and re.match(r"^[A-Za-z_]\w*=", k[j]):
        ad, deger = k[j].split("=", 1)
        d[ad] = genislet(deger, d)
        j += 1
    yorumlayici = any(YORUMLAYICI.match(os.path.basename(t)) for t in k)
    i = 0
    while i < len(k):
        s = k[i]
        if s in YAZ_YON or s in ("<", ">&", "<&", "<<<"):
            hedef = k[i + 1] if i + 1 < len(k) else ""
            if s in YAZ_YON and hedef != "/dev/null":
                yazar = True
            if s in YAZ_YON or s == "<":
                dokunur = dokunur or yol_mu_kasada(hedef, cwd, d)
            if temiz and temiz[-1].isdigit():
                temiz.pop()  # 2>…
            i += 2
            continue
        dokunur = dokunur or yol_mu_kasada(s, cwd, d) or (
            gomulu_betik(s, k[i - 1] if i else "", yorumlayici) and bool(GOMULU_AD.search(genislet(s, d))))
        temiz.append(s)
        i += 1
    while temiz and temiz[0] in KABUK_SOZ:
        temiz = temiz[1:]
    if temiz and temiz[0] == "for":
        temiz = []  # "for x in …" yalnız liste kurar
    if all(t in KAPANIS for t in temiz):
        temiz = []
    yeni_cwd = cwd
    if temiz and temiz[0] in ("cd", "pushd", "popd"):
        hedef = os.path.expanduser(genislet(temiz[1] if len(temiz) > 1 else "~", d))
        bilinmez = temiz[0] == "popd" or hedef.startswith("-") or "$" in hedef or cwd is None
        yeni_cwd = None if bilinmez else os.path.realpath(os.path.join(cwd, hedef))
    okur = not yazar and parca_okur(shlex.join(temiz))
    return dokunur, okur, yeni_cwd


def stdin_yorumlayici(s):
    """Borunun alıcısı, betik dosyası almayan (stdin'den okuyan) bir yorumlayıcı mı: … | bash, … | python3 -."""
    for i, t in enumerate(s):
        if t not in ("|", "|&"):
            continue
        k = []
        for u in s[i + 1:]:
            if u in AYIRAC:
                break
            k.append(u)
        while k and (re.match(r"^[A-Za-z_]\w*=", k[0]) or k[0] in ("sudo", "env", "exec", "command")):
            k = k[1:]
        if k and YORUMLAYICI.match(os.path.basename(k[0])) and all(a == "-" or a.startswith("-") for a in k[1:]):
            return True
    return False


def bash_reddedilir(komut, cwd):
    """Yalnız gerçek depoya (realpath) dokunan ve salt okur olmayan bir parça varsa True (T-036)."""
    try:
        p = parcalar(komut)
    except ValueError:  # ayrıştırılamadı: depoyu anıyorsa temkinli
        return KASA in komut or bool(GOMULU_AD.search(komut)) or kasada(".", cwd)
    degisken = {}
    if stdin_yorumlayici(sozcukler(komut)) and GOMULU_AD.search(komut):
        return True  # boru ile yorumlayıcıya verilen betik (echo '… 4k-claude …' | bash): temkinli
    if re.search(r"<<|`|\$\(", komut):
        # heredoc ve komut ikamesi ayrıştırılmaz: depoyu adıyla anan ya da depoya dokunan parça varsa temkinli
        if GOMULU_AD.search(komut):
            return True
        c = cwd
        for k in p:
            d, _, c = parca_incele(k, c, degisken)
            if d:
                return True
        return False
    for k in p:
        dokunur, okur, cwd = parca_incele(k, cwd, degisken)
        if dokunur and not okur:
            return True
    return False


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
            if bash_reddedilir(ti.get("command") or "", os.path.realpath(cwd)):
                reddet()
    except SystemExit:
        raise
    except Exception:  # noqa: BLE001
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
