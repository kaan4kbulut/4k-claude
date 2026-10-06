---
name: alan-paketi
description: Sistemin bilmediği bir alan (yeni iş kolu, teknoloji, sektör, mevzuat alanı) geldiğinde araştırma fazı açar ve 16 bölümlü Alan Paketi üretir; roller ve kurallar önerir. "Yapamıyoruz" yerine bu. Sahibi yeni bir alan açtığında, bir fikir mevcut paketlerin dışına taştığında kullan.
argument-hint: [alan-adi] [kapsam-cumlesi]
---

# /alan-paketi — bilinmeyen bir alanı sisteme öğretmek

Sistem bilmediği alanda şunu der: "Bunu henüz bilmiyorum; araştırma fazı açıyorum; şu noktalarda sen gerekeceksin." Paket onaylanmadan o alanda görev kartı açılmaz.

Mevcut paketler:
!`ls 20-sirket/alan-paketleri/ 2>/dev/null`

## 1. Talimat ve kapsam
- `TALIMATLAR.md` T-xxx: "X alanı için alan paketi"; kapı türü çift yönlü (araştırma geri alınabilir).
- Kapsam cümlesi sahibinden: ne, kimin için, hangi coğrafya, hangi ölçek (ör. "FDM/resin mikro-üretim, ≤10 yazıcı, B2C+B2B, TR").
- Sahibinin konuya hâkimiyetini sor: hiç / biraz / iyi. "Hiç" veya "biraz" ise önce **yönlendirme notu** (Danışman işlevi): konu üç cümleyle; bilmesi gereken ≤ 10 terim; alanın haritası; yaygın 2-3 yol ve kime uygun; vermesi gereken ilk 2-3 karar; önerilen küçük ve geri alınabilir ilk adım; sık yapılan hatalar; ≤ 3 soru.

## 2. Araştırma fazı
- Paralel alt ajanlar (model politikası: araştırma Sonnet, sentez Opus): kavramlar ve sözlük; araçlar/API'ler ve olgunluk; tedarikçiler ve pazar yerleri (fiyat bandı + tarih); mevzuat ve vergi (TR öncelikli, her satır tarihli ve VERIFIED/UNCONFIRMED); riskler ve güvenlik; maliyet modeli; gerçek dünya operasyonu (SOP, bakım, kalite); GitHub'da son 6 ayın ilgili projeleri.
- Her alt ajan ≤ 2.000 token özet + URL listesi döndürür. Ham çıktılar `10-insan/kaynaklar/` altına kaynak sayfası olarak girer (`tur: kaynak`, `alindi`, `guven`).
- Web'den gelen her olgu: URL + tarih + güven. Emin olunmayan: UNCONFIRMED.

## 3. Paketi yaz (`20-sirket/alan-paketleri/<alan>.md`, şablon `sablonlar/alan-paketi.md`)
16 bölüm, hiçbiri boş kalmaz:
1. Kimlik (ad, sürüm, sahip, kapsam cümlesi)
2. Kavramlar ve sözlük (her terim kanonik kaynağa bağlı)
3. Roller (sahibi + ajan rolleri; hangi katta)
4. Süreçler (uçtan uca akış; her adım A ajan yapar / P ajan hazırlar / H insan yapar; hata dalları)
5. Araçlar ve API'ler (uç nokta/CLI, kimlik doğrulama, olgunluk, sürüm, yedek yol)
6. Tedarikçiler ve pazar yerleri (fiyat bandı + tarih; lisans rejimi; ajanın erişim yolu)
7. Mevzuat ve vergi (tarihli; VERIFIED/UNCONFIRMED; kaynak; "mali müşavir teyidi gerekir" işareti)
8. Riskler ve güvenlik (azaltma + sahip)
9. Maliyet modeli (BOM, birim maliyet formülü, parametre dosyası)
10. İnsan noktaları kataloğu (id HP-xxx, tetik, insan ne yapar, kanıt, SLA, eskalasyon)
11. Metrikler (KPI başlangıç seti)
12. Bakım ve operasyon takvimi
13. Veri şeması (hangi kayıtlar tutulur)
14. Test senaryoları (kuru koşu; en az bir "ret" senaryosu)
15. Bilinmeyenler / UNCONFIRMED listesi (go-live öncesi doğrulanacaklar)
16. Değişiklik günlüğü ve yeniden kontrol kadansı

## 4. Rol ve kural önerisi
- Paketten çıkan rolleri `sablonlar/rol.md` ile taslak olarak öner (roller/ klasörüne yazma; kadro kapısı gerekir).
- Kata eklenecek kuralları (ör. "bu alanda lisansı NC olan model satılmaz") `/karar` ile öner; yürürlük sahibinin.
- `/kapi adhoc "X alan paketi onayı"`: sahibi paketi ve rolleri onaylar; sonra görev kartları açılabilir.

## 5. Kapanış
- HARITA, GUNLUK, `dayandigi/besledigi` (kaynak sayfaları ↔ paket). kontrol.py. BLUF brifing (DECISION).

## Örnek
`20-sirket/alan-paketleri/3d-uretim.md` 05 numaralı araştırmadan dolduruldu; şablonun nasıl dolduğunu görmek için ona bak.
