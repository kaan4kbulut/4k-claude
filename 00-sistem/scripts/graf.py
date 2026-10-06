#!/usr/bin/env python3
"""graf.py — wiki'nin bağ grafı ve yapısal denetimi (yalnız okur; LLM yok, ağ yok).

Kullanım:
  python3 00-sistem/scripts/graf.py            özet (≤ 30 satır) + 00-sistem/.kosu/graf/{graf.json, graf.html, rapor.md}
  python3 00-sistem/scripts/graf.py --json     özet JSON
Çıkış kodu: 0 (bulgular uyarıdır; kontrol.py'nin yerini tutmaz), 2 Graphify bulunamadı.

Graf: düğüm = frontmatter'lı her sayfa (kontrol.py'nin taradığı küme). Kenarlar, hepsi EXTRACTED (tahmin yok):
  dayanir   A.dayandigi ∋ B          (besledigi bunun tersidir; kontrol.py iki yönlülüğü ayrıca denetler)
  ust       A.ust = MOC
  bahseder  A'nın gövdesinde [[B]]   (yalnız dayanir/ust ile zaten bağlı değilse)
Graphify (graphifyy, sürüm SABIT_SURUM) yalnız kütüphane olarak kullanılır: Leiden topluluk tespiti, merkez düğümler,
topluluk sınırını aşan bağlar ve vis.js HTML görünümü. `graphify install`, git hook'ları ve `--mode deep` KULLANILMAZ
(CLAUDE.md'ye ve settings.json'a yazar; deep modu içeriği LLM'e gönderir). Graphify'ın kendi markdown çıkarıcısı
frontmatter'daki düz yol listelerinden kenar üretmediği için graf burada kurulur.
Not: graf.html tarayıcıda açılınca vis-network kütüphanesini unpkg.com'dan indirir; sayfa verisi gönderilmez.

Yorum (/uyku ve /haftalik için):
  bileşen > 1      bir sayfa kümesi geri kalanla hiç bağlı değil — MOC ya da dayanak eksik olabilir
  yetim            hiç bağı olmayan sayfa
  zayıf bağlı      tek bağı olan sayfa (çoğu yalnız ust MOC'una bağlı) — bağ adayı
  merkez           en çok bağlı sayfalar — değişirse etkisi geniş, /degistir'de dikkat
  sınır aşan bağ   farklı toplulukları birleştiren bağ — yansıma (40-ic-ses/yansimalar) adayı
"""
import json
import os
import re
import sys

SABIT_SURUM = "0.9.77"
BURASI = os.path.dirname(os.path.abspath(__file__))


def graphify_yukle():
    """graphify yoksa projenin .venv'iyle kendini yeniden çalıştırır."""
    try:
        import graphify  # noqa: F401
        import networkx  # noqa: F401
        return
    except ImportError:
        pass
    kok = os.path.dirname(os.path.dirname(BURASI))
    py = os.environ.get("GRAF_PYTHON") or os.path.join(kok, ".venv", "bin", "python")
    # venv python'u sistem python'una sembolik bağdır; yol karşılaştırması yerine tek seferlik işaret kullan
    if os.path.exists(py) and not os.environ.get("GRAF_YENIDEN"):
        os.environ["GRAF_YENIDEN"] = "1"
        os.execv(py, [py, os.path.abspath(__file__)] + sys.argv[1:])
    print("graphify bulunamadı. Kurulum (sahibi, bir kez): python3 -m venv .venv && "
          f".venv/bin/pip install graphifyy=={SABIT_SURUM}   (ya da GRAF_PYTHON=<python yolu>)")
    sys.exit(2)


