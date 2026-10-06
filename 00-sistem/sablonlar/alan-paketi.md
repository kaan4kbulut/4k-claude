---
id: YYYYMMDD-HHMM-slug
ad: slug
tur: alan-paketi
kat: 2
surum: 0.1
durum: taslak
amac: Bu alan paketi, ... alaninda sistemin dijital tarafi ucten uca yurutebilmesi icin gereken tum bilgiyi (kavramlar, roller, surecler, araclar, tedarikciler, mevzuat, riskler, maliyet, insan noktalari, metrikler) tek yerde toplar.
olusturma: YYYY-MM-DD
guncelleme: YYYY-MM-DD
yazar: claude
talimat: T-xxx
dayandigi: []
besledigi: []
ust: 20-sirket/MOC-sirket.md
kaynaklar: []
alindi: YYYY-MM-DD
guven: orta
kapsam: "<ne, kimin icin, cografya, olcek>"
yeniden_kontrol_kadansi: "ceyreklik (mevzuat, fiyat); aylik (araclar)"
insan_noktalari: []
etiketler: []
---

<!--
ALAN PAKETİ — 16 bölüm, hiçbiri boş kalmaz. Örnek: 20-sirket/alan-paketleri/3d-uretim.md.
- Mevzuat satırları tarihli ve VERIFIED/UNCONFIRMED etiketli; "mali müşavir teyidi gerekir" işareti.
- İnsan noktaları kataloğu zorunlu; görev kartları HP-id ile buraya bağlanır.
- Paket onaylanmadan (/kapi adhoc) bu alanda görev kartı açılmaz.
- Web'den gelen her olgu: URL + alindi + guven.
-->

# Alan paketi: <alan>

## Amaç
Bu alan paketi, … alanında sistemin dijital tarafı uçtan uca yürütebilmesi için gereken tüm bilgiyi tek yerde toplar.

## İçerik
### 1. Kimlik
Alan: … · Sürüm: 0.1 · Sahip: kaan · Kapsam: … · Oluşturma: …

### 2. Kavramlar ve sözlük
| Terim | Tanım (kendi kelimelerle) | Kaynak |
| --- | --- | --- |

### 3. Roller
| Rol | Kat | Sahip olduğu | Tek başına | Eskale | Ajan/İnsan |
| --- | --- | --- | --- | --- | --- |

### 4. Süreçler (uçtan uca akış)
| # | Adım | A/P/H | Araç | Kanıt | Hata dalı |
| --- | --- | --- | --- | --- | --- |
A = ajan yapar · P = ajan hazırlar, insan onaylar/yapar · H = insan yapar

### 5. Araçlar ve API'ler
| Yetenek | Araç / uç nokta / CLI | Kimlik doğrulama | Olgunluk | Sürüm | Yedek yol |
| --- | --- | --- | --- | --- | --- |

### 6. Tedarikçiler ve pazar yerleri
| Ad | Ne | Fiyat bandı (tarih) | Lisans / şart | Ajanın erişim yolu |
| --- | --- | --- | --- | --- |

### 7. Mevzuat ve vergi
| Konu | Hüküm | Durum | Kaynak | Tarih |
| --- | --- | --- | --- | --- |
Durum: VERIFIED / UNCONFIRMED. Vergi satırları için mali müşavir teyidi gerekir.

### 8. Riskler ve güvenlik
| Risk | Olasılık | Etki | Azaltma | Sahip |
| --- | --- | --- | --- | --- |

### 9. Maliyet modeli
Formül: … · BOM: … · Parametre dosyası: `…` · Hata tamponu: … · Platform komisyonu: …

### 10. İnsan noktaları kataloğu
| id | Tetik | İnsan ne yapar | Kanıt | SLA | Eskalasyon |
| --- | --- | --- | --- | --- | --- |
| HP-… | … | … | … | … | … |

### 11. Metrikler (KPI başlangıç seti)
- …

### 12. Bakım ve operasyon takvimi
| Ne | Tetik (zaman / kullanım) | Kim |
| --- | --- | --- |

### 13. Veri şeması
| Kayıt | Alanlar | Nerede |
| --- | --- | --- |

### 14. Test senaryoları
| # | Senaryo | Beklenen | (ret senaryosu mu) |
| --- | --- | --- | --- |

### 15. Bilinmeyenler / UNCONFIRMED
- (go-live öncesi doğrulanacaklar; kaynak nerede aranacak)

### 16. Değişiklik günlüğü ve yeniden kontrol
Kadans: … · Son kontrol: … · Sonraki: …

## Bağlar
### Dayandığı
- [[10-insan/kaynaklar/...]] — araştırma kaynakları
### Beslediği
- (roller, SOP'lar, görev kartları)
### Gelen

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | T-xxx | Oluşturuldu |
