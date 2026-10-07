#!/usr/bin/env python3
"""test-kurulum.py — 4k-claude'un ayrı test kopyası (T-035). Sahibi gerçek depoya dokunmadan sistemi ve panoyu dener.

Kullanım (kurulum: ln -s <kasa>/00-sistem/scripts/test-kurulum.py ~/.local/bin/4k-claude-test):
  4k-claude-test              kopyayı Claude Code ile açar (yoksa önce kurar)
  4k-claude-test guncelle     gerçek deponun HEAD'inden yeni kopya kurar; doğrulamayı geçerse geçer
  4k-claude-test pano         kopyanın panosunu üretir ve açar
  4k-claude-test geri         bir önceki kopyaya döner
  4k-claude-test durum        kurulum bilgisi

Yer: $FOURK_TEST_KOK ya da ~/.local/share/4k-claude-test
  kasa/        çalışan test kopyası (sabit yol: Claude Code klasör güveni bir kez sorulur)
  surumler/    yerinden çıkan ve doğrulamayı geçemeyen kopyalar (silinmez)
  kurulum.json son kurulum ve geçmiş
Kopya `git clone` ile yalnız işlenmiş (commit'li) hâli alır; uzak depo bağı kaldırılır (gerçek depoya push edemez,
otomatik push birimi yalnız gerçek depoyu izler). Kopyanın kökündeki `.test-kopyasi` işaretini pano gösterir.
Doğrulama: kopyada kontrol.py --kisa ve --test. Geçmezse çalışan kopya değişmez.
"""
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime

KAYNAK = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", ".."))
YER = os.path.expanduser(os.environ.get("FOURK_TEST_KOK") or "~/.local/share/4k-claude-test")
KASA = os.path.join(YER, "kasa")
SURUMLER = os.path.join(YER, "surumler")
KAYIT = os.path.join(YER, "kurulum.json")
ISARET = ".test-kopyasi"


