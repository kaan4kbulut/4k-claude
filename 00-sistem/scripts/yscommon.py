#!/usr/bin/env python3
"""Ortak yardımcılar: frontmatter ayrıştırma (PyYAML varsa onu, yoksa yerleşik mini ayrıştırıcı),
sayfa tarama, yol çözümleme. kontrol.py, bayat.py ve harita.py bunu kullanır. Yalnız standart kütüphane zorunludur."""
import datetime
import os
import re
import sys

KAT_KLASOR = {"00-sistem": 0, "01-gelen": 0, "10-insan": 1, "20-sirket": 2, "30-devlet": 3, "40-ic-ses": 4, "90-arsiv": 9}
TARANAN = ["00-sistem", "01-gelen", "10-insan", "20-sirket", "30-devlet", "40-ic-ses"]
HARIC_KLASOR = ("00-sistem/sablonlar", "00-sistem/scripts", "00-sistem/sema", "00-sistem/.kosu")
HARIC_DOSYA = {"00-sistem/HARITA.md", "00-sistem/GUNLUK.md", "00-sistem/ILERLEME.md", "00-sistem/TALIMATLAR.md",
               "00-sistem/KARARLAR.md", "00-sistem/DEGISIKLIKLER.md", "00-sistem/ASK.md"}

try:
    import yaml  # type: ignore
except Exception:  # noqa: BLE001
    yaml = None


def kok_bul(baslangic=None):
    p = os.path.abspath(baslangic or os.getcwd())
    while True:
        if os.path.exists(os.path.join(p, "CLAUDE.md")) and os.path.isdir(os.path.join(p, "00-sistem")):
            return p
        u = os.path.dirname(p)
        if u == p:
            return os.path.abspath(baslangic or os.getcwd())
        p = u


# ---------- mini YAML (yalnız bizim frontmatter alt kümesi) ----------
def _skaler(s):
    s = s.strip()
    if s == "" or s in ("null", "~"):
        return None
    if s in ("true", "True"):
        return True
    if s in ("false", "False"):
        return False
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    if re.fullmatch(r"-?\d+\.\d+", s):
        # sürüm numaraları metin kalsın ("0.1")
        return s
    return s


def _parcala_virgul(ic):
    """Üst düzey virgülle böl (tırnak, [] ve {} içindekileri atla)."""
    parcalar, derinlik, tirnak, cur = [], 0, None, ""
    for ch in ic:
        if tirnak:
            cur += ch
            if ch == tirnak:
                tirnak = None
            continue
        if ch in "\"'":
            tirnak = ch
            cur += ch
        elif ch in "[{":
            derinlik += 1
            cur += ch
        elif ch in "]}":
            derinlik -= 1
            cur += ch
        elif ch == "," and derinlik == 0:
            parcalar.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parcalar.append(cur)
    return [p.strip() for p in parcalar]


def _akis(s):
    s = s.strip()
    if s.startswith("[") and s.endswith("]"):
        ic = s[1:-1].strip()
        return [_akis(p) for p in _parcala_virgul(ic)] if ic else []
    if s.startswith("{") and s.endswith("}"):
        ic = s[1:-1].strip()
        d = {}
        for p in _parcala_virgul(ic):
            if ":" in p:
                k, v = p.split(":", 1)
                d[k.strip()] = _akis(v)
        return d
    return _skaler(s)


def mini_yaml(metin):
    d = {}
    satirlar = metin.splitlines()
    i = 0
    while i < len(satirlar):
        s = satirlar[i]
        if not s.strip() or s.lstrip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", s)
        if not m:
            i += 1
            continue
        k, v = m.group(1), m.group(2)
        if v.strip() == "":
            # blok liste olabilir
            lst = []
            j = i + 1
            while j < len(satirlar) and re.match(r"^\s+-\s+", satirlar[j]):
                lst.append(_akis(re.sub(r"^\s+-\s+", "", satirlar[j])))
                j += 1
            if lst:
                d[k] = lst
                i = j
                continue
            d[k] = None
        else:
            d[k] = _akis(v)
        i += 1
    return d


