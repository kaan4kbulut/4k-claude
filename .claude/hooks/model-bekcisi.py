#!/usr/bin/env python3
"""Model bekçisi — PreModelSwitch | PostModelSwitch (T-040). MODEL-POLITIKASI'nı araca bağlar (Anayasa ilke 6).

PreModelSwitch  Hedef model Fable ya da Opus ise permissionDecision "ask": geçiş sahibine sorulur (politika: Sonnet
                varsayılan, büyük işte Opus, Fable yalnız kritik sentez). Sonnet/Haiku ve bilinmeyen modeller serbest.
                Sorulan her geçiş GUNLUK'e [ayar] düşer.
PostModelSwitch Gerçekleşen her geçiş (neden ile) GUNLUK'e [ayar] düşer; engellemez.
Girdi alanları (code.claude.com/docs/en/hooks, okundu 2026-10-07): from_model, to_model, Post'ta reason. Kendi hatasında
sessiz geçer (oturumu kilitlemez).
"""
import json
import os
import sys
from datetime import datetime

KOK = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
PAHALI = {"fable": "Fable (yalnız kritik sentez)", "opus": "Opus (büyük iş, mimari)"}


def model_adi(m):
    if isinstance(m, dict):
        m = m.get("id") or m.get("name") or m.get("display_name") or ""
    return str(m or "?")


def sinif(m, bilgi=None):
    """Sözlük gelirse alan adına güvenmeden tüm metin değerlerine bakılır (to_model_info dahil; T-040 denetci)."""
    parca = [model_adi(m)] + [str(v) for x in (m, bilgi) if isinstance(x, dict) for v in x.values() if isinstance(v, str)]
    ad = " ".join(parca).lower()
    return next((k for k in PAHALI if k in ad), None)


def gunluk(not_):
    satir = f"{datetime.now().strftime('%Y-%m-%d %H:%M')} [ayar] model — {' '.join(str(not_).split())[:300]}"
    try:
        with open(os.path.join(KOK, "00-sistem", "GUNLUK.md"), "a", encoding="utf-8") as f:
            f.write(satir + "\n")
    except Exception:  # noqa: BLE001
        pass


def main():
    try:
        g = json.load(sys.stdin)
        olay = g.get("hook_event_name", "")
        eski, yeni = model_adi(g.get("from_model")), model_adi(g.get("to_model"))
        if olay == "PreModelSwitch":
            k = sinif(g.get("to_model"), g.get("to_model_info"))
            if k:
                gunluk(f"geçiş istendi {eski} → {yeni}: sahibine soruldu (MODEL-POLITIKASI, {PAHALI[k]})")
                print(json.dumps({"hookSpecificOutput": {
                    "hookEventName": "PreModelSwitch", "permissionDecision": "ask",
                    "permissionDecisionReason": f"4k-claude MODEL-POLITIKASI: {yeni} pahalı katman — {PAHALI[k]}. "
                                                "Oturum tavanı 5 USD; tavan/politika değişikliği sahibinin (A5)."}},
                    ensure_ascii=False))
        elif olay == "PostModelSwitch":
            gunluk(f"geçti {eski} → {yeni} (neden: {g.get('reason') or 'belirtilmedi'})")
    except Exception:  # noqa: BLE001
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
