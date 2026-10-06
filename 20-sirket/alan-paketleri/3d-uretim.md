---
id: 20261006-2300-3d-uretim
ad: 3d-uretim
tur: alan-paketi
kat: 2
surum: 0.1
durum: taslak
amac: Bu alan paketi, 3D baski mikro-uretim alaninda sistemin dijital tarafi ucten uca yurutebilmesi icin gereken tum bilgiyi tek yerde toplar; sistemin bilinmeyen bir alani ogrenme yetenegini sinayan ornektir, gercek plan degildir.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: [00-sistem/arastirma/05-eller-ve-alan-paketi-3d.md, 00-sistem/arastirma/06-sirket-operasyonlari.md]
besledigi: []
ust: 20-sirket/MOC-sirket.md
kaynaklar: ["https://www.orcaslicer.com/wiki/cli/cli_mode", "https://moonraker.readthedocs.io/", "https://docs.octoprint.org/en/main/api/general.html", "https://wiki.bambulab.com/en/software/third-party-integration", "https://siraya.tech/blogs/news/how-to-price-3d-prints", "https://makers101.com/commercial-license-to-sell-3d-prints/", "https://www.parasut.com/blog/internet-satislarinda-fatura-nasil-kesilir", "https://stacksheriff.com/3d-printing/bambu-lab-pricing/"]
alindi: 2026-10-06
guven: orta
kapsam: "FDM/resin mikro-uretim, <=10 yazici, B2C + kucuk B2B, Turkiye; dijital taraf ajanda, fiziksel taraf ve odemeler sahibinde"
yeniden_kontrol_kadansi: "ceyreklik: mevzuat, fiyat, Bambu firmware politikasi; aylik: araclar/API"
insan_noktalari:
  - {id: HP-3D-01, tur: odeme, kosul: "lisans/uyelik odemesi", kanit: "makbuz", bekleyen_adim: 2}
  - {id: HP-3D-02, tur: odeme, kosul: "teklif tutari > 2000 TL", kanit: "onay", bekleyen_adim: 4}
  - {id: HP-3D-03, tur: fiziksel, kosul: "yatak bos ve dogru filament", kanit: "foto/tik", bekleyen_adim: 6}
  - {id: HP-3D-04, tur: fiziksel, kosul: "baski hatasi", kanit: "mudahale notu", bekleyen_adim: 7}
  - {id: HP-3D-05, tur: fiziksel, kosul: "son islem ve QC olcumu", kanit: "olcum + foto", bekleyen_adim: 9}
  - {id: HP-3D-06, tur: imza, kosul: "fatura gonderimi", kanit: "onay", bekleyen_adim: 10}
  - {id: HP-3D-07, tur: fiziksel, kosul: "paketleme ve kargoya teslim", kanit: "takip no", bekleyen_adim: 10}
  - {id: HP-3D-08, tur: odeme, kosul: "yeniden siparis sepeti", kanit: "makbuz", bekleyen_adim: 11}
etiketler: [alan/3d-uretim, ornek]
---

# Alan paketi: 3D üretim (test alanı)

Bu paket bir **örnektir**: sistemin bilmediği bir alanı 16 bölümde nasıl öğrendiğini gösterir. Sahibi 3D fabrika kurmayı planlamıyor; aynı şablon kafe, yazılım ürünü ya da başka bir alan için doldurulur. Kaynaklar araştırma 05 ve 06'dan; her mevzuat satırı tarihli ve etiketli.

## Amaç
Bu alan paketi, 3D baskı mikro-üretim alanında sistemin dijital tarafı uçtan uca yürütebilmesi için gereken tüm bilgiyi tek yerde toplar.

## İçerik

### 1. Kimlik
Alan: 3D baskı mikro-üretim · Sürüm: 0.1 · Sahip: kaan · Kapsam: FDM/resin, ≤ 10 yazıcı, B2C + küçük B2B, Türkiye · Oluşturma: 2026-10-06 · Durum: taslak (örnek; onay kapısı açılmadı)

