#!/usr/bin/env python3
"""Stop hook — durus-kapisi.

Oturumun sessizce bitmesini engeller. Üç çıkış kapısı vardır, biri açık olmalı:
  A) Son asistan mesajında bir "## Kanıt" bloğu var (komut + çıkış kodu + çıktı özeti), VE
     kontrol.py --kisa sıfır hata veriyor.
  B) 00-sistem/ASK.md var: beyan edilmiş bir kapı, tek soru; sahibinin cevabı bekleniyor.
  C) Son mesaj GUNLUK.md'ye yazılmış bir [durdu] kaydına işaret ediyor ("[durdu]" geçiyor) — engel kaydı.

Hiçbiri yoksa decision: block döner ve additionalContext ile ne yapılacağını söyler.
Döngü koruması: stop_hook_active true ise (bu hook zaten bir kez engelledi ve Claude devam etti) ikinci kez
yalnızca kontrol.py hatası varsa engeller; üçüncü ve sonrası için CLAUDE_CODE_STOP_HOOK_BLOCK_CAP geçerlidir.
Sohbet niteliğindeki kısa mesajlar (soru soruyorsa, "?" ile bitiyorsa ve 600 karakterden kısaysa) serbesttir:
bir kapı sorusu zaten ASK.md gerektirir ama ara soru sorabilmeli.
"""
import json
import os
import re
import subprocess
import sys


def main():
    try:
        girdi = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    kok = os.environ.get("CLAUDE_PROJECT_DIR") or girdi.get("cwd") or os.getcwd()
    mesaj = girdi.get("last_assistant_message") or ""
    aktif = bool(girdi.get("stop_hook_active"))

    ask_var = os.path.exists(os.path.join(kok, "00-sistem", "ASK.md"))
    kanit_var = re.search(r"^##\s*Kan[ıi]t\b", mesaj, re.M) is not None
    durdu_var = "[durdu]" in mesaj
    kisa_soru = len(mesaj.strip()) < 600 and mesaj.strip().endswith("?")

    if ask_var or durdu_var or kisa_soru:
        sys.exit(0)

    # kontrol.py çalıştır (varsa)
    kontrol_yol = os.path.join(kok, "00-sistem", "scripts", "kontrol.py")
    kontrol_hata = None
    if os.path.exists(kontrol_yol):
        try:
            r = subprocess.run([sys.executable, kontrol_yol, "--kisa"], cwd=kok, capture_output=True, text=True, timeout=50)
            if r.returncode != 0:
                kontrol_hata = (r.stdout.strip() + "\n" + r.stderr.strip()).strip()[-1500:]
        except Exception as e:  # noqa: BLE001
            kontrol_hata = f"kontrol.py çalıştırılamadı: {e}"

    if kanit_var and not kontrol_hata:
        sys.exit(0)

    if aktif and not kontrol_hata:
        # Bir kez engellendi, kanıt hâlâ yok ama bütünlük temiz: ikinci kez durdurma.
        sys.exit(0)

    sebep = []
    if not kanit_var:
        sebep.append("Son mesajda '## Kanıt' bloğu yok.")
    if kontrol_hata:
        sebep.append("kontrol.py hata veriyor:\n" + kontrol_hata)
    yol = (
        "Bitirmeden önce üç yoldan birini seç:\n"
        "1) İşi kanıtla kapat: '## Kanıt' başlığı altında çalıştırdığın komutları, çıkış kodlarını ve çıktı özetini yaz; "
        "kontrol.py sıfır hata vermeli (python3 00-sistem/scripts/kontrol.py --kisa).\n"
        "2) Bir karar sahibine aitse /kapi ile Onay Dosyası ve 00-sistem/ASK.md yaz (tek soru) ve turu bitir.\n"
        "3) Takıldıysan GUNLUK.md'ye '[durdu]' satırı ve ILERLEME.md'ye 'siradaki' yaz; mesajında [durdu] kaydına işaret et."
    )
    cikti = {
        "decision": "block",
        "reason": "Yeni Sistem: oturum kanıt, kapı ya da engel kaydı olmadan kapanamaz.",
        "hookSpecificOutput": {
            "hookEventName": "Stop",
            "additionalContext": "\n".join(sebep) + "\n\n" + yol,
        },
    }
    print(json.dumps(cikti, ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
