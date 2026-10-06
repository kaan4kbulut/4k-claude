#!/usr/bin/env python3
"""Stop hook — durus-kapisi.

Oturumun sessizce bitmesini engeller; ama yalnız bu turda gerçekten iş yapıldıysa.
Ölçüt mesaj metni değil, dosya izidir: SessionStart (oturum-basi) izlenen dosyaların izini
00-sistem/.kosu/durus-izi.json'a yazar; her durmada iz yeniden alınır ve fark bulunur.

  Fark yok                         → serbest (sohbet turu; İç Ses konuşması kesilmez).
  Fark yalnız wiki metninde        → kontrol.py --kisa temizse serbest (makine kanıtı yeter).
    (40-ic-ses, 01-gelen, HARITA, ILERLEME, TALIMATLAR)
  Başka fark var                   → üç kapıdan biri açık olmalı:
    A) Son mesajda '## Kanıt' bölümü, içinde en az bir `komut` ve bir çıkış kodu (→ 0, çıkış 0, exit 1 …),
       ve kontrol.py --kisa temiz.
    B) 00-sistem/ASK.md var (beyan edilmiş kapı, tek soru).
    C) GUNLUK.md'de bu oturumda yazılmış bir [durdu] satırı var.
Kısa ara soru (< 600 karakter, '?' ile biter) her zaman serbesttir.

Döngü koruması: stop_hook_active true ise (bu tur bir kez engellendi) ikinci kez engellemez;
kanıtsız kapanışı GUNLUK'e [hata] satırı olarak yazar ki bir sonraki oturum görsün.
Serbest bırakılan her durmada iz güncellenir: sonraki tur yalnız kendi değişikliğinden sorumludur.
İz dosyası yoksa (hook ilk kez çalışıyor) mevcut iz taban kabul edilir ve serbest bırakılır.
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime

KOK = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
sys.path.insert(0, os.path.join(KOK, "00-sistem", "scripts"))
import yscommon as yc  # noqa: E402

WIKI_ON_EKLER = ("40-ic-ses/", "01-gelen/")
WIKI_DOSYALAR = {"00-sistem/HARITA.md", "00-sistem/ILERLEME.md", "00-sistem/TALIMATLAR.md"}
IZ_YOL = os.path.join("00-sistem", ".kosu", "durus-izi.json")


def iz_oku(kok):
    try:
        with open(os.path.join(kok, IZ_YOL), encoding="utf-8") as f:
            return json.load(f)
    except Exception:  # noqa: BLE001
        return {}


def iz_yaz(kok, sid, iz):
    tum = iz_oku(kok)
    tum[sid] = {"zaman": datetime.now().strftime("%Y-%m-%d %H:%M"), "iz": iz}
    # yalnız son 20 oturumu tut
    if len(tum) > 20:
        for k in sorted(tum, key=lambda k: tum[k].get("zaman", ""))[:-20]:
            tum.pop(k, None)
    yol = os.path.join(kok, IZ_YOL)
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(tum, f)


def gunluk_yaz(kok, satir):
    try:
        with open(os.path.join(kok, "00-sistem", "GUNLUK.md"), "a", encoding="utf-8") as f:
            f.write(satir + "\n")
    except Exception:  # noqa: BLE001
        pass


def kanit_gecerli(mesaj):
    """'## Kanıt' bölümünde en az bir `komut` ve bir çıkış kodu var mı?"""
    m = re.search(r"^##\s*Kan[ıi]t\b[^\n]*\n(.*?)(?=^##\s|\Z)", mesaj, re.M | re.S)
    if not m:
        return False, "Son mesajda '## Kanıt' bölümü yok."
    govde = m.group(1)
    komut = re.search(r"`[^`\n]{2,}`", govde)
    kod = re.search(r"(→|->|=>|çıkış(\s+kodu)?|cikis|exit(\s+code)?|kod)\s*[:=]?\s*\d+", govde, re.I)
    if not (komut and kod):
        return False, "'## Kanıt' bölümü boş ya da eksik: en az bir `komut` ve çıkış kodu (ör. `kontrol.py --kisa` → 0) gerekli."
    return True, ""


def durdu_kaydi_var(kok, baslangic):
    """GUNLUK son 50 satırında, oturum başlangıcından sonra yazılmış [durdu] satırı."""
    try:
        with open(os.path.join(kok, "00-sistem", "GUNLUK.md"), encoding="utf-8") as f:
            satirlar = f.read().splitlines()[-50:]
    except Exception:  # noqa: BLE001
        return False
    for s in satirlar:
        m = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}) \[durdu\]", s)
        if m and m.group(1) >= baslangic:
            return True
    return False


def kontrol_calistir(kok):
    yol = os.path.join(kok, "00-sistem", "scripts", "kontrol.py")
    if not os.path.exists(yol):
        return None
    try:
        r = subprocess.run([sys.executable, yol, "--kisa"], cwd=kok, capture_output=True, text=True, timeout=50)
        if r.returncode != 0:
            return (r.stdout.strip() + "\n" + r.stderr.strip()).strip()[-1500:]
    except Exception as e:  # noqa: BLE001
        return f"kontrol.py çalıştırılamadı: {e}"
    return None


def main():
    try:
        girdi = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    kok = os.environ.get("CLAUDE_PROJECT_DIR") or girdi.get("cwd") or os.getcwd()
    sid = str(girdi.get("session_id") or "bilinmeyen")
    mesaj = girdi.get("last_assistant_message") or ""
    aktif = bool(girdi.get("stop_hook_active"))

    simdi_iz = yc.dosya_izi(kok)
    kayit = iz_oku(kok).get(sid)
    if kayit is None:
        iz_yaz(kok, sid, simdi_iz)
        sys.exit(0)
    degisen = yc.iz_farki(kayit.get("iz", {}), simdi_iz)

    def serbest():
        iz_yaz(kok, sid, simdi_iz)
        sys.exit(0)

    if not degisen:
        serbest()
    if len(mesaj.strip()) < 600 and mesaj.strip().endswith("?"):
        sys.exit(0)  # ara soru; iz güncellenmez, iş hâlâ kanıt bekliyor
    if os.path.exists(os.path.join(kok, "00-sistem", "ASK.md")):
        serbest()
    if durdu_kaydi_var(kok, kayit.get("zaman", "")):
        serbest()

    kontrol_hata = kontrol_calistir(kok)
    yalniz_wiki = all(d.startswith(WIKI_ON_EKLER) or d in WIKI_DOSYALAR for d in degisen)
    if yalniz_wiki and not kontrol_hata:
        serbest()

    kanit_ok, kanit_neden = kanit_gecerli(mesaj)
    if kanit_ok and not kontrol_hata:
        serbest()

    ozet = ", ".join(degisen[:8]) + (f" (+{len(degisen) - 8})" if len(degisen) > 8 else "")
    if aktif:
        gunluk_yaz(kok, f"{datetime.now().strftime('%Y-%m-%d %H:%M')} [hata] oturum {sid[:12]} — kanıtsız durma "
                        f"(ikinci deneme, engel kaldırıldı); değişen: {ozet}")
        serbest()

    sebep = [f"Bu turda değişen dosyalar: {ozet}"]
    if not kanit_ok:
        sebep.append(kanit_neden)
    if kontrol_hata:
        sebep.append("kontrol.py hata veriyor:\n" + kontrol_hata)
    yol = (
        "Bitirmeden önce üç yoldan birini seç:\n"
        "1) İşi kanıtla kapat: '## Kanıt' başlığı altında çalıştırdığın komutları (`ters tırnakla`), çıkış kodlarını ve "
        "çıktı özetini yaz; kontrol.py sıfır hata vermeli (python3 00-sistem/scripts/kontrol.py --kisa).\n"
        "2) Bir karar sahibine aitse /kapi ile Onay Dosyası ve 00-sistem/ASK.md yaz (tek soru) ve turu bitir.\n"
        "3) Takıldıysan `python3 00-sistem/scripts/gunluk.py durdu T-xxx \"<engel>\"` ile [durdu] satırı yaz ve "
        "ILERLEME.md'ye 'siradaki' ekle."
    )
    print(json.dumps({
        "decision": "block",
        "reason": "Yeni Sistem: bu turda değişiklik var; kanıt, kapı ya da engel kaydı olmadan kapanamaz.\n\n"
                  + "\n".join(sebep) + "\n\n" + yol,
    }, ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