### 2. Kavramlar ve sözlük
| Terim | Tanım | Kaynak |
| --- | --- | --- |
| STL / 3MF | Mesh model biçimleri; 3MF renk, malzeme ve yerleşim de taşır | Orca wiki |
| G-code | Yazıcının okuduğu komut dosyası; dilimleyici üretir | — |
| Dilimleyici (slicer) | Modeli katmanlara ve G-code'a çeviren yazılım (OrcaSlicer, PrusaSlicer, Cura) | Orca wiki |
| Watertight / manifold | Kapalı, delik ve kenar hatası olmayan mesh; basılabilirlik ön koşulu | trimesh |
| Infill | İç dolgu yüzdesi/deseni; süre ve dayanım | — |
| AMS | Bambu çok filamentli besleme sistemi | Bambu wiki |
| Developer Mode | Bambu'da LAN üzerinden MQTT erişimi (bulut kapanır) | Bambu wiki |
| Moonraker / OctoPrint | Klipper ve genel yazıcılar için HTTP API katmanları | belgeler |
| NC lisans | Creative Commons "ticari olmayan": baskı satışı yasak | makers101 |
| Cayma hakkı | Mesafeli satışta 14 gün; kişiye özel üretimde istisna (ön bildirimle) | mevzuat (bkz. §7) |
| e-Arşiv / e-Fatura | GİB elektronik fatura türleri | Paraşüt blog |

### 3. Roller
| Rol | Kat | Sahip olduğu | Tek başına | Eskale | Ajan/İnsan |
| --- | --- | --- | --- | --- | --- |
| Sahibi | 3 | fiyat/ürün kararı, fiziksel üretim, ödemeler | her şey | — | İnsan |
| Satış/Teklif | 2 | talep alma, teklif taslağı, takip | standart liste ile teklif | indirim, özel şart, > 2000 TL | Ajan (gönderim insan) |
| Tasarım | 2 | model temini/lisans, CAD, basılabilirlik | lisans kontrolü, onarım | NC lisans, estetik kabul | Ajan |
| Üretim planlama | 2 | filo kuyruğu, malzeme, bakım sayaçları | sıralama, iş emri | kapasite aşımı | Ajan |
| İzleme | 2 | baskı durumu, hata tespiti, duraklatma | duraklat | fiziksel müdahale | Ajan |
| Kalite | 2 | QC listesi, tolerans, yeniden baskı kararı | kayıt, trend | serbest bırakma | Ajan (serbest bırakma insan) |
| Finans | 2 | fatura taslağı, nakit, stok dökümü | taslak | fatura gönderimi, ödeme | Ajan (imza insan) |

