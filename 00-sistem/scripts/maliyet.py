#!/usr/bin/env python3
"""maliyet.py — MALIYET.csv tahminini ccusage ile karşılaştırır (yalnız okur; MALIYET.csv'ye yazmaz).

Kullanım:
  python3 00-sistem/scripts/maliyet.py              oturum başına tahmin vs ccusage, toplam fark
  python3 00-sistem/scripts/maliyet.py --gunluk     sonucu GUNLUK.md'ye [oturum] satırı olarak da yaz (/haftalik)
  python3 00-sistem/scripts/maliyet.py --json
Çıkış kodu: 0 toplam fark ≤ %5; 1 fark > %5 (tahmin yöntemi ya da fiyat tablosu bozulmuş olabilir); 2 ccusage yok.

ccusage 20.0.26 (.araclar/ccusage, git dışı) Claude Code oturum kayıtlarını (~/.claude/projects) yerelde okur; --offline ile
fiyatları gömülü tablodan alır, ağa çıkmaz. Bilinen sınır (T-013): çevrimdışı tabloda olmayan modeller (ör. claude-sonnet-5-5)
0 USD sayılır; bu oturumlar "fiyatsız" diye işaretlenir ve toplam karşılaştırmaya girmez.
Eşleşme: MALIYET.csv session_id'nin ilk 12 karakteri ile ccusage oturum kimliğinin başı.
Not: "eski" işaretli satırlar T-013 öncesi tahmin yöntemiyle (önbellek yazımı tek tip 1.25×) yazılmıştır; düşük çıkmaları beklenir.
"""
import csv
import json
import os
import subprocess
import sys
from datetime import datetime

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(os.path.dirname(BURASI))
CCUSAGE = os.path.join(KOK, ".araclar", "ccusage", "node_modules", ".bin", "ccusage")
ESIK = 0.05
YENI_YONTEM = "2026-10-07 01:21"  # kapanis-kaydi.py TTL ayrımlı fiyat değişikliğinin dosya zamanı (T-013, stat ile ölçüldü)


def main():
    arg = sys.argv[1:]
    if not os.path.exists(CCUSAGE):
        print("ccusage kurulu değil. Kurulum (sahibi, bir kez): npm install --prefix .araclar/ccusage ccusage@20.0.26")
        sys.exit(2)
    r = subprocess.run([CCUSAGE, "session", "--json", "--offline"], capture_output=True, text=True, timeout=300)
    try:
        oturumlar = json.loads(r.stdout)["session"]
    except Exception as e:  # noqa: BLE001
        print(f"ccusage çıktısı okunamadı (çıkış {r.returncode}): {e}")
        sys.exit(2)
    cc = {}
    for o in oturumlar:
        if o.get("agent") != "claude":
            continue
        fiyatsiz = sorted(m["modelName"] for m in o.get("modelBreakdowns") or [] if m.get("missingPricing"))
        cc[o["period"]] = (float(o.get("totalCost") or 0), fiyatsiz)

    satirlar = []
    with open(os.path.join(KOK, "00-sistem", "MALIYET.csv"), encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sid = (row.get("session_id") or "").strip()
            try:
                tahmin = float((row.get("usd_tahmin") or "").split()[0])
            except (ValueError, IndexError):
                tahmin = None
            eslesen = [k for k in cc if k.startswith(sid)] if sid else []
            if len(eslesen) != 1:
                satirlar.append({"oturum": sid, "tarih": row.get("tarih"), "tahmin": tahmin, "ccusage": None,
                                 "durum": "eşleşmedi" if not eslesen else "çok eşleşme"})
                continue
            gercek, fiyatsiz = cc[eslesen[0]]
            durum = "fiyatsız: " + ",".join(fiyatsiz) if fiyatsiz else ("eski" if (row.get("tarih") or "") < YENI_YONTEM else "tamam")
            satirlar.append({"oturum": sid, "tarih": row.get("tarih"), "tahmin": tahmin, "ccusage": round(gercek, 4),
                             "fark": None if not gercek or tahmin is None else round((tahmin - gercek) / gercek, 4),
                             "durum": durum})

    yeni = [s for s in satirlar if s["durum"] == "tamam" and s.get("ccusage") and s["tahmin"] is not None]
    toplam_t = sum(s["tahmin"] for s in yeni)
    toplam_g = sum(s["ccusage"] for s in yeni)
    fark = (toplam_t - toplam_g) / toplam_g if toplam_g else None
    ozet = {"karsilastirilan": len(yeni), "tahmin_usd": round(toplam_t, 4), "ccusage_usd": round(toplam_g, 4),
            "fark": None if fark is None else round(fark, 4), "esik": ESIK, "satir": satirlar,
            "eski_satir": sum(1 for s in satirlar if s["durum"] == "eski"),
            "fiyatsiz_satir": sum(1 for s in satirlar if s["durum"].startswith("fiyatsız")),
            "eslesmeyen": sum(1 for s in satirlar if s["durum"] in ("eşleşmedi", "çok eşleşme"))}
    kod = 0 if fark is None or abs(fark) <= ESIK else 1

    if "--json" in arg:
        print(json.dumps(ozet, ensure_ascii=False, indent=1))
    else:
        print(f"{'oturum':13} {'tarih':16} {'tahmin':>8} {'ccusage':>8} {'fark':>7}  durum")
        for s in satirlar:
            fk = f"{s['fark']:+.1%}" if s.get("fark") is not None else "—"
            print(f"{s['oturum']:13} {s['tarih'] or '':16} {s['tahmin'] if s['tahmin'] is not None else '—':>8} "
                  f"{s['ccusage'] if s['ccusage'] is not None else '—':>8} {fk:>7}  {s['durum']}")
        print(f"Toplam (yeni yöntem, {len(yeni)} oturum): tahmin {toplam_t:.4f} USD, ccusage {toplam_g:.4f} USD, "
              + (f"fark {fark:+.1%}" if fark is not None else "karşılaştırılacak satır yok")
              + (" — EŞİK AŞILDI" if kod else "") + f". Eski {ozet['eski_satir']}, fiyatsız {ozet['fiyatsiz_satir']}, "
              f"eşleşmeyen {ozet['eslesmeyen']}.")
    if "--gunluk" in arg:
        with open(os.path.join(KOK, "00-sistem", "GUNLUK.md"), "a", encoding="utf-8") as f:
            f.write(f"{datetime.now():%Y-%m-%d %H:%M} [{'hata' if kod else 'oturum'}] 00-sistem/MALIYET.csv — mutabakat: "
                    f"{len(yeni)} oturum, tahmin {toplam_t:.4f} / ccusage {toplam_g:.4f} USD"
                    + (f", fark {fark:+.1%}" if fark is not None else "") + "\n")
    sys.exit(kod)


if __name__ == "__main__":
    main()
