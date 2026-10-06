---
id: 20261006-2210-k-001-pilotta-kadro-yok
ad: k-001-pilotta-kadro-yok
tur: karar
kat: 3
surum: 1.0
durum: kabul
amac: Bu karar kaydi, pilot asamasinda rol (bakanlik) ajanlari acilmamasini, yalniz okuyucu ve denetci alt ajanlarinin bulunmasini ve nedenini kalici olarak tutar.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: kaan
talimat: T-000
dayandigi: [30-devlet/normlar/ANAYASA.md, 00-sistem/arastirma/03-cok-ajanli-isleyis-ve-yonetisim.md]
besledigi: [30-devlet/kararlar/K-002-danisman-zihin-islevi.md]
ust: 30-devlet/MOC-devlet.md
kapi: cift-yonlu
karar_veren: kaan
danisilan: [claude]
bilgilendirilen: []
beklenen_sonuc_olasilik: 80
gozden_gecir: 2026-11-06
saklama: S
etiketler: [karar/kadro]
---

# Karar K-001: Pilotta kadro yok

## Amaç
Bu karar kaydı, pilot aşamasında rol (bakanlık) ajanları açılmamasını, yalnız okuyucu ve denetci alt ajanlarının bulunmasını ve nedenini kalıcı olarak tutar.

## İçerik
### Bağlam ve problem
İlk tasarımda sekiz-dokuz alt ajan (Planlayıcı, Tasarımcı, Mimar, Geliştirici, Testçi, İnceleyici, Yayıncı, Kadro yöneticisi, Danışman) vardı ve hiçbiri denenmemişti. Araştırma, çok ajanlı sistemlerin başlıca hatalarının spesifikasyon ve doğrulama eksikliğinden geldiğini (MAST), ve "önce tek ajanı optimize et, yetmezse takıma geç" tavsiyesini gösterdi. Önce işleyişin (altı adım, kapılar, kanıt) oturması gerekiyor; kadro işleyişin üstüne gelir.

### Karar sürücüleri
- İşleyiş denenmeden rol eklemek hata kaynağını çoğaltır.
- Maliyet: çok ajanlı iş ~15× token (Anayasa 13).
- Güvenlik için iki alt ajan şart: güvenilmeyen içerik için karantinalı okuyucu (Dual-LLM), kanıt için bağımsız inceleyici.

### Seçenekler
| # | Seçenek | Artı | Eksi | Maliyet | Risk |
| --- | --- | --- | --- | --- | --- |
| A | Pilotta rol yok; yalnız okuyucu + denetci | Basit, ucuz, hata kaynağı az; işleyiş net test edilir | Büyük iş pilotta yapılamaz | düşük | işleyiş oturunca kadro eklemek ikinci tur ister |
| B | Tam kadro ile başla | Gerçekçi ölçek | Denenmemiş 9 ajan; hata kaynağı yüksek; maliyet | yüksek | koordinasyon hataları işleyiş hatasıyla karışır |
| 0 | Hiçbir şey yapma (alt ajan hiç) | En ucuz | Güvenilmeyen içerik ana ajana girer; inceleme yazarla aynı bağlamda | çok düşük | güvenlik ve kanıt zafiyeti |

### Karar
**Pilotta rol ajanı açmayacağız; yalnız `okuyucu` ve `denetci` olacak** (seçenek A), çünkü işleyiş oturmadan kadro eklemek hata kaynağını çoğaltır ve iki alt ajan güvenlik ve kanıt için yeterlidir.

### Beklenen sonuç
Dört talimatlık deneme tek ana oturum + iki alt ajanla tamamlanır; olasılık %80; gerekçe: işler küçük/orta sınıfta.

### Sonuçlar
- İyi: basit, ölçülebilir pilot; maliyet düşük.
- Kötü: büyük iş sınıfı pilotta test edilmez.
- Nötr: roller/ klasörü boş kalır; şablon hazır.

### Doğrulama
Deneme raporu (T-001..T-004) sonrası 2026-11-06'da gözden geçirilir: işleyiş oturduysa kadro kapısı açılır (IMZA A2).

### Kapı ve roller
kapi: cift-yonlu · karar veren: kaan · danışılan: claude · bilgilendirilen: —

## Bağlar
### Dayandığı
- [[30-devlet/normlar/ANAYASA]] — Madde 13 (kaynak kıtlığı), Madde 11 (güvenilmeyen içerik), Madde 8 (bağımsız inceleme)
- [[00-sistem/arastirma/03-cok-ajanli-isleyis-ve-yonetisim]] — MAST hata sınıfları; "önce tek ajan" tavsiyesi
### Beslediği
- [[30-devlet/kararlar/K-002-danisman-zihin-islevi]] — Danışman kararı bu karara dayanır (ek ajan yok)
### Gelen
- ← [[30-devlet/normlar/ANAYASA]] — Madde 13 uyarınca ilk kadro kararı

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 1.0 | 2026-10-06 | T-000 | Kabul edildi |