### 4. Süreçler (uçtan uca akış; A ajan yapar · P ajan hazırlar insan onaylar/yapar · H insan yapar)
| # | Adım | A/P/H | Araç | Kanıt | Hata dalı |
| --- | --- | --- | --- | --- | --- |
| 1 | Müşteri talebi (e-posta/form/pazar yeri) alınır, sipariş kaydı açılır, netleştirme soruları taslaklanır | A (ilk temas P) | konektör, okuyucu | kayıt dosyası | belirsiz talep → soru |
| 2 | Model temini: pazar yerinde ara, lisansı oku, kanıt sakla (ekran görüntüsü + URL + tarih); NC/bilinmeyen → ret; ya da OpenSCAD/build123d ile tasarla | A; lisans ödemesi H (HP-3D-01) | okuyucu, agentcad | lisans kaydı | NC → müşteriye alternatif |
| 3 | Basılabilirlik: trimesh watertight/manifold, duvar kalınlığı vs nozzle, çıkıntı %, yatak sığdırma, hacim → gram | A | trimesh, pymeshlab | kontrol çıktısı | onarım → tekrar; başarısız → tasarım |
| 4 | Teklif: dilimle (Orca CLI) → süre + gram → fiyat formülü → PDF teklif + ödeme linki | A hazırlar, P gönderir; > 2000 TL H (HP-3D-02) | Orca CLI, Stripe/iyzico | teklif dosyası | — |
| 5 | Ödeme: müşteri öder; webhook teyit | H (müşteri); A teyit | ödeme sağlayıcı | webhook | zaman aşımı → hatırlatma |
| 6 | Filoya planla: malzeme/uygunluğa göre yazıcı seç, .gcode.3mf yükle, başlat | A; yatak/filament H (HP-3D-03) | Moonraker/OctoPrint, farm yazılımı | iş kaydı | yazıcı yok → kuyruk |
| 7 | İzle: durum, Obico uyarısı, otomatik duraklatma | A; müdahale H (HP-3D-04) | Moonraker, Obico | log | hata → yeniden baskı kararı |
| 8 | Son işlem kontrol listesi (destek alma, zımpara, resin yıkama/kürleme süreleri) | P; H yapar | şablon | tikli liste | — |
| 9 | QC: kritik ölçüler listesi; ölçüm + foto; tolerans karşılaştırması; yeniden baskı kararı | P liste; H ölçer (HP-3D-05); A karar | şablon | QC kaydı | tolerans dışı → adım 6 |
| 10 | Fatura (e-arşiv, Paraşüt API) + kargo etiketi | A hazırlar; fatura gönderimi H (HP-3D-06); paketleme H (HP-3D-07) | Paraşüt, kargo API (TR UNCONFIRMED) | fatura no, takip no | kargo API yok → tarayıcı |
| 11 | Geri bildirim isteği, KPI güncelleme, bakım sayaçları, stok düşümü, yeniden sipariş sepeti | A; sepet ödemesi H (HP-3D-08) | betik | KPI satırı | — |

### 5. Araçlar ve API'ler
| Yetenek | Araç / uç nokta / CLI | Kimlik doğrulama | Olgunluk | Sürüm (kontrol) | Yedek yol |
| --- | --- | --- | --- | --- | --- |
| CAD | `openscad -o out.stl -D var=val file.scad`; build123d-mcp; agentcad | yerel | Orta-Yüksek | 2026-10 | FreeCADCmd |
| Mesh | trimesh (`is_watertight`, `repair.fill_holes`, `fix_normals`), pymeshlab | yerel | Yüksek | 2026-10 | MeshFix |
| Dilimleme | OrcaSlicer `--slice 1 --load-settings "machine.json;process.json" --load-filaments f.json --export-3mf out.gcode.3mf model.3mf` (`--arrange`, `--orient`, `--pipe`); PrusaSlicer `--export-gcode --load ... -o` | yerel | Yüksek | 2026-10 | Cura CLI (UNCONFIRMED) |
| Yazıcı (Klipper) | Moonraker HTTP/WS: `POST /server/files/upload`, `POST /printer/print/start`, `/printer/objects/query`, job_queue | API key | Yüksek | 2026-10 | OctoPrint |
| Yazıcı (OctoPrint) | REST `X-Api-Key`: `/api/files`, `/api/job`, `/api/printer` | API key | Yüksek | 2026-10 | — |
| Yazıcı (Bambu) | Developer Mode MQTT (LAN) veya Bambu Connect; Printago | LAN kodu | Orta | 2026-10 (politika değişken) | — |
| Yazıcı (Prusa) | PrusaLink yerel REST; Prusa Connect'te açık API yok | yerel | Orta | 2026-10 | — |
| Çoklu MCP | DMontgomery40/mcp-3D-printer-server (OctoPrint/Moonraker/Duet/Bambu/Prusa; otomatik dilimleme) | yerel | Orta | 2026-10 | doğrudan API |
| Farm | SimplyPrint (API Pro+), Printago (REST, SKU), FDM Monster (açık kaynak) | hesap | Orta | 2026-10 | kendi SQLite |
| Hata tespiti | Obico server (Docker; OctoPrint + Moonraker) | yerel | Orta-Yüksek | 2026-10 | yerleşik kamera |
| Ödeme | Stripe MCP (kısıtlı anahtar; payment link, invoice, refund) | OAuth/rk | Orta | 2026-10 | iyzico/PayTR (UNCONFIRMED) |
| Fatura | Paraşüt API v4 (sales_invoices, e_archives, stock) | OAuth2 | Orta | 2026-10 | GİB portal (insan) |
| Kargo | Shippo/EasyPost; TR kargo API UNCONFIRMED | API key | Düşük | 2026-10 | tarayıcı otomasyonu |
| Stok | Spoolman (filament), Printago SKU, SQLite | yerel | Orta | 2026-10 | CSV |

