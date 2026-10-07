---
id: 20261007-1115-kr-001-hafif-yol
ad: kr-001-hafif-yol
tur: kural
kat: 3
surum: 1.0
durum: kabul
amac: Bu kural, Ic Ses'e gozlem ve ham fikir (M0) notu eklenirken alti adimin tek komutla otomatik yapilmasini (hafif yol) zorunlu ve yeterli kilmak icin var; amaci kucuk not icin tören yukunun not almayi caydirmasi riskini onlemektir.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-021
dayandigi: [CLAUDE.md]
besledigi: [00-sistem/scripts/not.py, 30-devlet/kapilar/KP-002-kr-001-yayimi.md]
ust: 30-devlet/MOC-devlet.md
kapi: tek-yonlu
karar_veren: kaan
yururluk: 2026-10-07
yuruten: orkestrator
sunset: 2027-01-05
saklama: S
etiketler: [norm/kural, ic-ses]
---

# Kural KR-001: Hafif yol (İç Ses gözlem ve ham fikir)

## Amaç
Bu kural, İç Ses'e gözlem ve ham fikir (M0) notu eklenirken altı adımın tek komutla otomatik yapılmasını (hafif yol) zorunlu ve yeterli kılmak için var; amacı küçük not için tören yükünün not almayı caydırması riskini önlemektir.

## İçerik
### Madde 1 — Kapsam
Bu kural yalnız 40-ic-ses katında iki sayfa türünü bağlar: (a) gözlem; (b) merdiven 0 (ham) fikir. Diğer bütün türler (merdiven ≥ 1 fikir, karar, kural, görev, kaynak, çıktı) ve bağ (dayandigi) içeren her sayfa CLAUDE.md'deki tam altı adımla açılır.

### Madde 2 — Hüküm
1. Kapsamdaki notlar `python3 00-sistem/scripts/not.py <gozlem|fikir> "<başlık>" "<metin>"` komutuyla eklenir. Komut altı adımın hepsini yapar: talimat kaydı (T-xxx, otomatik kapanır), amaç ve kat, yer ve ad, şablon alanları, MOC bağı, HARITA ve GUNLUK satırı ve `kontrol.py --kisa`.
2. Komut çıkış kodu 0 vermedikçe not eklenmiş sayılmaz; hata kontrol.py çıktısıyla düzeltilir.
3. Hafif yolla açılan fikir merdiven 1'e terfi ederken tam yola geçer: Cynefin ataması, çerçeve ve bağlar `/degistir` ile yazılır.
4. Hafif yol Anayasa Madde 3.2'ye ("küçük işte yol kısalır, atlanmaz") uygundur: hiçbir adım atlanmaz, adımlar otomatikleşir.

### Madde 3 — İstisnalar
İstisna yoktur. Sahibi bir notun tam yolla açılmasını isterse tam yol kullanılır.

### Madde 4 — Yürürlük ve yürütme
Bu kural sahibinin imzasıyla (IMZA-MATRISI A4, tek yönlü kapı) `durum: kabul` olur ve KARARLAR.md'ye yazılarak yürürlüğe girer; `not.py` kural kabul edilmeden çalışmaz (çıkış 3). Yürüten orkestratördür; `sunset` 2027-01-05'te gözden geçirilir, uzatılmazsa yürürlükten kalkar ve not.py yeniden kilitlenir.

### DEA-lite (düzenleyici etki analizi)
| Soru | Cevap |
| --- | --- |
| İhtiyaç: hangi sorun, hangi kanıt | T-001'de tek fikir notu için 6 dosyaya dokunuldu; T-002–T-004'te bir karar + bir kart + bir cümle için 10+ dosya; T-018'de bağımsız inceleme sürüm/günlük eksikliklerini yakaladı (elle yapılan adımlar hata üretiyor). Analizde "tören yükü" en büyük tasarım riski olarak saptandı. |
| Alternatifler (kural çıkarmama dahil) | (0) Kural çıkarmama: her not 6 elle adım; yük ve hata sürer. (A) Bu kural: adımlar otomatik, yalnız gözlem/M0. (B) Adım sayısını azaltmak (ör. HARITA'yı kaldırmak): Anayasa 3.2'ye aykırı ("atlanmaz"); reddedildi. |
| Etkilenen roller / sayfalar | Orkestratör (not alma); 40-ic-ses/gozlemler, 40-ic-ses/fikirler, MOC-ic-ses, HARITA, GUNLUK, TALIMATLAR. |
| Maliyet (zaman, token, bağlam) | Not başına tek komut (~1 sn) yerine 6 elle adım (bir oturum turu, binlerce token). |
| Risk ve azaltma | Gözden kaçan bağlam (çerçeve, Cynefin) → M1 terfisinde tam yol zorunlu. Toplu çöp not → 48 saat / 30 gün öldürme kuralları (rules/40-ic-ses) ve /uyku geçerli. Betik hatası → kontrol.py çıkış koduyla durur. |
| Nasıl ölçülür (uygunluk) | Haftalık: hafif yol talimatlarının hepsi `kapali` ve kontrol.py 0; M1'e çıkan hafif yol fikirlerinin günlüğünde `/degistir` satırı. |

### Write-round
| Rol | Görüş | Tarih |
| --- | --- | --- |
| (pilotta rol yok, K-001) | — | 2026-10-07 |

### Danışman görüşü (≤ 3 cümle)
Hafif yol not almayı kolaylaştırırken bağlamı fikir terfisine erteler; bu, İç Ses'in "dinle, kaydet" moduna uygundur. Risk, çok sayıda ham notun bakımsız kalmasıdır; mevcut öldürme ve /uyku kuralları bunu karşılar. (K-002: Danışman zihin katının işlevidir; bu görüş orkestratörün ZORLA tarzı değerlendirmesidir.)

### Denetim uygunluk notu
Anayasaya uygunluk: evet. Madde 3.2 (yol kısalır, atlanmaz) korunur; Madde 10 (her sayfa şemayla doğar, haritada ve günlükte görünür) betikle sağlanır ve kontrol.py ile doğrulanır.

### Değişiklik geçmişi (çerçeve taslak)
- 2026-10-07: Kural taslağı oluşturuldu, sahibinin imzasına sunuldu (T-021).
- 2026-10-07: Sahibinin imzasıyla kabul edildi ve yürürlüğe girdi (KP-002, T-022).

## Bağlar
### Dayandığı
- [[CLAUDE.md]] — "Bir parçanın doğuşu (zorunlu altı adım)" kuralı; bu kural onu kapsamdaki iki tür için otomatikleştirir
### Beslediği
- [[00-sistem/scripts/not.py]] — kuralın uygulayıcısı; kural kabul edilmeden çalışmaz
- [[30-devlet/kapilar/KP-002-kr-001-yayimi]] — yayım kapısı (go)
### Gelen
- ← [[30-devlet/MOC-devlet]] — normlar listesi
- ← [[30-devlet/kapilar/KP-002-kr-001-yayimi]] — imza kaydı

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-07 | T-021 | Taslak (önerildi); sahibinin imzası bekleniyor |
| 1.0 | 2026-10-07 | T-022 | Sahibinin imzasıyla kabul, yürürlük 2026-10-07 (eski: önerildi) |
