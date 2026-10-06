---
id: 20261007-0152-k-004-yazici-pazar-arastirmasi
ad: k-004-yazici-pazar-arastirmasi
tur: karar
kat: 3
surum: 0.1
durum: onerildi
amac: Bu karar kaydi, yazici isi fikri (F-0001) icin yazici satin almadan once pazar arastirmasi yapilmasi secenegini neden onerdigimizi, alternatifleri ve dogrulama yolunu kalici olarak tutmak icin var.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-002
dayandigi: [40-ic-ses/fikirler/F-0001-yazici-isi-fikri.md]
besledigi: [20-sirket/gorevler/G-001-yazici-pazar-arastirmasi.md]
ust: 30-devlet/MOC-devlet.md
kapi: cift-yonlu
karar_veren: kaan
danisilan: [claude]
bilgilendirilen: []
beklenen_sonuc_olasilik: 70
gozden_gecir: 2026-11-07
saklama: S
etiketler: [karar/is-fikri, proje/yazici]
---

# Karar K-004: Yazıcı işinde önce pazar araştırması

## Amaç
Bu karar kaydı, yazıcı işi fikri (F-0001) için yazıcı satın almadan önce pazar araştırması yapılması seçeneğini neden önerdiğimizi, alternatifleri ve doğrulama yolunu kalıcı olarak tutmak için var.

## İçerik
### Bağlam ve problem
Kaan bir yazıcı satın alıp onunla para kazandıran küçük bir iş kurmak istiyor (F-0001, merdiven 1). Yazıcının türü (3D mi, kâğıt/baskı mı) ve kime ne satılacağı henüz belirlenmedi; F-0001'in iki açık sorusu bunlar. Fikir Cynefin'de `kompleks` atandı (sahibi onayı bekliyor): talep ve müşteri tepkisi önceden analizle bilinemez, küçük denemelerle öğrenilir. Yazıcı alımı para harcayan ve kolay geri dönmeyen bir adım; ne alınacağı belli değilken alım yanlış türe para bağlama riski taşır.

### Karar sürücüleri
- Anayasa Madde 13: kaynak (para, zaman) kıttır; geri dönüşü pahalı adım bilgi olmadan atılmaz.
- Anayasa Madde 12: olgunlaşmamış fikir (M1) devlete iş emri olarak gitmez; önce kanıt toplanır.
- Fiziksel adımlar ve ödemeler sahibinindir (Madde 5); araştırma dijital olarak sistemin işidir.
- Bilinmeyen alanda "yapamıyoruz" denmez; araştırma fazı açılır (Madde 4). 3D üretim için bir alan paketi zaten var (`20-sirket/alan-paketleri/3d-uretim`), ama F-0001 bunun aynı şey olduğunu varsaymıyor.

### Seçenekler
| # | Seçenek | Artı | Eksi | Maliyet / token | Risk |
| --- | --- | --- | --- | --- | --- |
| A | Önce pazar araştırması: yazıcı türü, hedef müşteri, rakip fiyatları, talep işaretleri; sonra alım kararı | Yanlış türe para bağlanmaz; F-0001'in açık soruları kanıtla cevaplanır; merdivende M2'ye gerekli "kaynaklar, alternatifler" alanları dolar | Gelir başlangıcı gecikir; araştırma da kesin cevap vermeyebilir (kompleks alan) | Düşük para; araştırma alt ajanı ~2 USD (MODEL-POLITIKASI) ve sahibin zamanı | Araştırma uzayıp karar ertelenebilir; zaman kutusu gerekir |
| B | Hemen bir yazıcı al, deneyerek öğren | En hızlı öğrenme; kompleks alanda "dene-gör" ile uyumlu | Tür belli değilken alım; para geri dönmeyebilir | Yazıcı bedeli (belirlenmedi) | Yanlış tür, atıl cihaz |
| 0 | Hiçbir şey yapma (fikri park et) | Maliyet yok | Fikir ilerlemez, sahibinin isteği karşılanmaz | Yok | Fırsat kaybı |

### Karar (öneri)
**Yazıcı almadan önce zaman kutulu bir pazar araştırması yapacağız**, çünkü yazıcı türü ve müşteri belli değilken alım geri dönüşü pahalı bir adım; araştırma ucuz ve fikri merdivende kanıtla ilerletir. (seçilen: A). Kompleks alana uygun olarak araştırma, B'deki "küçük deneme" fikrini dışlamaz: araştırma sonunda en ucuz deneme (ör. ikinci el ya da kiralık cihazla tek ürün denemesi) önerilebilir.

Bu kayıt **önerildi** durumundadır; sahibi onaylamadan `kabul` olmaz ve buna dayanan görev kartı (G-001) başlamaz.

### Beklenen sonuç
Araştırma bir oturumluk zaman kutusunda yazıcı türü ve ilk müşteri kitlesi için en az iki seçenek ve karşılaştırma üretir; olasılık %70; gerekçe: türü belirsiz bir fikirde ilk tur araştırma genelde seçenekleri daraltır ama kesin talep kanıtı vermez.

### Sonuçlar
- İyi: alım kararı kanıta dayanır; F-0001 M2'ye çıkabilir.
- Kötü: gelir başlangıcı gecikir.
- Nötr: araştırma sonucu fikri öldürebilir; bu da geçerli bir çıkış.

### Doğrulama
2026-11-07'de gözden geçirilir: G-001 kapandı mı, F-0001'in iki açık sorusu cevaplandı mı, alım kararı verildi mi. Kanıt: G-001 kanıt tablosu ve F-0001 merdiven alanı.

### Kapı ve roller
kapi: cift-yonlu (araştırma geri alınabilir; alım kararı ayrı ve sahibinin) · karar veren: kaan · danışılan: claude · bilgilendirilen: —

## Bağlar
### Dayandığı
- [[40-ic-ses/fikirler/F-0001-yazici-isi-fikri]] — kararın konusu olan fikir; açık soruları ve Cynefin ataması
### Beslediği
- [[20-sirket/gorevler/G-001-yazici-pazar-arastirmasi]] — bu karara dayanan görev kartı (bekliyor)
### Gelen
- ← [[30-devlet/MOC-devlet]] — kararlar listesi
- ← [[20-sirket/gorevler/G-001-yazici-pazar-arastirmasi]] — yetki kaynağı olarak

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-07 | T-002 | Oluşturuldu (önerildi) |