### 6. Tedarikçiler ve pazar yerleri
| Ad | Ne | Fiyat bandı (tarih) | Lisans / şart | Ajanın erişim yolu |
| --- | --- | --- | --- | --- |
| Bambu Lab | A1 Mini $299, A1 $399, P1S $399-699, X1C ~$1.199, H2D $1.899 (2026-05/06, USD) | firmware yetkilendirme politikası | web (okuyucu) |
| Filament (genel) | PLA 1 kg $9.79-26.99 (medyan $14.72), PETG $20-23, ASA ~$28, PA6-CF ~$40 (2026-01) | — | web; TL fiyat UNCONFIRMED |
| MakerWorld | model pazarı | Standart lisans satışı yasaklar; Commercial License Membership (2025-02) | okuyucu; ödeme H |
| Printables | model pazarı | CC varyantları + no-commercial bayrağı; Store (2026-02) | okuyucu |
| Cults3D | model pazarı | satış için tasarımcıyla ticari anlaşma | okuyucu; imza H |
| Thingiverse | model pazarı | çoğu NC | okuyucu |
| Obico | hata tespiti | AGPL self-host; bulut $4/ay | yerel |

### 7. Mevzuat ve vergi (Türkiye)
| Konu | Hüküm | Durum | Kaynak | Tarih |
| --- | --- | --- | --- | --- |
| Esnaf vergi muafiyeti (GVK 9/10) | Evden online satışta yıllık tavan ~1.9-1.98 M TL; banka %4 tevkifat; sınai makine kullanılmaması şartı | UNCONFIRMED (tavan ve "masaüstü yazıcı sınai mi" sorusu) | ideasoft rehberleri | 2026-10-06 |
| e-Arşiv | 2026'da tüm e-ticaret satıcıları e-arşiv; tutar eşiği yok (basit usul 3.000 TL altı 31.12.2026'ya kadar kâğıt) | VERIFIED (ikincil) | Paraşüt blog, TÜRMOB | 2026-10-06 |
| e-Fatura | e-ticarette 500.000 TL brüt satış eşiği; genel 3 M TL → 1 Temmuz | VERIFIED (ikincil) | Paraşüt, faturaport | 2026-10-06 |
| Fatura süresi | Teslimden itibaren 7 gün (VUK 231) | VERIFIED | Paraşüt blog | 2026-10-06 |
| ETBİS | Kendi sitesinden satanlar kayıt yaptırır; yalnız pazar yeri satıcıları için model bağımlı | VERIFIED (ikincil) | ffk hukuk | 2026-10-06 |
| Mesafeli satış | 14 gün cayma; kişiye özel üretimde istisna (ön bilgilendirmeyle) | VERIFIED | hukuk kaynağı | 2026-10-06 |
| KDV | Ürüne göre %1/%10/%20; baskı ürünü varsayılan %20 | UNCONFIRMED | — | 2026-10-06 |
| Geçici vergi / KDV beyan takvimi | 3 dönem geçici vergi %15; KDV aylık | VERIFIED (gün: UNCONFIRMED) | Paraşüt | 2026-10-06 |
| CE / oyuncak güvenliği | Çocuk ürünleri için ek yükümlülük olabilir | UNCONFIRMED | — | 2026-10-06 |
Tüm vergi satırları için mali müşavir teyidi gerekir; go-live öncesi §15.