def git(*arg, cwd=KAYNAK):
    r = subprocess.run(["git", *arg], cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout.strip() + r.stderr.strip()


def kayit_oku():
    try:
        with open(KAYIT, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {"gecmis": []}


def kayit_yaz(k):
    with open(KAYIT, "w", encoding="utf-8") as f:
        json.dump(k, f, ensure_ascii=False, indent=1)


def damga():
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def dogrula(kok):
    """Kopyada bütünlük ve testler; (geçti mi, özet). FOURK_TEST_DOGRULAMA=kisa yalnız --kisa koşar (testlerin testi)."""
    env = dict(os.environ, FOURK_DOGRULAMA_ICINDE="1")
    kipler = ["--kisa"] if os.environ.get("FOURK_TEST_DOGRULAMA") == "kisa" else ["--kisa", "--test"]
    for kip in kipler:
        try:
            r = subprocess.run([sys.executable, os.path.join(kok, "00-sistem", "scripts", "kontrol.py"), kip],
                               cwd=kok, capture_output=True, text=True, env=env, timeout=900)
        except subprocess.TimeoutExpired:
            return False, f"kontrol.py {kip} 900 sn'de bitmedi"
        if r.returncode != 0:
            return False, f"kontrol.py {kip} → {r.returncode}: {(r.stdout + r.stderr).strip().splitlines()[-1:]}"
    return True, "kontrol.py " + " ".join(kipler) + " → 0"


def guncelle():
    os.makedirs(SURUMLER, exist_ok=True)
    kod, sha = git("rev-parse", "--short", "HEAD")
    if kod:
        print(f"Kaynak depo okunamadı: {sha}", file=sys.stderr)
        return 2
    yeni = os.path.join(YER, f"yeni-{damga()}-{sha}")
    kod, cikti = git("clone", "--quiet", "--no-hardlinks", KAYNAK, yeni)
    if kod:
        print(f"Kopya alınamadı: {cikti}", file=sys.stderr)
        return 2
    git("remote", "remove", "origin", cwd=yeni)
    _, uzak = git("remote", cwd=yeni)
    with open(os.path.join(yeni, ISARET), "w", encoding="utf-8") as f:
        f.write(f"4k-claude TEST kopyası · kaynak {KAYNAK} · {sha}\n")
    with open(os.path.join(yeni, ".git", "info", "exclude"), "a", encoding="utf-8") as f:
        f.write(f"\n{ISARET}\n")
    gecti, ozet = (False, f"uzak depo bağı kaldırılamadı ({uzak}); kopya gerçek depoya push edebilirdi") if uzak \
        else dogrula(yeni)
    k = kayit_oku()
    satir = {"zaman": datetime.now().strftime("%Y-%m-%d %H:%M"), "commit": sha, "dogrulama": ozet, "gecti": gecti}
    if not gecti:
        hedef = os.path.join(SURUMLER, os.path.basename(yeni).replace("yeni-", "basarisiz-"))
        os.rename(yeni, hedef)
        satir["yer"] = hedef
        k["gecmis"].append(satir)
        kayit_yaz(k)
        print(f"Doğrulama geçmedi, çalışan kopya değişmedi. {ozet}\nBaşarısız kopya: {hedef}")
        return 1
    if os.path.isdir(KASA):
        eski = os.path.join(SURUMLER, f"eski-{damga()}-{k.get('commit', 'bilinmiyor')}")
        os.rename(KASA, eski)
        satir["onceki"] = eski
    try:
        os.rename(yeni, KASA)
    except OSError:
        if satir.get("onceki"):
            os.rename(satir["onceki"], KASA)  # çalışan kopya yerine döner
        raise
    k.update({"kaynak": KAYNAK, "commit": sha, "kuruldu": satir["zaman"], "dogrulama": ozet})
    k["gecmis"].append(satir)
    kayit_yaz(k)
    print(f"Test kopyası hazır: {KASA} ({sha}) · {ozet}")
    return 0


def geri():
    k = kayit_oku()
    onceki = next((g.get("onceki") for g in reversed(k["gecmis"]) if g.get("gecti") and g.get("onceki")
                   and os.path.isdir(g["onceki"])), None)
    if not onceki:
        print("Dönülecek önceki kopya yok.", file=sys.stderr)
        return 1
    if os.path.isdir(KASA):
        os.rename(KASA, os.path.join(SURUMLER, f"geri-alinan-{damga()}-{k.get('commit', 'bilinmiyor')}"))
    os.rename(onceki, KASA)
    _, sha = git("rev-parse", "--short", "HEAD", cwd=KASA)
    k.update({"commit": sha, "kuruldu": datetime.now().strftime("%Y-%m-%d %H:%M"), "dogrulama": "geri alındı"})
    k["gecmis"].append({"zaman": k["kuruldu"], "commit": sha, "geri": onceki, "gecti": True})
    kayit_yaz(k)
    print(f"Önceki kopyaya dönüldü: {sha}")
    return 0


def kurulu_mu():
    if os.path.isdir(KASA):
        return True
    print("Test kopyası yok; kuruluyor…")
    return guncelle() == 0


def main():
    komut = sys.argv[1] if len(sys.argv) > 1 else "ac"
    if komut == "guncelle":
        return guncelle()
    if komut == "geri":
        return geri()
    if komut == "durum":
        k = kayit_oku()
        print(json.dumps({x: k.get(x) for x in ("kaynak", "commit", "kuruldu", "dogrulama")} | {"yer": KASA},
                         ensure_ascii=False, indent=1))
        return 0
    if komut == "pano":
        if not kurulu_mu():
            return 1
        r = subprocess.run([sys.executable, os.path.join(KASA, "00-sistem", "scripts", "pano.py")], cwd=KASA)
        if r.returncode == 0 and "--acma" not in sys.argv:
            subprocess.Popen(["xdg-open", os.path.join(KASA, "00-sistem", ".kosu", "pano", "pano.html")],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return r.returncode
    if komut == "ac":
        if not kurulu_mu():
            return 1
        if not shutil.which("claude"):
            print("claude komutu bulunamadı.", file=sys.stderr)
            return 2
        os.chdir(KASA)
        os.execvp("claude", ["claude", *sys.argv[2:]])
    print(__doc__.split("\n\n")[1], file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
