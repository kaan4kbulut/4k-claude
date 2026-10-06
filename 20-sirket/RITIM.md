---
id: 20261006-2242-ritim
ad: ritim
tur: referans
kat: 2
surum: 0.1
durum: aktif
amac: Gunluk, haftalik, aylik, ceyreklik ve yillik operasyon ritmini; her toplantinin gundemini ve ajanin onceden hazirladiklarini belirler.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: [00-sistem/arastirma/06-sirket-operasyonlari.md, 00-sistem/arastirma/08-ic-ses-yontemleri.md]
besledigi: []
etiketler: [ritim]
---

# Ritim

EOS Level 10 ve Rockefeller Habits'ten; kısıt sahibinin fiziksel saatleridir (Kısıtlar Teorisi): her plan buna tabi kılınır. Ajan hazırlar, sahibi karar verir.

## Amaç
Günlük, haftalık, aylık, çeyreklik ve yıllık operasyon ritmini; her toplantının gündemini ve ajanın önceden hazırladıklarını belirler.

## İçerik
### Günlük (ajan hazırlar; sahibi 5-10 dk okur)
- Gelen kutusu triage (`/inbox-triage`); açık ASK varsa ilk sırada.
- Açık görevler: SLA/SLE kontrolü; fiziksel-adim-bekliyor olanların listesi = bugünün insan noktaları.
- Stok/tetik kontrolleri (alan paketi varsa); nakit pozisyonu (varsa).
- Huddle: dün bitti / bugün / engeller (3 madde).

### Haftalık L10 (60-90 dk; sesli; `/haftalik`)
Segue 5 · Scorecard 5 (SCORECARD.md on/off track) · Rocks 5 (çeyreklik öncelikler) · Başlıklar 5 · To-do 5 · IDS 60 (Issues: tespit-tartış-çöz) · Kapanış 5 (to-do özeti, kaskad mesaj, 1-10 puan). Ardından `/uyku tam`.

### Haftalık finans (ajan)
13 haftalık nakit tahmini güncelle (alan paketi varsa); vadesi gelen alacak/borç; vergi takvimi hatırlatması (geçici vergi, KDV) — mali müşavir teyidi ile.

### Aylık (yarım gün)
Bütçe vs gerçek; MALIYET.csv aylık toplam; tedarikçi puan kartı; NC/CAPA trendi; SOP gözden geçirme kuyruğu; karar günlüğü kalibrasyonu (`gozden_gecir` tarihi gelenler); `/uyku aylik`.

### Çeyreklik
Rocks kapanış/açılış; OKR puanlama; iç denetim (bir süreç; Denetim); FMEA/risk kaydı gözden geçirme; kural stoğu giyotin testi (yasal mı, gerekli mi, yararlı mı); MODEL-POLITIKASI fiyat/tazelik kontrolü; alan paketleri yeniden kontrol kadansı.

### Yıllık
Strateji / tek sayfa plan; Anayasa ve imza matrisi gözden geçirme (değişiklik yalnız sahibi); yıllık vergi takvimi (mali müşavir); arşiv süpürmesi.

### Zamanlı görevler (öneri; sahibi kurar)
| Görev | Sıklık | Komut |
| --- | --- | --- |
| Gelen kutusu triage | günlük 08:40 | `calistir.sh T-xxx "/inbox-triage hepsi" 15 0.5` |
| Uyku hafif | her gün 23:10 | `calistir.sh T-xxx "/uyku hafif" 15 1` |
| Uyku tam | pazar 20:10 | `calistir.sh T-xxx "/uyku tam" 30 3` |
| Bayat raporu | pazartesi 08:50 | `python3 00-sistem/scripts/bayat.py` |
Gözetimsiz koşuda onay sorulamaz; onay gerektiren adım ASK.md yazar ve durur.

## Bağlar
### Dayandığı
- [[00-sistem/arastirma/06-sirket-operasyonlari]] — EOS L10, Rockefeller ritmi, aylık/çeyreklik döngü
- [[00-sistem/arastirma/08-ic-ses-yontemleri]] — haftalık gözden geçirme ritüeli
### Beslediği
### Gelen
- ← [[20-sirket/MOC-sirket]] — ritim

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-06 | T-000 | Oluşturuldu |
