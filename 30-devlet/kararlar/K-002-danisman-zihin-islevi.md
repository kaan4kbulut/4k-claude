---
id: 20261006-2211-k-002-danisman-zihin-islevi
ad: k-002-danisman-zihin-islevi
tur: karar
kat: 3
surum: 1.0
durum: kabul
amac: Bu karar kaydi, Danisman rolunun ayri bir ajan olarak degil zihin katinin bir islevi (yonlendirme notu + steelman/pre-mortem degerlendirmesi) olarak tanimlanmasi onerisini ve alternatifleri tutar.
olusturma: 2026-10-06
guncelleme: 2026-10-07
yazar: claude
talimat: T-000
dayandigi: [30-devlet/normlar/ANAYASA.md, 00-sistem/arastirma/08-ic-ses-yontemleri.md, 30-devlet/kararlar/K-001-pilotta-kadro-yok.md]
besledigi: []
ust: 30-devlet/MOC-devlet.md
kapi: cift-yonlu
karar_veren: kaan
danisilan: [claude]
bilgilendirilen: []
beklenen_sonuc_olasilik: 70
gozden_gecir: 2026-11-06
saklama: S
etiketler: [karar/kadro, karar/ic-ses]
---

# Karar K-002: Danışman zihin katının işlevidir

## Amaç
Bu karar kaydı, Danışman rolünün ayrı bir ajan olarak değil zihin katının bir işlevi (yönlendirme notu + steelman/pre-mortem değerlendirmesi) olarak tanımlanması önerisini ve alternatifleri tutar.

## İçerik
### Bağlam ve problem
Önceki tasarımda Danışman iki iş yapıyordu: bilinmeyen konuda yönlendirme notu ve fikrin olumlu/olumsuz değerlendirmesi. Ayrı ajan mı, İnceleyici'nin içinde mi tartışması açık kalmıştı. Yeni modelde (Anayasa 12) zihin katı zaten dinleyen, araştıran ve meydan okuyan bir iç sestir; Danışman'ın işleri bu katın ZORLA ve ARAŞTIR modlarıyla örtüşüyor.

### Karar sürücüleri
- Çakışma yok: aynı iş iki yerde tanımlanmasın.
- Dalkavukluk araştırması: değerlendirme ayrı bir "övgü/eleştiri" ajanı değil, prosedür (steelman → inversion → pre-mortem) olmalı.
- Kadro kararı K-001: pilotta ek ajan yok.

### Seçenekler
| # | Seçenek | Artı | Eksi | Maliyet | Risk |
| --- | --- | --- | --- | --- | --- |
| A | Zihin katının işlevi (rules/40-ic-ses ZORLA + ARAŞTIR; /alan-paketi yönlendirme notu) | Çakışma yok; prosedür olarak dalkavukluğa dirençli; ek ajan yok | Ana oturumun bağlamını kullanır | düşük | uzun değerlendirmelerde bağlam dolabilir |
| B | Ayrı salt okunur Danışman ajanı (Opus) | Temiz bağlam; bağımsız görüş | Dokuzuncu ajan; koordinasyon; maliyet | orta | görüş yazan ajan "iki taraf da haklı" formülüne kayabilir |
| C | denetci'nin içine katmak | Tek inceleme noktası | Denetim bağımsızlığı bulanır (yürütme öncesi görüş vs sonrası denetim) | düşük | Anayasa 8 ile çatışır |

### Karar (öneri)
**Danışman'ı zihin katının işlevi olarak tanımlayacağız** (seçenek A), çünkü işleri İç Ses modlarıyla örtüşüyor ve değerlendirme ajandan çok prosedür ister. Büyük işlerde uzun değerlendirme gerekirse B seçeneği kadro kapısında yeniden açılır.

### Beklenen sonuç
Pilotta yönlendirme ve değerlendirme ihtiyacı ana oturumda karşılanır; olasılık %70.

### Sonuçlar
- İyi: sade; dalkavukluk-karşıtı kurallar tek yerde.
- Kötü: ana oturum yükü artar.
- Nötr: "Danışman" adı rol listesinde görünmez; işlev MODEL-POLITIKASI'nda Opus/high satırı olarak durur.

### Doğrulama
Pilot deneme sonunda (2026-11-06) sahibine soru: yönlendirme/değerlendirme yeterli miydi? Yetersizse B.

### Kapı ve roller
kapi: cift-yonlu · karar veren: kaan (kabul, 2026-10-07) · danışılan: claude

## Bağlar
### Dayandığı
- [[30-devlet/normlar/ANAYASA]] — Madde 12 zihin katı
- [[00-sistem/arastirma/08-ic-ses-yontemleri]] — dalkavukluk araştırması: prosedür > istem
- [[30-devlet/kararlar/K-001-pilotta-kadro-yok]] — ek ajan yok
### Beslediği
### Gelen
- ← [[30-devlet/normlar/ANAYASA]] — Madde 12 uyarınca Danışman'ın yeri

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-06 | T-000 | Oluşturuldu (onerildi) |
| 1.0 | 2026-10-07 | T-019 | Sahibi kabul etti (eski durum: onerildi) |
