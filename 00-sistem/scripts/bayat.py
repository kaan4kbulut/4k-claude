#!/usr/bin/env python3
"""bayat.py — süresi dolan ve gözden geçirilmemiş sayfaları listeler (yalnız okur). /uyku bunu kullanır.

Kurallar (SEMA ve rules/40-ic-ses):
  gozlem      : olusturma > 30 gün ve atıf (besledigi + gelen bağ) < 3  → öneri: arsiv
  gorev       : kanban tamam/iptal değil ve olusturma > 90 gün           → öneri: ilerlet / bekle / iptal (sahibine sor)
  fikir       : merdiven 1 ve son_dokunus > 30 gün ve dokunus_sayisi ≤ 1 → öneri: oldur (sor)
  her sayfa   : son_gozden_gecirme > 60 gün                               → öneri: gozden gecir
  web kaynak  : alindi > 90 gün                                           → öneri: TAZELIK, yeniden kontrol
  ham (gelen) : islendi false ve islenecek_son geçmiş                      → öneri: arsiv (48 saat kuralı)
  kural/yonerge: sunset ≤ bugün + 14 gün                                   → öneri: gözden geçir / uzat / kaldır
Çıktı: tek satır/sayfa: `oneri · yol · neden`. --json ile JSON.
"""
import json
import os
import sys
from datetime import date, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yscommon as yc  # noqa: E402


def t(s):
    try:
        return datetime.strptime(str(s)[:10], "%Y-%m-%d").date()
    except Exception:  # noqa: BLE001
        return None


def main():
    kok = yc.kok_bul()
    bugun = date.today()
    sayfalar = yc.sayfalari_tara(kok)
    fm_map = {y: fm for y, fm, g, e in sayfalar if fm and not e}
    gelen_atif = {}
    for y, fm in fm_map.items():
        for h in (fm.get("dayandigi") or []):
            if isinstance(h, str):
                gelen_atif[yc.normalize_yol(h)] = gelen_atif.get(yc.normalize_yol(h), 0) + 1
    sonuc = []
    for y, fm in fm_map.items():
        tur = fm.get("tur")
        ol = t(fm.get("olusturma"))
        yas = (bugun - ol).days if ol else None
        if fm.get("durum") == "arsiv":
            continue
        if tur == "gozlem" and yas is not None and yas > 30:
            atif = len(fm.get("besledigi") or []) + gelen_atif.get(yc.normalize_yol(y), 0)
            if atif < 3:
                sonuc.append(("arsiv", y, f"gözlem {yas} gün, atıf {atif} < 3"))
        if tur == "gorev" and fm.get("kanban") not in ("tamam", "iptal") and yas is not None and yas > 90:
            sonuc.append(("sor: ilerlet/bekle/iptal", y, f"görev {yas} gün açık"))
        if tur == "fikir" and fm.get("merdiven") in (0, 1):
            sd = t(fm.get("son_dokunus"))
            if sd and (bugun - sd).days > 30 and (fm.get("dokunus_sayisi") or 0) <= 1:
                sonuc.append(("sor: oldur", y, f"fikir M{fm.get('merdiven')} {(bugun - sd).days} gün dokunulmadı"))
        sg = t(fm.get("son_gozden_gecirme"))
        if sg and (bugun - sg).days > 60:
            sonuc.append(("gozden-gecir", y, f"son gözden geçirme {(bugun - sg).days} gün önce"))
        al = t(fm.get("alindi"))
        if al and (bugun - al).days > 90:
            sonuc.append(("TAZELIK", y, f"alındı {(bugun - al).days} gün önce"))
        if tur == "ham" and not fm.get("islendi"):
            son = t(fm.get("islenecek_son"))
            if son and son < bugun:
                sonuc.append(("arsiv", y, "48 saat kuralı aşıldı"))
        if tur in ("kural", "yonerge"):
            sn = t(fm.get("sunset"))
            if sn and (sn - bugun).days <= 14:
                sonuc.append(("sunset", y, f"sunset {sn}"))
    if "--json" in sys.argv:
        print(json.dumps([{"oneri": o, "yol": y, "neden": n} for o, y, n in sonuc], ensure_ascii=False, indent=1))
        return
    if not sonuc:
        print(f"Bayat sayfa yok ({len(fm_map)} sayfa tarandı).")
        return
    print(f"{len(sonuc)} bayat/dikkat ({len(fm_map)} sayfa tarandı):")
    for o, y, n in sonuc:
        print(f"  {o:<26} {y} — {n}")


if __name__ == "__main__":
    main()
