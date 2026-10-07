#!/usr/bin/env python3
"""pano.py — sistemin durumunu salt okur HTML pano olarak üretir (T-034, ilk aşama: kabuk, Pano, Sağlık).

Kullanım: python3 00-sistem/scripts/pano.py   (argüman yok)
Çıktı: 00-sistem/.kosu/pano/{pano.html, saglik.html, css/} (git dışı). Açmak için: 00-sistem/scripts/pano.sh

Yalnız stdlib; ağa çıkmaz; depoda hiçbir dosyaya yazmaz (yalnız .kosu/pano). Karar vermez, talimat açmaz.
Bütünlük ve bayatlık kontrol.py / bayat.py --json çıktısından alınır (denetim burada yeniden yazılmaz);
frontmatter yscommon ile okunur. Tasarım: 10-insan/kaynaklar/pano-tasarim-paketi (CSS: scripts/pano-tasarim/css).
Üretilen HTML'de betik, style= ve http(s) kaynağı yoktur (test_pano.py denetler).
"""
import csv
import html
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yscommon as yc  # noqa: E402

KOK = yc.kok_bul()
BETIK = os.path.join(KOK, "00-sistem", "scripts")
CIKTI = os.path.join(KOK, "00-sistem", ".kosu", "pano")
CSS = os.path.join(BETIK, "pano-tasarim", "css")
KATLAR = [  # (no, ad, klasör, ekran)
    ("40", "İç ses", "40-ic-ses", None), ("30", "Devlet", "30-devlet", None), ("20", "Şirket", "20-sirket", None),
    ("10", "İnsan", "10-insan", None), ("00", "Sistem", "00-sistem", "saglik.html"),
]
ONAY = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5l3 3 7-7"/></svg>'
CARPI = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8"/></svg>'


def e(x):
    return html.escape(str(x), quote=True)


