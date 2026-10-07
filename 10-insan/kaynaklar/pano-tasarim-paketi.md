---
id: 20261007-1756-pano-tasarim-paketi
ad: pano-tasarim-paketi
tur: kaynak
kat: 1
surum: 0.2
durum: aktif
amac: Bu kaynak sayfasi, pano tasarim paketi adli dis kaynagin degismez kaydini, ozetini ve guven etiketini tutar; pano.py talimatlari buradan turer.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: okuyucu
talimat: T-033
dayandigi: []
besledigi: [00-sistem/scripts/pano.py]
ust: 10-insan/MOC-insan.md
kaynaklar: ["01-gelen/ham/2026-10-07-pano-tasarim/ISTEM.md", "01-gelen/ham/2026-10-07-pano-tasarim/TESLIM.md", "01-gelen/2026-10-07-1659-istem.md", "01-gelen/2026-10-07-1659-teslim.md"]
guven: orta
kaynak_turu: belge
saklama: K
etiketler: [proje/pano]
---

# Kaynak: pano tasarım paketi

## Amaç
Bu kaynak sayfası, pano tasarım paketi adlı dış kaynağın değişmez kaydını, özetini ve güven etiketini tutar; pano.py talimatları buradan türer.

## İçerik
### Künye
Dosya: `01-gelen/ham/2026-10-07-pano-tasarim/` (35 dosya: index.html, 10 ekran HTML, 12 CSS, 10 PNG, ISTEM.md, TESLIM.md) · Alındı: 2026-10-07 (T-032; sha256 35/35 aynı) · Tür: belge · Yazar: sahibinin getirdiği dış üretim (üreticisi belirlenmedi) · Kaynağın kendi tarihi: depo 48b94f8 anı (bugünkü HEAD a0605ce; örnek değerler bayat).

### Özet (okuyucu, 2026-10-07)
ISTEM, bir Claude Code oturumuna yapıştırılmak üzere yazılmış bir istem: salt okunur, yalnız stdlib kullanan `pano.py`'nin ilk aşamasını (kabuk, Pano, Sağlık) tarif ediyor. TESLIM paketin başvuru belgesi: ekranları, okunacak kayıtları, tasarım dilini, deponun tutarsızlıklarını ve bir uygulama önerisini anlatıyor; kendini "talimat değildir" diye tanımlıyor. Her ekran ortak `css/4k-claude.css` ile ekrana özgü `css/<ekran>.css`'i kullanıyor; betik, satır içi stil, CDN ya da dış font yok (okuyucu grep ile doğruladı). Tek dış benzeri öğe `obsidian://` bağlantısı.