def main():
    graphify_yukle()
    import importlib.metadata
    import networkx as nx
    from graphify.analyze import god_nodes, surprising_connections
    from graphify.cluster import cluster, label_communities_by_hub
    from graphify.export import to_json
    from graphify.exporters.html import to_html

    sys.path.insert(0, BURASI)
    import yscommon as yc

    as_json = "--json" in sys.argv[1:]
    kok = yc.kok_bul()
    surum = importlib.metadata.version("graphifyy")
    uyarilar = []
    if surum != SABIT_SURUM:
        uyarilar.append(f"graphifyy {surum} kurulu, sınanan sürüm {SABIT_SURUM}; çıktı farklı olabilir")

    # ham notlar (01-gelen) grafa girmez: geçici ve güvenilmeyen içerik, bağ üretmesin (T-012)
    sayfalar = [(y, fm, g) for y, fm, g, h in yc.sayfalari_tara(kok) if fm and not h and fm.get("tur") != "ham"]
    G = nx.Graph()
    for y, fm, _ in sayfalar:
        G.add_node(yc.normalize_yol(y), label=fm.get("ad") or os.path.basename(y), source_file=y,
                   file_type="document", tur=fm.get("tur"), kat=fm.get("kat"), durum=fm.get("durum"))

    def bagla(a, b, iliski):
        if b in G and a != b and not G.has_edge(a, b):
            G.add_edge(a, b, relation=iliski, confidence="EXTRACTED", kaynak=a, hedef=b)

    for y, fm, govde in sayfalar:
        a = yc.normalize_yol(y)
        for h in fm.get("dayandigi") or []:
            if isinstance(h, str):
                bagla(a, yc.normalize_yol(h), "dayanir")
        if isinstance(fm.get("ust"), str):
            bagla(a, yc.normalize_yol(fm["ust"]), "ust")
    for y, fm, govde in sayfalar:
        a = yc.normalize_yol(y)
        for m in re.finditer(r"\[\[([^\]|#]+)", govde):
            bagla(a, yc.normalize_yol(m.group(1).strip()), "bahseder")

    topluluk = cluster(G) if G.number_of_edges() else {0: list(G.nodes)}
    etiket = label_communities_by_hub(G, topluluk)
    bilesenler = sorted(nx.connected_components(G), key=len, reverse=True)
    yetim = sorted(n for n in G if G.degree(n) == 0)
    zayif = sorted(n for n in G if G.degree(n) == 1 and G.nodes[n].get("tur") != "moc")
    merkez = god_nodes(G, top_n=5)
    sinir = surprising_connections(G, topluluk, top_n=5)

    cikti_dir = os.path.join(kok, "00-sistem", ".kosu", "graf")
    os.makedirs(cikti_dir, exist_ok=True)
    to_json(G, topluluk, os.path.join(cikti_dir, "graf.json"), force=True, community_labels=etiket)
    html_ok = to_html(G, topluluk, os.path.join(cikti_dir, "graf.html"), community_labels=etiket)

    ozet = {
        "graphifyy": surum, "dugum": G.number_of_nodes(), "kenar": G.number_of_edges(),
        "iliski": {r: sum(1 for *_, d in G.edges(data=True) if d["relation"] == r) for r in ("dayanir", "ust", "bahseder")},
        "bilesen": len(bilesenler),
        "kopuk_kumeler": [sorted(c) for c in bilesenler[1:]],
        "yetim": yetim, "zayif_bagli": zayif,
        "merkez": [{"sayfa": m["id"], "bag": m["degree"]} for m in merkez],
        "topluluk": [{"etiket": etiket.get(k, str(k)), "boyut": len(v)} for k, v in sorted(topluluk.items(), key=lambda kv: -len(kv[1]))],
        "sinir_asan": [{"kaynak": G.nodes[s["source"]]["source_file"] if s["source"] in G else s["source"],
                        "hedef": G.nodes[s["target"]]["source_file"] if s["target"] in G else s["target"],
                        "iliski": s.get("relation")} for s in _id_coz(G, sinir)],
        "uyari": uyarilar, "cikti": os.path.relpath(cikti_dir, kok), "html": bool(html_ok),
    }

    satirlar = [f"Graf: {ozet['dugum']} sayfa, {ozet['kenar']} bağ "
                f"(dayanır {ozet['iliski']['dayanir']}, üst {ozet['iliski']['ust']}, bahseder {ozet['iliski']['bahseder']}); "
                f"{ozet['bilesen']} bileşen, {len(topluluk)} topluluk. graphifyy {surum}, LLM yok."]
    for k in ozet["kopuk_kumeler"]:
        satirlar.append(f"  KOPUK KÜME ({len(k)}): " + ", ".join(k[:6]) + (" …" if len(k) > 6 else ""))
    if yetim:
        satirlar.append("  yetim: " + ", ".join(yetim[:8]))
    if zayif:
        satirlar.append(f"  zayıf bağlı ({len(zayif)}): " + ", ".join(zayif[:10]))
    satirlar.append("  merkez: " + ", ".join(f"{m['sayfa']} ({m['bag']})" for m in ozet["merkez"]))
    satirlar.append("  topluluklar: " + ", ".join(f"{t['etiket']} {t['boyut']}" for t in ozet["topluluk"]))
    for s in ozet["sinir_asan"]:
        satirlar.append(f"  sınır aşan: {s['kaynak']} —{s['iliski']}→ {s['hedef']}")
    for u in uyarilar:
        satirlar.append(f"  uyarı: {u}")
    satirlar.append(f"  çıktı: {ozet['cikti']}/graf.json, graf.html{'' if html_ok else ' (yazılmadı)'}, rapor.md")

    with open(os.path.join(cikti_dir, "rapor.md"), "w", encoding="utf-8") as f:
        f.write("# Graf raporu (graf.py; üretilmiş dosya, wiki sayfası değil)\n\n```\n" + "\n".join(satirlar) + "\n```\n")
    if as_json:
        print(json.dumps(ozet, ensure_ascii=False, indent=1))
    else:
        print("\n".join(satirlar))
    sys.exit(0)


def _id_coz(G, liste):
    """surprising_connections kaynak/hedefi etiketle döndürebilir; düğüm kimliğine çevir."""
    etiketten = {d.get("label"): n for n, d in G.nodes(data=True)}
    for s in liste:
        yield {**s, "source": s["source"] if s["source"] in G else etiketten.get(s["source"], s["source"]),
               "target": s["target"] if s["target"] in G else etiketten.get(s["target"], s["target"])}


if __name__ == "__main__":
    main()
