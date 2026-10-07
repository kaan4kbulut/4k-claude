#!/usr/bin/env python3
"""Çok olaylı kayıt hook'u — kapanis-kaydi.

SessionEnd        → 00-sistem/MALIYET.csv'ye satır: token toplamları transcript'ten (transcript_path) okunur,
                    çünkü SessionEnd girdisi token taşımaz. Aynı API mesajı transcript'e birden çok satır yazılır ve her
                    satır aynı usage'ı tekrarlar: message.id ile tekilleştirilir. Alt ajan transcript'leri
                    (<oturum>/subagents/*.jsonl) varsa eklenir.
StopFailure       → GUNLUK.md'ye "[hata] oturum — <hata türü>" (bir sonraki oturum neden öldüğünü okur)
PostToolUseFailure→ GUNLUK.md'ye "[hata] <araç> — <hata özeti>"
ConfigChange      → artık ayar-denetimi.py (T-011)

Hiçbir zaman engellemez; yalnız yazar. Alan adları Claude Code sürümüne göre değişebildiği için savunmacı okur.
Maliyet tahmini: fiyatlar 30-devlet/normlar/MODEL-POLITIKASI.md fiyat tablosundan okunur (tek kaynak); önbellek yazımı
usage.cache_creation'daki ayrıma göre fiyatlanır: 5 dk TTL giriş fiyatının 1.25 katı, 1 saat TTL 2 katı (T-013: eski
tek tip 1.25 varsayımı ~%30 düşük tahmin veriyordu; ccusage mutabakatıyla ölçüldü). Abonelikte gerçek fatura
farklıdır; buradaki değer sıra büyüklüğü içindir.
"""
import csv
import glob
import json
import os
import re
import sys
from datetime import datetime

BASLIK = ["session_id", "tarih", "tur", "tokens_in", "tokens_out", "cache_okuma", "cache_yazma", "model", "neden", "usd_tahmin"]


def gunluk_yaz(kok, satir):
    yol = os.path.join(kok, "00-sistem", "GUNLUK.md")
    try:
        with open(yol, "a", encoding="utf-8") as f:
            # GUNLUK satırı tek satırdır: çok satırlı hata özeti (komut çıktısı) " · " ile birleşir (T-036)
            f.write(" · ".join(p.strip() for p in satir.splitlines() if p.strip()) + "\n")
    except Exception:  # noqa: BLE001
        pass


def fiyatlar(kok):
    """MODEL-POLITIKASI.md fiyat tablosu → {"opus 5.5": (giris, cikis, onbellek_okuma)}."""
    f = {}
    try:
        with open(os.path.join(kok, "30-devlet", "normlar", "MODEL-POLITIKASI.md"), encoding="utf-8") as fh:
            for s in fh:
                m = re.match(r"^\|\s*([A-Za-z]+ \d+(?:\.\d+)?)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|", s)
                if m:
                    f[m.group(1).lower()] = (float(m.group(2)), float(m.group(3)), float(m.group(4)))
    except Exception:  # noqa: BLE001
        pass
    return f


def model_adi(model_id):
    """claude-opus-5-5 → "opus 5.5"; claude-haiku-4-5-20251001 → "haiku 4.5"."""
    m = re.match(r"^claude-([a-z]+)-(\d+)(?:-(\d{1,2}))?(?:-|$)", model_id or "")
    if not m:
        return None
    return f"{m.group(1)} {m.group(2)}" + (f".{m.group(3)}" if m.group(3) else "")


def transcript_ozeti(yol):
    """(tur, {message.id: (model, in, out, cache_okuma, cache_yazma)}) — tekilleştirilmiş."""
    mesajlar, tur = {}, 0
    dosyalar = [yol] + sorted(glob.glob(os.path.join(yol[:-6] if yol.endswith(".jsonl") else yol, "subagents", "*.jsonl")))
    for i, d in enumerate(dosyalar):
        try:
            fh = open(d, encoding="utf-8")
        except OSError:
            continue
        with fh:
            for satir in fh:
                try:
                    k = json.loads(satir)
                except Exception:  # noqa: BLE001
                    continue
                m = k.get("message") if isinstance(k.get("message"), dict) else {}
                if i == 0 and k.get("type") == "user" and not k.get("isSidechain"):
                    icerik = m.get("content")
                    if isinstance(icerik, str) or (isinstance(icerik, list) and any(
                            isinstance(b, dict) and b.get("type") == "text" for b in icerik)):
                        tur += 1
                u = m.get("usage")
                if k.get("type") == "assistant" and isinstance(u, dict) and m.get("model") != "<synthetic>":
                    mesajlar[m.get("id") or k.get("requestId") or f"{d}:{len(mesajlar)}"] = (
                        m.get("model") or "", u.get("input_tokens") or 0, u.get("output_tokens") or 0,
                        u.get("cache_read_input_tokens") or 0, u.get("cache_creation_input_tokens") or 0,
                        ((u.get("cache_creation") or {}).get("ephemeral_1h_input_tokens") or 0))
    return tur, mesajlar


def maliyet_satiri(kok, girdi):
    tur, mesajlar = transcript_ozeti(girdi.get("transcript_path") or "")
    fy = fiyatlar(kok)
    top = [0, 0, 0, 0]
    usd, bilinmeyen, modeller = 0.0, set(), {}
    for model, gi, co, cr, cw, cw1s in mesajlar.values():
        for j, v in enumerate((gi, co, cr, cw)):
            top[j] += v
        modeller[model] = modeller.get(model, 0) + co
        p = fy.get(model_adi(model) or "")
        if p is None:
            bilinmeyen.add(model)
            continue
        cw1s = min(cw1s, cw)  # 1 saatlik yazım; kalan 5 dakikalık
        usd += (gi * p[0] + co * p[1] + cr * p[2] + (cw - cw1s) * p[0] * 1.25 + cw1s * p[0] * 2) / 1_000_000
    baskin = max(modeller, key=modeller.get) if modeller else ""
    usd_yazi = f"{usd:.4f}" + (f" (fiyatsız: {','.join(sorted(bilinmeyen))})" if bilinmeyen else "")
    return tur, top, baskin, usd_yazi


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
        try:
            tur, (gi, co, cr, cw), model, usd = maliyet_satiri(kok, girdi)
        except Exception as e:  # noqa: BLE001
            tur, (gi, co, cr, cw), model, usd = "", (0, 0, 0, 0), "", f"okunamadı: {e}"
        yol = os.path.join(kok, "00-sistem", "MALIYET.csv")
        yeni = not os.path.exists(yol)
        try:
            with open(yol, "a", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                if yeni:
                    w.writerow(BASLIK)
                w.writerow([sid, simdi, tur, gi, co, cr, cw, model, girdi.get("reason", ""), usd])
        except Exception:  # noqa: BLE001
            pass
        gunluk_yaz(kok, f"{simdi} [oturum] {sid} — kapandı ({girdi.get('reason', '')}); tur={tur} "
                        f"in={gi} out={co} cache_okuma={cr} usd≈{usd}")

    elif olay == "StopFailure":
        hata = girdi.get("error_type") or girdi.get("error") or "bilinmeyen"
        gunluk_yaz(kok, f"{simdi} [hata] oturum {sid} — durma hatası: {str(hata)[:200]}")

    elif olay == "PostToolUseFailure":
        arac = girdi.get("tool_name", "?")
        err = girdi.get("error") or {}
        ozet = err.get("type") if isinstance(err, dict) else str(err)
        gunluk_yaz(kok, f"{simdi} [hata] {arac} — {str(ozet)[:200]}")


    sys.exit(0)


if __name__ == "__main__":
    main()