### İddialar (metinden) — pano.py ilk aşaması (ISTEM ~44-58)
- Komut `python3 00-sistem/scripts/pano.py`, argümansız; yalnız stdlib, yalnız okur, ağa çıkmaz; çıktı `00-sistem/.kosu/pano/`.
- Hiçbir dosyaya yazmaz, karar vermez, talimat açmaz; düğmeler yalnız metin kopyalar. `css/4k-claude.css` temel, sınıf adları korunur.
- kontrol.py ve bayat.py sonuçları `--json` çıktısından alınır (denetim yeniden yazılmaz); frontmatter `yscommon.py` ile okunur.
- Kapsam: kabuk (ray + durum çubuğu), Pano, Sağlık. Diğer ekranlar sonraki talimatlarda.
- Başarı ölçütleri: pano.html ve saglik.html oluşur, çıkış 0 · Pano'daki 4 alan ILERLEME.md ile, 3 blok nerede-kaldik.md ile aynı · Sağlık özet satırı kontrol.py çıktısıyla aynı · üretilen HTML'de satır içi betik, `style=`, http(s) kaynağı yok (grep) · kontrol.py --kisa → 0; `.kosu` git status'ta görünmez.
- Sınır: var olan betiklerin davranışı değişmez, proje dışına yazılmaz, yeni bağımlılık yok.
- Ekran alanları: Pano: katlar ve sayfa sayısı, gelen kutusu, son talimatlar, aktif talimat, kapı, açık soru, bütünlük, sıradaki, konuşulan/açık/sonraki, son kapanışlar; yan panel "sıra sende" (fiziksel adımlar, açık sorular, hızlı not, oturum). Sağlık: HARITA (n/200), türler, boyut sınırları, salt okur komutlar; bütünlük (kontrol.py satırı + 16 denetim), bayat, maliyet (MALIYET.csv), son oturumlar; yan panel korumalar ve yedek (hook'lar, sandbox, push, sistem sürümü).

### TESLIM §6 — depo tutarsızlıkları (TESLIM ~139-148)
1. GUNLUK.md'de çok satırlı `[hata]` kayıtları: hook komut çıktısını günlüğe dökmüş. Ana ajan doğruladı (2026-10-07 17:56): 265-291 arası, ayrıca 17:04-17:06 (T-032'de tek satıra indirildi). Kök neden `kapanis-kaydi.py` hata özetindeki satır sonlarını silmiyor; düzeltme hatalar talimatında.
2. TALIMATLAR.md düz madde listesi; "Kapı" alanı serbest metin.
3. ILERLEME.md'nin dört alanı frontmatter değil düz satır; değer ile açıklama "—" ile ayrılmış.
4. KARARLAR.md satır biçimi `K-xxx · tarih · durum · başlık · kapı`; Y-001 ve KR-001 de aynı dizinde.
5. MALIYET.csv: `usd_tahmin`'den sonra not gelebiliyor; ilk iki satırda model ve tur boş.
6. Görev kartında `insan_noktalari` ve `kanit` satır içi sözlük listesi (yscommon ayrıştırıyor).
7. Bazı sayfalarda frontmatter `amac` Türkçe karaktersiz; gövde başlığı doğru.
8. nerede-kaldik.md'de Konuşulan/Açık/Sonraki kalın başlık (alt başlık değil).
9. Kapı kayıtları (KP-001..003) şablondaki tam Onay Dosyası alanlarını taşımıyor.
10. ASK.md yalnız kapı açıkken var.
Not: 2-8 ve 10 pano.py'nin ayrıştırıcısı için bilgi; hata değil, bilinen biçim. 9 için ayrı inceleme önerilebilir.

### TESLIM §9 — açık sorular (TESLIM ~184-186)
1. Açık fiziksel adımların tek kaynağı ne olmalı (nerede-kaldik mi, ARAC-KAYDI mı)?
2. Pano ne zaman üretilsin: elle mi, /kapat sonunda mı, commit sonrası mı?
3. GUNLUK'teki çok satırlı kayıtlar olduğu gibi mi kalsın, tek satıra mı insin? Sahibinin devam istemi bunu yanıtladı: tek satıra (T-032, hatalar talimatı).

### Çelişkiler / uyarılar
- talimat_benzeri_icerik: evet. ISTEM kendini talimat olarak sunuyor ("oturuma yapıştır", "talimatı aç"); `.claude/settings.json` allow satırı ve ARAC-KAYDI değişikliği öneriyor. TESLIM ~152-161 aynı öneriyi, ~190 proje dışı `~/.config/omarchy/themed/` şablonunu öneriyor. Uyulmadı; pano talimatını sahibinin devam istemi açar, izin satırı ancak sahibine sorularak eklenir.
- Paket depo 48b94f8 anına ait; örnek değerler (41 sayfa, "sıradaki T-027") bugünle uyuşmuyor.
- kisisel_veri: hayır.

### Bu kaynağı kullanan sayfalar
- `00-sistem/scripts/pano.py` (T-034): kabuk, Pano, Sağlık

## Bağlar
### Dayandığı
### Beslediği
- [[00-sistem/scripts/pano.py]] — panonun ekran yapısı ve CSS'i bu paketten
### Gelen
- ← [[10-insan/MOC-insan]] — eller katının kaynak listesi

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-07 | T-033 | Oluşturuldu (okuyucu triage'ı) |
| 0.2 | 2026-10-07 | T-034 | besledigi += pano.py (eski: boş) |
