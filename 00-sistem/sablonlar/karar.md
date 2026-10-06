---
id: YYYYMMDD-HHMM-slug
ad: slug
tur: karar
kat: 3
surum: 0.1
durum: onerildi
amac: Bu karar kaydi, ... konusunda ... secenegini neden sectigimizi, alternatifleri ve dogrulama yolunu kalici olarak tutmak icin var.
olusturma: YYYY-MM-DD
guncelleme: YYYY-MM-DD
yazar: claude
talimat: T-xxx
dayandigi: []
besledigi: []
ust: 30-devlet/MOC-devlet.md
kapi: cift-yonlu
karar_veren: kaan
danisilan: []
bilgilendirilen: []
beklenen_sonuc_olasilik: 70
gozden_gecir: YYYY-MM-DD
yerine_gecti: 
yerine_gecen: 
saklama: S
etiketler: []
---

<!--
KARAR = MADR 4.0 mini + Farnam Street karar günlüğü + DACI (tek Approver).
- durum: onerildi → kabul (sürüm 1.0; sahibi onayı; tek yönlüyse /kapi şart) → yerine-gecildi (yerine_gecen dolu) | reddedildi.
- Kabulden sonra gövde DÜZENLENMEZ. Değişiklik = yeni karar + supersede.
- Seçenekler ≥2; "hiçbir şey yapmama" dahil. Her seçenek: artı, eksi, maliyet/token, risk.
- beklenen_sonuc_olasilik: % olarak; gozden_gecir tarihinde tahmin vs gerçek karşılaştırılır (kalibrasyon).
- KARARLAR.md'ye dizin satırı zorunlu.
- Bu yorum bloğunu sil.
-->

# Karar K-xxx: <başlık>

## Amaç
Bu karar kaydı, … konusunda … seçeneğini neden seçtiğimizi, alternatifleri ve doğrulama yolunu kalıcı olarak tutmak için var.

## İçerik
### Bağlam ve problem
(3-5 cümle: neyi çözüyoruz, neden şimdi, hangi kısıtlar)

### Karar sürücüleri
- (kriter 1: sahibinin ilkesi / kısıt / maliyet / risk toleransı)
- (kriter 2)

### Seçenekler
| # | Seçenek | Artı | Eksi | Maliyet / token | Risk |
| --- | --- | --- | --- | --- | --- |
| A | … | … | … | … | … |
| B | … | … | … | … | … |
| 0 | Hiçbir şey yapma | … | … | … | … |

### Karar
**… yapacağız**, çünkü … . (seçilen: A)

### Beklenen sonuç
… olacak; olasılık %70; gerekçe: … . (gozden_gecir tarihinde kontrol)

### Sonuçlar
- İyi: …
- Kötü: …
- Nötr / bilinmeyen: …

### Doğrulama
Uygunluk nasıl kontrol edilir: (komut / gözden geçirme / metrik) · ne zaman: (tarih) · kim: (rol)

### Kapı ve roller
kapi: cift-yonlu | tek-yonlu (tek yönlüyse KP-xxx: [[30-devlet/kapilar/KP-xxx-...]]) · karar veren: kaan · danışılan: … · bilgilendirilen: …

### Karar günlüğü notu (opsiyonel)
Zihinsel durum / zaman: … · Bu kararı bilmeden verirsek ne olur: …

## Bağlar
### Dayandığı
- [[40-ic-ses/fikirler/F-xxxx-...]] — bu kararı doğuran fikir
### Beslediği
- [[20-sirket/gorevler/G-xxx-...]] — bu karardan çıkan görev
### Gelen

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | T-xxx | Oluşturuldu (onerildi) |
