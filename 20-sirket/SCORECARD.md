---
id: 20261006-2241-scorecard
ad: scorecard
tur: referans
kat: 2
surum: 0.1
durum: aktif
amac: Haftalik 5-15 KPI'yi sahipli ve hedefli tutar; off-track olan gosterge Issues listesine duser ve haftalik L10'da ele alinir.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: [00-sistem/arastirma/06-sirket-operasyonlari.md]
besledigi: []
etiketler: [olcum]
---

# Scorecard

EOS/Traction: 5-15 haftalık sayı, her biri bir sahibe ve hedefe bağlı; hedef dışı kalan Issues'a düşer. Sistem göstergeleri pilotta hemen ölçülür; operasyon göstergeleri ilk gerçek işle açılır.

## Amaç
Haftalık 5-15 KPI'yi sahipli ve hedefli tutar; off-track olan gösterge Issues listesine düşer ve haftalık L10'da ele alınır.

## İçerik
### Sistem göstergeleri (pilottan itibaren)
| # | Gösterge | Sahip | Hedef | Kaynak |
| --- | --- | --- | --- | --- |
| S1 | Kanıtla kapanan talimat % | orkestratör | 100% | TALIMATLAR.md |
| S2 | kontrol.py hata sayısı (haftalık ortalama) | orkestratör | 0 | kontrol.py |
| S3 | Açık görev ortalama is_yasi (gün) | orkestratör | ≤ 7 | gorevler/ |
| S4 | Gelen kutusu 48 saatte işlenen % | zihin | ≥ 90% | 01-gelen |
| S5 | Haftalık token / USD | orkestratör | ≤ bütçe (MODEL-POLITIKASI) | MALIYET.csv |
| S6 | Stop hook engel sayısı (ilk denemede kanıtsız kapanış) | orkestratör | ↓ | GUNLUK [durdu] |
| S7 | Flip sayacı: gerekçesiz pozisyon değişikliği | zihin | 0 | MOC-ic-ses |
| S8 | Açık bulgu sayısı ve en eski bulgu yaşı | denetim | 0 / — | denetim/bulgular |

### Operasyon göstergeleri (ilk gerçek işle; alan paketine göre uyarlanır)
Teslimat: zamanında teslim %, iş emri çevrim süresi, WIP, geciken. Kalite: ilk seferde doğru %, NC/hafta, şikâyet, açık CAPA yaşı. Tedarik: tedarikçi zamanında %, stok-out, ROP altı kalem, stok günü. Satış: pipeline, teklif→sipariş %, ortalama sipariş. Finans: nakit (13 hafta min), katkı marjı %, DSO, kesilmemiş fatura, bütçe sapması. Sahip: planlanan vs gerçekleşen fiziksel saat, darboğaz kullanım %.

### Haftalık kayıt
| Hafta | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | Issues |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Issues (off-track)
- —

## Bağlar
### Dayandığı
- [[00-sistem/arastirma/06-sirket-operasyonlari]] — EOS scorecard, KPI başlangıç seti
### Beslediği
### Gelen
- ← [[20-sirket/MOC-sirket]] — haftalık KPI seti

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-06 | T-000 | Oluşturuldu |