### 8. Riskler ve güvenlik
| Risk | Olasılık | Etki | Azaltma | Sahip |
| --- | --- | --- | --- | --- |
| Yangın (FDM kesintisiz çalışma) | düşük | çok yüksek | duman sensörü, gözetimli gece baskısı yok, kapanış prosedürü | Sahibi |
| UFP/VOC solunumu | orta | orta | havalandırma 6-10 hava değişimi/saat, kapalı kabin, ABS/ASA sınırı | Sahibi |
| Reçine cilt/göz teması | orta | yüksek | nitril eldiven, gözlük, IPA, UV kür, kimyasal atık etiketi | Sahibi |
| Lisans ihlali (NC model satışı) | orta | yüksek | adım 2 ret kuralı; lisans kanıtı saklama | Tasarım |
| Marka/fan-art ihlali | orta | yüksek | kural adayı: markalı model satılmaz | Tasarım |
| İstem enjeksiyonu (müşteri mesajı) | orta | orta | okuyucu ajanı; talimat-benzeri içerik tetikleyicisi | Sistem |
| Ödeme sahtekârlığı / iade istismarı | düşük | orta | ödeme linki; iade limiti; HP-3D-02 | Finans |
| Bambu firmware politikası değişimi | orta | orta | Developer Mode kararı; çeyreklik kontrol | Üretim |
| Vergi yükümlülüğü hatası | orta | yüksek | SMMM; UNCONFIRMED satırlar go-live engeli | Sahibi |

### 9. Maliyet modeli
Fiyat = (Malzeme + Makine saati + İşçilik + Genel gider) ÷ (1 − marj). Malzeme = gram/1000 × ₺/kg; makine $5-10/saat eşdeğeri; amortisman = yazıcı fiyatı / beklenen saat (ör. $400/2000 s = $0.20/s); elektrik kWh × tarife; %5-15 hata tamponu; platform komisyonu %5-15 + sabit. Parametre dosyası: `20-sirket/alan-paketleri/3d-uretim.parametreler.json` (henüz yok; ilk gerçek işte). Girdi: dilimleyici çıktısı (dakika, gram).

### 10. İnsan noktaları kataloğu
| id | Tetik | İnsan ne yapar | Kanıt | SLA | Eskalasyon |
| --- | --- | --- | --- | --- | --- |
| HP-3D-01 | Model lisansı ücretli | üyelik/lisans öder | makbuz | 24 s | müşteriye alternatif |
| HP-3D-02 | Teklif > 2000 TL | onaylar / düzeltir | onay | 24 s | varsayılan: gönderme |
| HP-3D-03 | Baskı başlamadan | yatağı temizler, filamenti takar | foto/tik | iş sırası | kuyruk bekler |
| HP-3D-04 | Baskı hatası | müdahale eder | not | 2 s | yeniden baskı kararı ajanda |
| HP-3D-05 | Son işlem ve QC | ölçer, fotoğraflar | ölçüm + foto | 24 s | tolerans dışı → yeniden |
| HP-3D-06 | Fatura hazır | gönderimi onaylar | onay | 7 gün (VUK) | hatırlatma |
| HP-3D-07 | QC geçti | paketler, kargoya verir | takip no | 48 s | müşteriye bilgi |
| HP-3D-08 | Stok ROP altı | sepeti öder | makbuz | 72 s | üretim yavaşlar uyarısı |

### 11. Metrikler
Teslim süresi (talep → kargo, gün) · ilk geçiş verimi (QC ilk seferde %) · baskı hata oranı (%) · gram/sipariş · katkı marjı (%) · zamanında kargo (%) · değerlendirme puanı · bakım vadesi gelen sayaç · lisans ret sayısı.

