#!/usr/bin/env python3
"""UserPromptSubmit hook — butce-bekcisi (T-028).

MODEL-POLITIKASI'ndaki oturum tavanını oturum sürerken ölçer; kapanis-kaydi maliyeti ancak SessionEnd'de yazıyordu.
Her istemde transcript'ten (alt ajanlar dahil) maliyet tahmini kapanis-kaydi.py'nin hesabıyla yapılır (tek kaynak).
  %80'i geçince          → bir kez uyarı (additionalContext): işi toparlamaya başla.
  %100 ve her katında    → bir kez uyarı + GUNLUK [hata]: tavan aşıldı; işi kanıtla kapat, sahibine brifingde bildir.
Engellemez: tavanda işi kesmek onu yarım bırakır (CLAUDE.md: hiçbir iş sessizce yarım kalmaz); tavan değeri ve
uygulama sertliği sahibinin kararıdır (IMZA-MATRISI A5). Hiçbir zaman çökme ile susturmaz; kendi hatasında sessiz geçer.
Hangi eşiklerin bildirildiği 00-sistem/.kosu/butce-izi.json'da oturum başına tutulur (son 20 oturum).
"""
import importlib.util
import json
import os
import re
import sys
from datetime import datetime

KOK = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
IZ = os.path.join(KOK, "00-sistem", ".kosu", "butce-izi.json")
VARSAYILAN_TAVAN = 5.0


def kapanis_kaydi():
    spec = importlib.util.spec_from_file_location("kapanis_kaydi", os.path.join(KOK, ".claude", "hooks", "kapanis-kaydi.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tavan():
    """MODEL-POLITIKASI tablosunda 'Orkestratör (ana oturum)' satırındaki 'oturum: N USD'."""
    try:
        with open(os.path.join(KOK, "30-devlet", "normlar", "MODEL-POLITIKASI.md"), encoding="utf-8") as f:
            for s in f:
                if s.startswith("| Orkestratör"):
                    m = re.search(r"oturum:\s*([\d.]+)\s*USD", s)
                    if m:
                        return float(m.group(1))
    except OSError:
        pass
    return VARSAYILAN_TAVAN


def iz_oku():
    try:
        with open(IZ, encoding="utf-8") as f:
            return json.load(f)
    except Exception:  # noqa: BLE001
        return {}


def iz_yaz(iz):
    if len(iz) > 20:
        for k in sorted(iz, key=lambda k: iz[k].get("zaman", ""))[:-20]:
            iz.pop(k, None)
    os.makedirs(os.path.dirname(IZ), exist_ok=True)
    with open(IZ, "w", encoding="utf-8") as f:
        json.dump(iz, f)


def esik(usd, t):
    """Bildirilecek en yüksek eşik: 0 (yok), 0.8, 1, 2, 3 … (tavanın katı)."""
    oran = usd / t if t > 0 else 0
    if oran >= 1:
        return int(oran)
    return 0.8 if oran >= 0.8 else 0


def main():
    try:
        girdi = json.load(sys.stdin)
        sid = str(girdi.get("session_id") or "bilinmeyen")
        kk = kapanis_kaydi()
        _, _, _, usd_yazi = kk.maliyet_satiri(KOK, girdi)
        usd = float(usd_yazi.split()[0])
        t = tavan()
        e = esik(usd, t)
        iz = iz_oku()
        onceki = iz.get(sid, {}).get("esik", 0)
        if e <= onceki:
            sys.exit(0)
        iz[sid] = {"zaman": datetime.now().strftime("%Y-%m-%d %H:%M"), "esik": e, "usd": round(usd, 4)}
        iz_yaz(iz)
        if e < 1:
            mesaj = (f"4k-claude bütçe bekçisi: bu oturumun tahmini maliyeti {usd:.2f} USD, oturum tavanının "
                     f"({t:g} USD, MODEL-POLITIKASI) %80'ini geçti. Açık talimatı toparlamaya başla; yeni iş açma.")
        else:
            mesaj = (f"4k-claude bütçe bekçisi: oturum tavanı aşıldı — tahmini {usd:.2f} USD, tavan {t:g} USD "
                     f"({e}×). Açık talimatı kanıtla kapat ve sahibine brifingde maliyeti bildir; tavanı yükseltmek "
                     f"sahibinin kararıdır (IMZA-MATRISI A5).")
            kk.gunluk_yaz(KOK, f"{datetime.now().strftime('%Y-%m-%d %H:%M')} [hata] oturum {sid[:12]} — bütçe tavanı "
                               f"aşıldı: ≈{usd:.2f} USD / tavan {t:g} USD ({e}×)")
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": mesaj}},
                         ensure_ascii=False))
    except Exception:  # noqa: BLE001
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
