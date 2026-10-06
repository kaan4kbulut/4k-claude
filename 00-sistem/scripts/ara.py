#!/usr/bin/env python3
"""ara.py — wiki'de yerel arama (qmd sarmalayıcısı; HARITA'dan sonra ikinci adım).

Kullanım:
  python3 00-sistem/scripts/ara.py "<sorgu>"              anlamsal (vektör) arama, ilk 5 — varsayılan
  python3 00-sistem/scripts/ara.py "<sorgu>" --hibrit     BM25 + vektör + sorgu genişletme + yeniden sıralama (daha yavaş)
  python3 00-sistem/scripts/ara.py "<sorgu>" --kelime     yalnız BM25: tek terim/özel ad için (Türkçe cümlede çöker)
  python3 00-sistem/scripts/ara.py "<sorgu>" -n 10 --json
  python3 00-sistem/scripts/ara.py --yenile               koleksiyonları kur/güncelle ve gömmeleri üret (yeni sayfadan sonra)
  python3 00-sistem/scripts/ara.py --durum
  python3 00-sistem/scripts/ara.py --mcp                  MCP sunucusu (stdio; .mcp.json bunu çağırır)
Çıkış kodu: qmd'nin çıkış kodu; 2 qmd kurulu değil.

İlkeler:
  - qmd 2.8.3 proje içinde: .araclar/qmd (git dışı). Dizin ve modeller .araclar/onbellek altında; böylece sandbox
    (yazma yalnız proje klasörüne) içinden de --yenile çalışır. Modeller yalnız ilk --yenile'de HuggingFace'ten iner.
  - Gömme modeli Qwen3-Embedding-0.6B (Türkçe için; varsayılan embeddinggemma İngilizce ağırlıklı).
  - Dizine giren klasörler KOLEKSIYONLAR'dır. 01-gelen GİRMEZ: güvenilmeyen içerik yalnız okuyucu ajanla okunur
    (CLAUDE.md kural 8); arama sonucu olarak ana bağlama sızmamalı.
  - Arama sonucu bir ipucudur, kanıt değildir: bulunan sayfa açılıp okunur.
  - Kip seçimi ölçüme dayanır (ara-olcum.py, 20 Türkçe sorgu, 2026-10-07; 40-ic-ses/arastirma-notlari/qmd-turkce-isabet):
    vektör %75 isabet@1 / %90 isabet@3 / 4.5 sn; hibrit %50 / %90 / 7.5 sn; kelime %0 (ekler yüzünden).
"""
import os
import subprocess
import sys

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(os.path.dirname(BURASI))
QMD = os.path.join(KOK, ".araclar", "qmd", "node_modules", ".bin", "qmd")
GOMME = "hf:Qwen/Qwen3-Embedding-0.6B-GGUF/Qwen3-Embedding-0.6B-Q8_0.gguf"
KOLEKSIYONLAR = [
    ("sistem", "00-sistem", "Omurga: şema, harita, günlük, talimatlar, araştırma raporları"),
    ("insan", "10-insan", "Kat 1 eller: çıktılar, kaynaklar, araç kaydı"),
    ("sirket", "20-sirket", "Kat 2 örgütleme: roller, görev kartları, SOP, alan paketleri"),
    ("devlet", "30-devlet", "Kat 3 irade: anayasa, normlar, kararlar, kapılar, denetim"),
    ("icses", "40-ic-ses", "Kat 4 zihin: gözlemler, fikirler, yansımalar, kavramlar"),
    ("arsiv", "90-arsiv", "Dondurulmuş, geçersiz kılınmış sayfalar"),
]


def ortam():
    e = dict(os.environ)
    e["XDG_CACHE_HOME"] = os.path.join(KOK, ".araclar", "onbellek")
    e["XDG_CONFIG_HOME"] = os.path.join(KOK, ".araclar", "ayar")
    e["QMD_EMBED_MODEL"] = GOMME
    return e


def qmd(*arg, sessiz=False):
    r = subprocess.run([QMD, *arg], cwd=KOK, env=ortam(),
                       stdout=subprocess.DEVNULL if sessiz else None, stderr=subprocess.DEVNULL if sessiz else None)
    return r.returncode


