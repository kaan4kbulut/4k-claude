#!/usr/bin/env python3
"""canli.py — wiki sayfalarındaki web bağlantılarının canlılık denetimi (lychee; yalnız okur, hiçbir sayfayı düzeltmez).

Kullanım:
  python3 00-sistem/scripts/canli.py              denetim + özet (ölü bağlantılar sayfa sayfa)
  python3 00-sistem/scripts/canli.py --json
  python3 00-sistem/scripts/canli.py 30-devlet    yalnız verilen klasör(ler)
Çıkış kodu: 0 ölü bağlantı yok; 1 ölü var; 2 lychee yok.

İlkeler (CLAUDE.md kural 5: web'den gelen her olgu URL taşır):
  - lychee 0.24.2 (.araclar/lychee, sha256 doğrulandı, git dışı). Yalnız http(s) bağlantılar; wikilink'ler kontrol.py'nin işi.
  - 01-gelen DENETLENMEZ: güvenilmeyen içerikteki bir URL'ye istek atmak, saldırganın seçtiği adrese bağlanmak demektir.
    Şablonlar ve üretilmiş dosyalar (.kosu) da dışarıda.
  - Yalnız 404/410 "ölü"dür. 403/429 (bot engeli), 5xx, zaman aşımı ve TLS/HTTP2 ağ hataları "belirsiz": kaynak yok demek değil.
  - Ağ ister. Sandbox içinde her yeni alan adı onay ister; /haftalik'te sahibi `! python3 00-sistem/scripts/canli.py` ile çalıştırır.
  - Ölü bağlantı otomatik düzeltilmez: sayfa /degistir ile güncellenir; olgu doğrulanamıyorsa UNCONFIRMED işaretlenir.
"""
import json
import os
import subprocess
import sys

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(os.path.dirname(BURASI))
LYCHEE = os.path.join(KOK, ".araclar", "lychee", "lychee-x86_64-unknown-linux-gnu", "lychee")
VARSAYILAN = ["00-sistem/arastirma", "00-sistem/SISTEM.md", "00-sistem/SEMA.md", "10-insan", "20-sirket", "30-devlet", "40-ic-ses"]


def main():
    arg = sys.argv[1:]
    if not os.path.exists(LYCHEE):
        print("lychee kurulu değil (.araclar/lychee). Kurulum T-013 kaydında.")
        sys.exit(2)
    hedefler = [a for a in arg if not a.startswith("--")] or VARSAYILAN
    hedefler = [h for h in hedefler if not h.startswith("01-gelen") and os.path.exists(os.path.join(KOK, h))]
    komut = [LYCHEE, "--format", "json", "--no-progress", "--scheme", "https", "--scheme", "http",
             "--max-concurrency", "8", "--timeout", "20", "--max-retries", "1",
             "--exclude-path", "00-sistem/sablonlar", "--exclude-path", "00-sistem/.kosu",
             "--accept", "200..=299", *hedefler]
    r = subprocess.run(komut, cwd=KOK, capture_output=True, text=True, timeout=900)
    try:
        d = json.loads(r.stdout)
    except json.JSONDecodeError:
        print(f"lychee çıktısı okunamadı (çıkış {r.returncode}): {(r.stderr or r.stdout)[-400:]}")
        sys.exit(2)
    olu, belirsiz = {}, {}
    for dosya, liste in (d.get("error_map") or d.get("fail_map") or {}).items():
        for x in liste:
            url = x.get("url")
            st = x.get("status") or {}
            kod = st.get("code") if isinstance(st, dict) else None
            metin = (st.get("text") if isinstance(st, dict) else str(st)) or ""
            # Kesin ölü: 404/410 (sayfa yok). Sunucu hatası (5xx), bot engeli (403/429), zaman aşımı, TLS/HTTP2 ağ
            # hataları kaynağın yok olduğunu kanıtlamaz: belirsiz (T-013 ilk raporu: .gov.tr TLS zinciri, HTTP/2 hatası).
            kesin = kod in (404, 410)
            hedef = olu if kesin else belirsiz
            sayfa = os.path.relpath(dosya, KOK) if os.path.isabs(dosya) else dosya
            if any(y["url"] == url for y in hedef.get(sayfa, [])):
                continue  # aynı sayfada tekrar eden bağlantı
            hedef.setdefault(sayfa, []).append({"url": url, "durum": kod or metin[:80]})
    ozet = {"toplam": d.get("total"), "basarili": d.get("successful"), "olu": sum(map(len, olu.values())),
            "belirsiz": sum(map(len, belirsiz.values())), "olu_sayfa": olu, "belirsiz_sayfa": belirsiz,
            "hedef": hedefler}
    if "--json" in arg:
        print(json.dumps(ozet, ensure_ascii=False, indent=1))
    else:
        print(f"Bağlantı: {ozet['toplam']} denetlendi, {ozet['basarili']} canlı, {ozet['olu']} ölü, "
              f"{ozet['belirsiz']} belirsiz (403/429/5xx/ağ). 01-gelen denetlenmedi.")
        for sayfa, liste in sorted(olu.items()):
            for x in liste[:8]:
                print(f"  ÖLÜ  {sayfa}: {x['url']} ({x['durum']})")
        for sayfa, liste in sorted(belirsiz.items()):
            print(f"  belirsiz {sayfa}: " + ", ".join(f"{x['url']} ({x['durum']})" for x in liste[:3])
                  + (f" … +{len(liste) - 3}" if len(liste) > 3 else ""))
    sys.exit(1 if ozet["olu"] else 0)


if __name__ == "__main__":
    main()