def oku(yol):
    try:
        with open(os.path.join(KOK, yol), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def sade(metin):
    """Markdown satırını düz metne: wikilink → son parça, `kod` ve ** işaretleri düşer."""
    metin = re.sub(r"\[\[([^\]|#]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1).split("/")[-1], metin)
    return re.sub(r"\*\*|`", "", metin).strip()


def calistir(*arg):
    try:
        r = subprocess.run(list(arg), capture_output=True, text=True, cwd=KOK, timeout=120)
        return r.returncode, r.stdout
    except (OSError, subprocess.TimeoutExpired) as h:
        return -1, str(h)


# ---------- veri ----------

def ilerleme():
    s = oku("00-sistem/ILERLEME.md")
    alan = {}
    for k in ("aktif_talimat", "kapi", "acik_soru", "siradaki"):
        m = re.search(rf"^{k}:\s*(.*)$", s, re.M)
        alan[k] = m.group(1).strip() if m else "belirlenmedi"
    kapanis = []
    m = re.search(r"^## Son kapanış\n(.*?)(?=^## |\Z)", s, re.M | re.S)
    for satir in (m.group(1).splitlines() if m else []):
        k = re.match(r"^- (T-\d+) \(([\d-]+)\):\s*(.*)$", satir)
        if k:
            metin, _, kanit = k.group(3).partition("Kanıt:")
            kapanis.append({"id": k.group(1), "tarih": k.group(2), "metin": sade(metin), "kanit": sade(kanit)})
    alan["kapanis"] = kapanis
    return alan


def bas_ve_kuyruk(deger):
    """'T-034 — açıklama' → ('T-034', 'açıklama'); ayırıcı yoksa (değer, '')."""
    bas, _, kuyruk = deger.partition(" — ")
    return bas.strip(), kuyruk.strip()


def nerede_kaldik():
    s = oku("40-ic-ses/nerede-kaldik.md")
    m = re.search(r"^### Oturum: (.*?)\n(.*?)(?=^### |^## |\Z)", s, re.M | re.S)
    blok = {"oturum": m.group(1).strip() if m else "belirlenmedi", "Konuşulan": [], "Açık": [], "Sonraki": []}
    if not m:
        return blok
    ad = None
    for satir in m.group(2).splitlines():
        b = re.match(r"^\*\*(Konuşulan|Açık|Sonraki)\*\*", satir)
        if b:
            ad = b.group(1)
        elif ad and satir.startswith("- "):
            blok[ad].append(sade(satir[2:]))
    return blok


def talimatlar():
    s = oku("00-sistem/TALIMATLAR.md")
    t = []
    for m in re.finditer(r"^## (T-\d+) — (.*?)\n(.*?)(?=^## |\Z)", s, re.M | re.S):
        g = m.group(3)
        durum = re.search(r"^- Durum:\s*(\S+)", g, re.M)
        kat = re.search(r"^- Kat:\s*(\S+)", g, re.M)
        kapi = re.search(r"^- Kapı:\s*([a-z-]+)", g, re.M)
        t.append({"id": m.group(1), "baslik": m.group(2).strip(), "durum": durum.group(1) if durum else "belirlenmedi",
                  "kat": kat.group(1) if kat else "?", "kapi": kapi.group(1) if kapi else "belirlenmedi"})
    return t


def sayfalar():
    return [(y, fm or {}, g) for y, fm, g, _ in yc.sayfalari_tara(KOK)]


def kontrol():
    kod, cikti = calistir(sys.executable, os.path.join(BETIK, "kontrol.py"), "--json")
    try:
        veri = json.loads(cikti)
    except json.JSONDecodeError:
        veri = {"sayfa": 0, "bag": 0, "hata": [{"yol": "kontrol.py", "mesaj": "JSON okunamadı"}], "uyari": [], "cikis": kod}
    _, kisa = calistir(sys.executable, os.path.join(BETIK, "kontrol.py"), "--kisa")
    satirlar = [s for s in kisa.strip().splitlines() if s.strip()]
    veri["ozet"] = satirlar[0] if satirlar else "kontrol.py çıktı vermedi"
    veri["satirlar"] = satirlar
    return veri


def bayat():
    _, cikti = calistir(sys.executable, os.path.join(BETIK, "bayat.py"), "--json")
    try:
        return json.loads(cikti)
    except json.JSONDecodeError:
        return None


def maliyet():
    satirlar = []
    try:
        with open(os.path.join(KOK, "00-sistem", "MALIYET.csv"), encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                m = re.match(r"\s*([\d.]+)", r.get("usd_tahmin") or "")
                r["usd"] = float(m.group(1)) if m else 0.0
                satirlar.append(r)
    except OSError:
        pass
    return satirlar


def tavan():
    m = re.search(r"^\| Orkestratör.*?oturum:\s*([\d.]+)\s*USD", oku("30-devlet/normlar/MODEL-POLITIKASI.md"), re.M)
    return float(m.group(1)) if m else None


def git(*arg):
    kod, cikti = calistir("git", *arg)
    return cikti.strip() if kod == 0 else "belirlenmedi"


def kimlik(yol):
    ad = yol.rsplit("/", 1)[-1][:-3]
    m = re.match(r"^([A-Z]+-\d+)", ad)
    return m.group(1) if m else ad


# ---------- kabuk ----------

def ray(aktif):
    s = ['<nav class="rail" aria-label="Ekranlar">']
    cur = ' aria-current="page"' if aktif == "pano" else ""
    s.append(f'<a class="rl" href="pano.html" aria-label="Pano"{cur}><svg viewBox="0 0 16 16" aria-hidden="true">'
             '<path d="M2 2h5v5H2zM9 2h5v5H9zM2 9h5v5H2zM9 9h5v5H9z"/></svg><span>Pano</span></a>')
    for no, ad, _, ekran in KATLAR:
        if ekran:
            cur = ' aria-current="page"' if aktif == ekran[:-5] else ""
            s.append(f'<a class="rl" href="{ekran}" aria-label="{e(ad)}"{cur}><b class="kn" aria-hidden="true">{no}</b>'
                     f'<span>{e(ad)}</span></a>')
        else:  # ekran sonraki aşamada
            s.append(f'<a class="rl" aria-label="{e(ad)} (sonraki aşama)" aria-disabled="true"><b class="kn" '
                     f'aria-hidden="true">{no}</b><span>{e(ad)}</span></a>')
    s.append("</nav>")
    return "\n".join(s)


def durum_cubugu(v):
    nokta = "ok" if v["kontrol"]["cikis"] == 0 else "err"
    return (f'<footer class="sbar"><span><span class="dot ok"></span>4k-claude · {e(v["dal"])}</span>'
            f'<span>{e(bas_ve_kuyruk(v["ilerleme"]["aktif_talimat"])[0])}</span>'
            f'<span>kapı: {e(bas_ve_kuyruk(v["ilerleme"]["kapi"])[0])}</span>'
            f'<span>açık soru: {e(bas_ve_kuyruk(v["ilerleme"]["acik_soru"])[0])}</span>'
            f'<a href="saglik.html"><span class="dot {nokta}"></span>bütünlük · {v["kontrol"]["sayfa"]} sayfa</a>'
            f'<span>WIP {v["wip"]}</span><span>gelen {v["gelen"]}</span>'
            f'<span class="gr"></span><span>salt okunur</span>'
            f'<span>üretildi {e(v["zaman"])} · {e(v["commit"])}</span></footer>')


def sayfa(baslik, aktif, govde, v, css):
    return (f'<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>4k-claude — {e(baslik)}</title>\n'
            f'<link rel="stylesheet" href="css/4k-claude.css">\n<link rel="stylesheet" href="css/{css}">\n'
            f'</head>\n<body>\n<div class="app" data-theme="tokyo-night">\n<div class="cols">\n{ray(aktif)}\n'
            f'{govde}\n</div>\n{durum_cubugu(v)}\n</div>\n</body>\n</html>\n')


def komut(k):
    return f'<div class="cmd"><code>{e(k)}</code><button class="btn" type="button">kopyala</button></div>'


def kart(baslik, deger, alt=""):
    return (f'<section class="card"><div class="sec"><h2 class="cap">{e(baslik)}</h2><p class="big">{e(deger)}</p>'
            f'<p class="sm mu">{e(alt)}</p></div></section>')


# ---------- Pano ----------

def pano(v):
    il, nk = v["ilerleme"], v["nerede"]
    sayim = Counter(yc.kat_from_yol(y) for y, _, _ in v["sayfalar"])
    toplam = sum(n for k, n in sayim.items() if k in (0, 1, 2, 3, 4))
    L = ['<aside class="list" aria-label="Katlar ve talimatlar">',
         f'<div class="hd"><h2 class="cap gr">Katlar · {toplam} sayfa</h2><a class="lk sm" href="saglik.html">harita</a></div>',
         '<div class="scr">']
    for no, ad, klasor, ekran in KATLAR:
        n = sum(1 for y, _, _ in v["sayfalar"] if y.startswith(klasor + "/"))
        moc = next((fm for y, fm, _ in v["sayfalar"] if y.startswith(klasor + "/MOC-")), {})
        href = f' href="{ekran}"' if ekran else ""
        L.append(f'<a class="row"{href}><span class="kt">{no}</span><span class="gr c0"><span class="r">'
                 f'<span class="b br gr">{e(ad)}</span><span class="sm mu">{n}</span></span>'
                 f'<span class="sm mu">{e(sade(moc.get("amac") or klasor))}</span></span></a>')
    L.append(f'<a class="row"><span class="kt">01</span><span class="gr c0"><span class="r"><span class="b br gr">'
             f'Gelen kutusu</span><span class="sm mu">{v["gelen"]}</span></span><span class="sm mu">işlenmemiş not '
             f'(48 saat kuralı)</span></span></a>')
    L.append('<div class="hd"><h2 class="cap gr">Son talimatlar</h2><span class="sm mu">TALIMATLAR.md</span></div>')
    for t in reversed(v["talimatlar"][-4:]):
        bd = {"acik": "run", "bekliyor": "wait", "kapali": "off"}.get(t["durum"], "unc")
        L.append(f'<a class="row"><span class="gr c0"><span class="el"><span class="b br">{e(t["id"])}</span> '
                 f'{e(t["baslik"])}</span><span class="r sm"><span class="bd {bd}">{ONAY if bd == "off" else ""}'
                 f'{e(t["durum"])}</span><span class="mu">kat {e(t["kat"])} · {e(t["kapi"])}</span></span></span></a>')
    L.append("</div></aside>")

    obs = "obsidian://open?vault=4k-claude&amp;file=40-ic-ses%2Fnerede-kaldik"
    S = ['<main class="stage">',
         f'<div class="hd"><h1 class="t gr">Pano</h1><span class="sm mu">{e(v["zaman"])}</span>'
         f'<span class="sm mu">{e(v["commit"])}</span><a class="lk sm" href="{obs}">Obsidian’de aç</a></div>',
         '<div class="scr pad c">', '<div class="g4">']
    for baslik, anahtar in (("Aktif talimat", "aktif_talimat"), ("Kapı", "kapi"), ("Açık soru", "acik_soru")):
        bas, kuyruk = bas_ve_kuyruk(il[anahtar])
        S.append(kart(baslik, bas, kuyruk))
    k = v["kontrol"]
    S.append(kart("Bütünlük", "temiz" if k["cikis"] == 0 else f'{len(k["hata"])} hata', k["ozet"]))
    S.append("</div>")
    sira = [p.strip() for p in il["siradaki"].split(";") if p.strip()]
    S.append('<section class="card" aria-label="Sıradaki"><div class="sec"><div class="r"><h2 class="cap gr">Sıradaki'
             '</h2><span class="sm mu">ILERLEME.md</span></div><ol class="no">')
    for i, p in enumerate(sira, 1):
        S.append(f"<li><i>{i}</i><span>{e(p)}</span></li>")
    S.append(f'</ol><p class="sm mu">{e(il["siradaki"])}</p></div></section>')
    S.append('<div class="g2"><section class="card" aria-label="Konuşulan"><div class="sec"><h2 class="cap">Konuşulan'
             '</h2><ul class="bl c">' + "".join(f"<li>{e(x)}</li>" for x in nk["Konuşulan"]) + "</ul></div></section>")
    S.append('<div class="c"><section class="card" aria-label="Açık"><div class="sec"><h2 class="cap">Açık</h2>'
             '<ul class="bl c">' + "".join(f"<li>{e(x)}</li>" for x in nk["Açık"]) + "</ul></div></section>")
    S.append('<section class="card" aria-label="Sonraki"><div class="sec"><h2 class="cap">Sonraki</h2>'
             + "".join(f"<p>{e(x)}</p>" for x in nk["Sonraki"]) + "</div></section></div></div>")
    S.append('<section class="card" aria-label="Son kapanışlar"><div class="sec"><div class="r"><h2 class="cap gr">'
             'Son kapanışlar</h2><span class="sm mu">ILERLEME.md</span></div></div>')
    for kp in il["kapanis"][:3]:
        S.append(f'<div class="sec"><p><span class="b">{e(kp["id"])}</span> <span class="mu">{e(kp["tarih"])}</span> '
                 f'{e(kp["metin"])}</p><p class="sm"><span class="tag">KANIT</span> <span class="mu">'
                 f'{e(kp["kanit"] or "yazılmamış")}</span></p></div>')
    S.append("</section></div></main>")

    adim, soru = v["insan"], v["sorular"]
    D = ['<aside class="side" aria-label="Sıra sende">', '<div class="hd"><h2 class="cap gr">Sıra sende</h2></div>',
         '<div class="scr">', f'<div class="sec"><h3 class="cap">Fiziksel adımlar · {len(adim)}</h3>']
    for ad, nerede in adim:
        D.append(f'<div class="r"><span class="dot wait"></span><span class="gr">{e(ad)}</span>'
                 f'<span class="sm mu">{e(nerede)}</span></div>')
    D.append('</div><div class="sec"><h3 class="cap">Açık sorular [?] · ' + str(len(soru)) + "</h3>")
    for metin, nerede in soru[:2]:
        D.append(f'<p>{e(metin)}</p><p class="sm mu">{e(nerede)}</p>')
    D.append("</div>")
    D.append('<div class="sec"><div class="r"><h3 class="cap gr">Hızlı not</h3><span class="sm mu">KR-001</span></div>'
             + komut('python3 00-sistem/scripts/not.py gozlem "<başlık>" "<metin>"')
             + komut('python3 00-sistem/scripts/not.py fikir "<başlık>" "<metin>"')
             + '<p class="sm mu">01-gelen yerine doğrudan kat 4 sayfası</p></div>')
    D.append('<div class="sec"><div class="r"><h3 class="cap gr">Oturum</h3><span class="sm mu">T-031</span></div>'
             + komut("4k-claude") + '<p class="sm mu">korumalar yalnız klasörde açılan oturumda yüklenir</p></div>')
    D.append("</div></aside>")
    return sayfa("Pano", "pano", "\n".join(L + S + D), v, "pano.css")


# ---------- Sağlık ----------

def denetimler():
    m = re.search(r"^## 11\..*?\n(.*?)(?=^## |\Z)", oku("00-sistem/SEMA.md"), re.M | re.S)
    if not m:
        return []
    return [re.sub(r"^\d+\s+", "", p.strip()) for p in m.group(1).strip().split(" · ")]


def saglik(v):
    k, sayfa_listesi = v["kontrol"], v["sayfalar"]
    harita = len(re.findall(r"^- \[\[", oku("00-sistem/HARITA.md"), re.M))
    claude_md = len(oku("CLAUDE.md").splitlines())
    L = ['<aside class="list" aria-label="Sistem">',
         '<div class="hd"><span class="btn gh">talimatlar</span><span class="btn gh">günlük</span>'
         '<a class="btn on" href="saglik.html" aria-current="page">sağlık</a></div>', '<div class="scr">',
         f'<div class="sec"><div class="r"><h2 class="cap gr">Harita</h2><span class="sm mu">{harita}/200</span></div>'
         f'<progress value="{harita}" max="200"></progress>']
    for no, ad, klasor, _ in KATLAR:
        n = sum(1 for y, _, _ in sayfa_listesi if y.startswith(klasor + "/"))
        L.append(f'<div class="r"><span class="b br">{no}</span><span class="gr">{e(ad)}</span><span class="mu">{n}</span></div>')
    L.append('</div><div class="sec"><h2 class="cap">Türler</h2><dl class="k2 sm">')
    for tur, n in sorted(Counter(str(fm.get("tur", "?")) for _, fm, _ in sayfa_listesi).items()):
        L.append(f"<dt>{e(tur)}</dt><dd>{n}</dd>")
    L.append('</dl></div><div class="sec"><h2 class="cap">Boyut sınırları</h2>'
             f'<div class="r"><span class="gr">CLAUDE.md</span><span class="sm mu">{claude_md}/200 satır</span></div>'
             f'<progress value="{min(claude_md, 200)}" max="200"></progress>'
             f'<div class="r"><span class="gr">HARITA.md</span><span class="sm mu">{harita}/200 sayfa</span></div>'
             f'<progress value="{min(harita, 200)}" max="200"></progress></div>')
    L.append('<div class="sec"><div class="r"><h2 class="cap gr">Salt okur komutlar</h2><span class="sm mu">yazmaz</span>'
             '</div>' + komut("python3 00-sistem/scripts/kontrol.py --kisa") + komut("python3 00-sistem/scripts/bayat.py")
             + komut("python3 00-sistem/scripts/harita.py --dogrula") + "</div></div></aside>")

    temiz = k["cikis"] == 0
    S = ['<main class="stage">',
         f'<div class="hd"><h1 class="t gr">Sağlık</h1><span class="bd {"ok" if temiz else "err"}">'
         f'{ONAY if temiz else CARPI}{"temiz" if temiz else str(len(k["hata"])) + " hata"}</span>'
         f'<span class="sm mu">{e(v["zaman"])}</span></div>', '<div class="scr pad c">',
         '<section class="card" aria-label="Bütünlük denetimi"><div class="sec">'
         + komut("python3 00-sistem/scripts/kontrol.py --kisa") + '<div class="pre">'
         + "".join(f'<div class="ln">{e(s)}</div>' for s in k["satirlar"]) + "</div></div>"]
    d = denetimler()
    S.append(f'<div class="sec"><h2 class="cap">{len(d)} denetim</h2><ol class="dnt">')
    for i, ad in enumerate(d, 1):
        S.append(f"<li><i>{i}</i>{ONAY if temiz else CARPI}<span>{e(ad)}</span></li>")
    S.append("</ol></div></section>")
    b = v["bayat"]
    bayat_satir = (["bayat.py çıktısı okunamadı"] if b is None else
                   [f'{x.get("yol", "?")}: {x.get("neden") or x.get("mesaj") or x}' if isinstance(x, dict) else str(x)
                    for x in b] or [f"Bayat sayfa yok ({len(sayfa_listesi)} sayfa tarandı)."])
    S.append('<div class="g2"><section class="card" aria-label="Bayat"><div class="sec"><h2 class="cap">Bayat</h2>'
             '<div class="pre">' + "".join(f'<div class="ln">{e(s)}</div>' for s in bayat_satir)
             + '</div><p class="sm mu">bayat.py · son_gozden_gecirme 60, alindi 90 gün</p></div></section>')
    m, t = v["maliyet"], v["tavan"]
    sinir = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    hafta = [r for r in m if (r.get("tarih") or "") >= sinir]
    usd7 = sum(r["usd"] for r in hafta)
    en = max(hafta, key=lambda r: r["usd"], default=None)
    S.append('<section class="card" aria-label="Maliyet"><div class="sec"><div class="r"><h2 class="cap gr">Maliyet'
             f'</h2><span class="sm mu">MALIYET.csv</span></div><p><span class="big">{usd7:.2f} USD</span> '
             f'<span class="mu">son 7 gün · {len(hafta)} oturum</span></p><dl class="kv">'
             f'<dt>oturum tavanı</dt><dd>{f"{t:g} USD" if t else "belirlenmedi"}</dd>'
             f'<dt>en yüksek oturum</dt><dd>{e(en.get("session_id", "?")) + " · " + format(en["usd"], ".2f") + " USD" if en else "—"}</dd>'
             f'<dt>tavana oran</dt><dd>{format(en["usd"] / t, ".1f") + "×" if en and t else "—"}'
             f'<progress value="{min(en["usd"], t) if en and t else 0}" max="{t or 1}"></progress></dd></dl></div></section></div>')
    S.append('<section class="card" aria-label="Son oturumlar"><div class="sec"><h2 class="cap">Son oturumlar</h2></div>'
             '<div class="ox"><table class="tb"><thead><tr><th scope="col">Oturum</th><th scope="col">Zaman</th>'
             '<th scope="col">Model</th><th scope="col" class="num">Tur</th><th scope="col" class="num">USD</th></tr>'
             "</thead><tbody>")
    for r in reversed(m[-5:]):
        S.append(f'<tr><td class="b br">{e(r.get("session_id", ""))}</td><td>{e(r.get("tarih", ""))}</td>'
                 f'<td>{e(r.get("model") or "—")}</td><td class="num">{e(r.get("tur") or "—")}</td>'
                 f'<td class="num">{r["usd"]:.2f}</td></tr>')
    S.append("</tbody></table></div></section></div></main>")

    ayar = {}
    try:
        ayar = json.loads(oku(".claude/settings.json") or "{}")
    except json.JSONDecodeError:
        pass
    hooklar = {}
    for olay, liste in (ayar.get("hooks") or {}).items():
        for grup in (liste if isinstance(liste, list) else []):
            for h in (grup.get("hooks", []) if isinstance(grup, dict) else []):
                parca = str(h.get("command") or "?").replace('"', " ").split() or ["?"]
                ad = os.path.basename(parca[-1])
                hooklar.setdefault(ad, []).append(olay)
    sb = ayar.get("sandbox") or {}
    push = [s for s in oku("00-sistem/.kosu/push.log").splitlines() if s.strip()]
    son_push = push[-1].split() if push else []
    surum = re.search(r"^## \[(\d+\.\d+\.\d+)\][^\n]*", oku("00-sistem/DEGISIKLIKLER.md"), re.M)
    D = ['<aside class="side" aria-label="Korumalar ve yedek">', '<div class="hd"><h2 class="cap gr">Korumalar ve yedek'
         '</h2></div>', '<div class="scr">', f'<div class="sec"><h3 class="cap">Hook\'lar · {len(hooklar)}</h3>'
         '<dl class="kv kvw">']
    for ad, olaylar in hooklar.items():
        D.append(f"<dt>{e(ad)}</dt><dd>{e(', '.join(olaylar))}</dd>")
    D.append('</dl><p class="sm"><span class="tag unc">NOT</span> <span class="mu">kullanıcı düzeyi '
             '<span class="nw">kasa-disi-koruma</span> ~/.claude/settings.json’da; burada sayılmaz</span></p></div>')
    D.append('<div class="sec"><h3 class="cap">Sandbox</h3><dl class="kv kvs">'
             f'<dt>açık</dt><dd>{e(sb.get("enabled", "—"))}</dd><dt>yoksa dur</dt><dd>{e(sb.get("failIfUnavailable", "—"))}</dd>'
             f'<dt>sandbox dışı komut</dt><dd>{e(sb.get("allowUnsandboxedCommands", "—"))}</dd></dl></div>')
    D.append('<div class="sec"><h3 class="cap">Yedek ve push</h3><dl class="kv kvs">'
             f'<dt>son push</dt><dd>{e(" ".join(son_push[:2]) or "—")}</dd>'
             f'<dt>sonuç</dt><dd>{e(son_push[2] if len(son_push) > 2 else "—")}</dd>'
             f'<dt>commit</dt><dd>{e(son_push[3] if len(son_push) > 3 else "—")}</dd>'
             f'<dt>uzak</dt><dd>{e(git("remote") or "—")}</dd></dl></div>')
    D.append('<div class="sec"><h3 class="cap">Sistem sürümü</h3><p class="sm mu">'
             f'{e(surum.group(1) if surum else "belirlenmedi")} · DEGISIKLIKLER.md (yayımlanmamış değişiklikler ayrı)</p></div>')
    D.append("</div></aside>")
    return sayfa("Sağlık", "saglik", "\n".join(L + S + D), v, "saglik.css")


def main():
    if len(sys.argv) > 1:
        print("pano.py argüman almaz. Çıktı: 00-sistem/.kosu/pano/", file=sys.stderr)
        return 2
    sl = sayfalar()
    gelen = sum(1 for y, fm, _ in sl if y.startswith("01-gelen/") and fm.get("tur") == "ham" and fm.get("islendi") is not True)
    v = {"ilerleme": ilerleme(), "nerede": nerede_kaldik(), "talimatlar": talimatlar(), "sayfalar": sl,
         "kontrol": kontrol(), "bayat": bayat(), "maliyet": maliyet(), "tavan": tavan(), "gelen": gelen,
         "wip": sum(1 for _, fm, _ in sl if fm.get("tur") == "gorev" and fm.get("kanban") in ("basladi", "kontrol")),
         "insan": [(ad, kimlik(y)) for y, fm, g in sl if yc.kat_from_yol(y) in (1, 2, 3, 4)
                   for m in re.finditer(r"^#{2,4} [^\n]*[İi]nsan noktalar[ıi][^\n]*\n(.*?)(?=^#|\Z)", g, re.M | re.S)
                   for ad in (sade(s).split(":")[0] for s in re.findall(r"^\d+\.\s+(.*)$", m.group(1), re.M))],
         "sorular": [(sade(s), kimlik(y)) for y, _, g in sl if yc.kat_from_yol(y) in (1, 2, 3, 4)
                     for s in re.findall(r"^- \[\?\]\s*(.*)$", g, re.M)],
         "dal": git("rev-parse", "--abbrev-ref", "HEAD"), "commit": git("rev-parse", "--short", "HEAD"),
         "zaman": datetime.now().strftime("%Y-%m-%d %H:%M")}
    os.makedirs(os.path.join(CIKTI, "css"), exist_ok=True)
    for ad in ("4k-claude.css", "pano.css", "saglik.css"):
        shutil.copyfile(os.path.join(CSS, ad), os.path.join(CIKTI, "css", ad))
    for ad, icerik in (("pano.html", pano(v)), ("saglik.html", saglik(v))):
        with open(os.path.join(CIKTI, ad), "w", encoding="utf-8") as f:
            f.write(icerik)
    print(f"Pano üretildi: {os.path.relpath(CIKTI, KOK)}/pano.html, saglik.html · bütünlük çıkışı {v['kontrol']['cikis']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