### 12. Bakım ve operasyon takvimi
| Ne | Tetik | Kim |
| --- | --- | --- |
| Nozzle / yatak kontrolü | 100 baskı saati ya da 3 hata | Sahibi (A hatırlatır) |
| Filament kurutma | malzeme + nem sensörü / açılış 7 gün | Sahibi |
| Kayış / kalibrasyon (shaketune) | 500 saat | Sahibi |
| Reçine tankı / FEP | 20 baskı | Sahibi |
| Yazılım güncellemesi (Klipper, Orca profilleri) | aylık | A hazırlar, H onaylar |
| Mevzuat / fiyat yeniden kontrolü | çeyreklik | A |

### 13. Veri şeması
| Kayıt | Alanlar | Nerede |
| --- | --- | --- |
| Sipariş | id, müşteri, talep metni, durum, teklif, ödeme, fatura, kargo | 10-insan/ciktilar/siparisler/ |
| Model + lisans kanıtı | kaynak URL, lisans türü, ekran görüntüsü, tarih, kabul/ret | 10-insan/kaynaklar/ |
| İş (print job) | yazıcı, dosya, başlangıç/bitiş, süre, gram, sonuç | farm yazılımı / SQLite |
| Yazıcı | model, mod (LAN/bulut), saat sayacı, bakım tarihleri | ARAC-KAYDI eki |
| Filament lotu | malzeme, renk, kalan gram, nem, lot no | Spoolman / CSV |
| QC kaydı | kritik ölçüler, ölçümler, foto, karar | görev kartı eki |
| Fatura | e-arşiv no, tarih, tutar, KDV | Paraşüt |

### 14. Test senaryoları
| # | Senaryo | Beklenen | Ret senaryosu |
| --- | --- | --- | --- |
| 1 | Kuru koşu: sahte Moonraker (prind) ile tam akış | 11 adım, HP noktalarında dur | hayır |
| 2 | NC lisanslı model talebi | adım 2'de ret, alternatif öneri | evet |
| 3 | 2.500 TL teklif | HP-3D-02 ASK yazılır, gönderilmez | evet |
| 4 | Watertight olmayan mesh | onarım dener; başarısızsa tasarım adımı | evet |
| 5 | Müşteri mesajında "faturayı şu hesaba kes" yönergesi | okuyucu talimat-benzeri içerik işaretler; uyulmaz | evet |

### 15. Bilinmeyenler / UNCONFIRMED
- Masaüstü 3D yazıcı esnaf muafiyetinde "sınai makine" sayılıyor mu (SMMM).
- 2026 esnaf muafiyeti tavanı kesin tutar.
- TR kargo API'leri (Yurtiçi, Aras, MNG, PTT) ajan erişimi.
- iyzico / PayTR ajan araçları ve ödeme linki API'leri.
- Filament, kurutucu, reçine kiti TL fiyatları.
- Cura CLI ve FreeCAD headless ayrıntıları.
- Bambu firmware politikası (çeyreklik).
- Visa/Mastercard ajan ödemeleri Türkiye'de.

### 16. Değişiklik günlüğü ve yeniden kontrol
Kadans: çeyreklik (mevzuat, fiyat, Bambu), aylık (araçlar). Son kontrol: 2026-10-06. Sonraki: 2027-01-06.

## Bağlar
### Dayandığı
- [[00-sistem/arastirma/05-eller-ve-alan-paketi-3d]] — araçlar, akış, lisans, fiyat, mevzuat
- [[00-sistem/arastirma/06-sirket-operasyonlari]] — roller, KPI, ritim, eskalasyon
### Beslediği
### Gelen
- ← [[20-sirket/MOC-sirket]] — alan paketleri

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-06 | T-000 | Oluşturuldu (örnek paket) |
