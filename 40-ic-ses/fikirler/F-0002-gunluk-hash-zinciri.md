---
id: 20261007-1946-gunluk-hash-zinciri
ad: f-0002-gunluk-hash-zinciri
tur: fikir
kat: 4
surum: 0.1
durum: taslak
amac: "Bu fikir, 'GUNLUK hash zinciri' onerisini kaydetmek ve olgunlastirmak icin var (merdiven 0, ham)."
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-047
dayandigi: []
besledigi: []
ust: 40-ic-ses/MOC-ic-ses.md
merdiven: 0
cynefin: belirlenmedi
guven: dusuk
kaynaklar: []
dokunus_sayisi: 1
son_dokunus: "2026-10-07"
kapi: belirlenmedi
etiketler: [hafif-yol]
---

# Fikir F-0002: GUNLUK hash zinciri

## Amaç
Bu fikir, 'GUNLUK hash zinciri' onerisini kaydetmek ve olgunlastirmak icin var (merdiven 0, ham).

## İçerik
### Tek cümle
Kaynak: 2026-10-07 YZ taraması (liste T-k). gunluk.py her satıra önceki satırın kısa hash'ini eklesin, kontrol.py zinciri doğrulasın: salt-ekleme kuralının teknik kanıtı olur. Engel: GUNLUK'e altı hook (kapanis-kaydi, ayar-denetimi, durus-kapisi, butce-bekcisi, model-bekcisi, yikici-koruma dışı) kendi satırını doğrudan yazıyor; zincir için hepsi ortak bir yazıcıya (yscommon ya da gunluk.py içe aktarımı) geçmeli ve eşzamanlı yazımda kilit gerekir. Ayrıca T-032/T-036'da GUNLUK geçmişi bilerek düzeltildi (çok satırlı kayıtlar): zincir bu tür meşru düzeltmeyi de 'kırık' sayar, düzeltme satırı biçimi gerekir. Git geçmişi zaten değişmezlik kanıtı veriyor (GitHub'a push); zincirin ek değeri git dışı düzenlemeyi yakalamak. Önerilen sıra: önce hook yazımlarını tek yazıcıda topla, sonra zincir.

### Çerçeve (üçüncü şahıs)
belirlenmedi

### Neden şimdi
belirlenmedi

### Kanıt
- henüz yok
### Karşı-kanıt
- aranmadı

### Açık sorular (M3 için ≤2)
- belirlenmedi

## Bağlar
### Dayandığı
### Beslediği
### Gelen
- ← [[40-ic-ses/MOC-ic-ses]] — merdiven tablosu, M0

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-07 | T-047 | Oluşturuldu (hafif yol, KR-001) |