def _tarihleri_metne(v):
    if isinstance(v, datetime.datetime):
        return v.strftime("%Y-%m-%d %H:%M")
    if isinstance(v, datetime.date):
        return v.isoformat()
    if isinstance(v, dict):
        return {k: _tarihleri_metne(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_tarihleri_metne(x) for x in v]
    return v


def frontmatter_oku(yol):
    """(frontmatter dict | None, govde str, hata str | None)"""
    try:
        with open(yol, encoding="utf-8") as f:
            icerik = f.read()
    except Exception as e:  # noqa: BLE001
        return None, "", f"okunamadı: {e}"
    if not icerik.startswith("---"):
        return None, icerik, None
    parcalar = icerik.split("\n---", 1)
    if len(parcalar) < 2:
        return None, icerik, "frontmatter kapanmamış"
    fm_metin = parcalar[0][3:]
    govde = parcalar[1].lstrip("\n")
    if yaml is not None:
        try:
            fm = yaml.safe_load(fm_metin) or {}
            # sürüm sayıları metne
            if isinstance(fm.get("surum"), float):
                fm["surum"] = f"{fm['surum']:.1f}"
            # PyYAML tırnaksız YYYY-MM-DD'yi date nesnesine çevirir; mini ayrıştırıcı metin bırakır.
            # Alan listesi tutmak yerine tüm tarihleri metne çevir (yeni şablon alanı eklenince kırılmasın).
            fm = _tarihleri_metne(fm)
            return fm, govde, None
        except Exception as e:  # noqa: BLE001
            return None, govde, f"YAML hatası: {e}"
    try:
        return mini_yaml(fm_metin), govde, None
    except Exception as e:  # noqa: BLE001
        return None, govde, f"frontmatter ayrıştırılamadı: {e}"


def sayfalari_tara(kok):
    """Taranan klasörlerdeki tüm .md sayfalarını döndürür: [(goreli_yol, fm, govde, hata)]"""
    sonuc = []
    for kat in TARANAN:
        d = os.path.join(kok, kat)
        if not os.path.isdir(d):
            continue
        for dirpath, dirs, files in os.walk(d):
            dirs.sort()
            for f in sorted(files):
                if not f.endswith(".md"):
                    continue
                yol = os.path.join(dirpath, f)
                goreli = os.path.relpath(yol, kok).replace(os.sep, "/")
                if any(goreli.startswith(h + "/") for h in HARIC_KLASOR):
                    continue
                if goreli in HARIC_DOSYA:
                    continue
                fm, govde, hata = frontmatter_oku(yol)
                sonuc.append((goreli, fm, govde, hata))
    return sonuc


def kat_from_yol(goreli):
    ilk = goreli.split("/")[0]
    return KAT_KLASOR.get(ilk)


def hedef_var(kok, hedef):
    """dayandigi/besledigi/ust/wikilink hedefi dosya olarak var mı (uzantılı ya da uzantısız)."""
    if not hedef or not isinstance(hedef, str):
        return False
    h = hedef.split("#")[0].split("|")[0].strip()
    adaylar = [h, h + ".md"]
    return any(os.path.exists(os.path.join(kok, a)) for a in adaylar)


def normalize_yol(h):
    h = h.split("#")[0].split("|")[0].strip()
    return h[:-3] if h.endswith(".md") else h


# ---------- dosya izi (durus-kapisi: bu turda ne değişti?) ----------
IZ_KOKLER = ("CLAUDE.md", "AGENTS.md", ".claude", "00-sistem", "01-gelen", "10-insan", "20-sirket", "30-devlet", "40-ic-ses", "90-arsiv")
# Hook'ların kendi yazdığı dosyalar iş sayılmaz.
IZ_HARIC = ("00-sistem/.kosu/", "00-sistem/GUNLUK.md", "00-sistem/MALIYET.csv", ".claude/settings.local.json")


def dosya_izi(kok):
    """{goreli_yol: [mtime_ns, boyut]} — izlenen köklerdeki tüm dosyalar (__pycache__ hariç)."""
    iz = {}
    for k in IZ_KOKLER:
        p = os.path.join(kok, k)
        if os.path.isfile(p):
            adaylar = [p]
        elif os.path.isdir(p):
            adaylar = []
            for dirpath, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d != "__pycache__"]
                adaylar.extend(os.path.join(dirpath, f) for f in files)
        else:
            continue
        for a in adaylar:
            g = os.path.relpath(a, kok).replace(os.sep, "/")
            if any(g == h or g.startswith(h) for h in IZ_HARIC):
                continue
            try:
                st = os.stat(a)
            except OSError:
                continue
            iz[g] = [st.st_mtime_ns, st.st_size]
    return iz


def iz_farki(eski, yeni):
    """Eklenen, silinen ya da değişen göreli yollar (sıralı)."""
    return sorted(k for k in set(eski) | set(yeni) if eski.get(k) != yeni.get(k))