# Günlük ve dizin dosyaları her şeyden bahsettiği için sonuçları kirletir (T-010 ölçümü); HARITA/GUNLUK ayrıca okunur.
IHMAL = {"sistem": ["sablonlar/**", ".kosu/**", "scripts/**", "sema/**", "GUNLUK.md", "TALIMATLAR.md", "DEGISIKLIKLER.md", "HARITA.md", "KARARLAR.md", "ILERLEME.md"]}
MODELLER = {
    "generate": "hf:tobil/qmd-query-expansion-1.7B-gguf/qmd-query-expansion-1.7B-q4_k_m.gguf",
    "rerank": "hf:ggml-org/Qwen3-Reranker-0.6B-Q8_0-GGUF/qwen3-reranker-0.6b-q8_0.gguf",
}


def _yaml_metin(v):
    return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"') + '"'


def ayar_yaz(gomme):
    """qmd ayarını (index.yml) tek kaynaktan yazar. qmd ayardaki models.embed'i ortam değişkeninden önce okur;
    ayar elle ya da qmd tarafından değişirse bir sonraki --yenile bunu geri yazar."""
    s = ["# ara.py tarafından üretilir; elle düzenleme bir sonraki --yenile'de ezilir.", "collections:"]
    for ad, klasor, baglam in KOLEKSIYONLAR:
        if not os.path.isdir(os.path.join(KOK, klasor)):
            continue
        s += [f"  {ad}:", f"    path: {_yaml_metin(os.path.join(KOK, klasor))}", '    pattern: "**/*.md"']
        if IHMAL.get(ad):
            s += ["    ignore:"] + [f"      - {_yaml_metin(i)}" for i in IHMAL[ad]]
        s += ["    context:", f'      "": {_yaml_metin(baglam)}']
    s += ["models:", f"  embed: {_yaml_metin(gomme)}"] + [f"  {k}: {_yaml_metin(v)}" for k, v in MODELLER.items()]
    yol = os.path.join(KOK, ".araclar", "ayar", "qmd", "index.yml")
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    eski = open(yol, encoding="utf-8").read() if os.path.exists(yol) else ""
    yeni = "\n".join(s) + "\n"
    with open(yol, "w", encoding="utf-8") as f:
        f.write(yeni)
    m = [l for l in eski.splitlines() if l.strip().startswith("embed:")]
    return bool(m) and gomme not in m[0]  # gömme modeli değişti mi


def yenile(gomme=None):
    degisti = ayar_yaz(gomme or GOMME)
    kod = qmd("update")
    return kod or (qmd("embed", "-f") if degisti else qmd("embed"))


def main():
    if not os.path.exists(QMD):
        print("qmd kurulu değil. Kurulum (sahibi, bir kez): npm install --prefix .araclar/qmd @tobilu/qmd@2.8.3")
        sys.exit(2)
    arg = sys.argv[1:]
    if not arg or arg[0] in ("-h", "--help"):
        print(__doc__.strip())
        sys.exit(0)
    if arg[0] == "--yenile":
        # --gomme <uri>: ölçüm için başka gömme modeliyle kur (varsayılan GOMME)
        sys.exit(yenile(arg[arg.index("--gomme") + 1] if "--gomme" in arg else None))
    if arg[0] == "--durum":
        sys.exit(qmd("status"))
    if arg[0] == "--mcp":
        os.execve(QMD, [QMD, "mcp"], ortam())
    kip = "search" if "--kelime" in arg else "query" if "--hibrit" in arg else "vsearch"
    kalan = [a for a in arg if a not in ("--kelime", "--hibrit")]
    if "-n" not in kalan:
        kalan += ["-n", "5"]
    # qmd sorgu genişletme satırlarını (vec:/hyde:) stderr'e basar; ajan bağlamını doldurmasın, yalnız hatada göster
    r = subprocess.run([QMD, kip, *kalan], cwd=KOK, env=ortam(), stderr=subprocess.PIPE, text=True)
    if r.returncode:
        sys.stderr.write("\n".join(r.stderr.strip().splitlines()[-8:]) + "\n")
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
