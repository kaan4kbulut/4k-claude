#!/usr/bin/env python3
"""Çok olaylı kayıt hook'u — kapanis-kaydi.

SessionEnd        → 00-sistem/MALIYET.csv'ye satır (session_id, tarih, tur, token girdi/çıktı, neden, usd_tahmin)
StopFailure       → GUNLUK.md'ye "[hata] oturum — <hata türü>" (bir sonraki oturum neden öldüğünü okur)
PostToolUseFailure→ GUNLUK.md'ye "[hata] <araç> — <hata özeti>"
ConfigChange      → GUNLUK.md'ye "[ayar] <kaynak> — ayar değişti" (denetim izi)

Hiçbir zaman engellemez; yalnız yazar. Alan adları Claude Code sürümüne göre değişebildiği için savunmacı okur.
Maliyet tahmini: MODEL-POLITIKASI.md'deki Sonnet 5.5 fiyatı varsayılır (2 / 10 USD per M token); gerçek maliyet
`/usage` veya OTel ile ölçülür; buradaki değer yalnız sıra büyüklüğü içindir.
"""
import csv
import json
import os
import sys
from datetime import datetime


def gunluk_yaz(kok, satir):
    yol = os.path.join(kok, "00-sistem", "GUNLUK.md")
    try:
        with open(yol, "a", encoding="utf-8") as f:
            f.write(satir.rstrip("\n") + "\n")
    except Exception:  # noqa: BLE001
        pass


def main():
    try:
        girdi = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    kok = os.environ.get("CLAUDE_PROJECT_DIR") or girdi.get("cwd") or os.getcwd()
    olay = girdi.get("hook_event_name", "")
    simdi = datetime.now().strftime("%Y-%m-%d %H:%M")
    sid = str(girdi.get("session_id", ""))[:12]

    if olay == "SessionEnd":
        tur = girdi.get("total_turns") or girdi.get("turns") or ""
        gi = girdi.get("total_tokens_input") or girdi.get("input_tokens") or girdi.get("tokens_input") or 0
        co = girdi.get("total_tokens_output") or girdi.get("output_tokens") or girdi.get("tokens_output") or 0
        try:
            usd = round((float(gi) * 2 + float(co) * 10) / 1_000_000, 4)
        except Exception:  # noqa: BLE001
            usd = ""
        yol = os.path.join(kok, "00-sistem", "MALIYET.csv")
        yeni = not os.path.exists(yol)
        try:
            with open(yol, "a", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                if yeni:
                    w.writerow(["session_id", "tarih", "tur", "tokens_in", "tokens_out", "neden", "usd_tahmin_sonnet"])
                w.writerow([sid, simdi, tur, gi, co, girdi.get("reason", ""), usd])
        except Exception:  # noqa: BLE001
            pass
        gunluk_yaz(kok, f"{simdi} [oturum] {sid} — kapandı ({girdi.get('reason', '')}); tur={tur} in={gi} out={co}")

    elif olay == "StopFailure":
        hata = girdi.get("error_type") or girdi.get("error") or "bilinmeyen"
        gunluk_yaz(kok, f"{simdi} [hata] oturum {sid} — durma hatası: {str(hata)[:200]}")

    elif olay == "PostToolUseFailure":
        arac = girdi.get("tool_name", "?")
        err = girdi.get("error") or {}
        ozet = err.get("type") if isinstance(err, dict) else str(err)
        gunluk_yaz(kok, f"{simdi} [hata] {arac} — {str(ozet)[:200]}")

    elif olay == "ConfigChange":
        gunluk_yaz(kok, f"{simdi} [ayar] {girdi.get('source', '?')} — ayar değişti (denetim izi)")

    sys.exit(0)


if __name__ == "__main__":
    main()
