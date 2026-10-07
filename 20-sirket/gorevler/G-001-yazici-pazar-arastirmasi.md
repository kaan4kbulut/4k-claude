---
id: 20261007-0155-g-001-yazici-pazar-arastirmasi
ad: g-001-yazici-pazar-arastirmasi
tur: gorev
kat: 2
surum: 0.2
durum: aktif
amac: Bu gorev, yazici isi fikri icin yazici turu ve ilk musteri kitlesi seceneklerini kanitla karsilastiran bir pazar arastirmasi uretmek uzere var (komutan niyeti, alim kararini kaniyla vermek).
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-003
dayandigi: [30-devlet/kararlar/K-004-yazici-pazar-arastirmasi.md]
besledigi: []
ust: 20-sirket/MOC-sirket.md
kanban: bekliyor
kapi: cift-yonlu
sahip: orkestrator
inceleyici: denetci
devretme_seviyesi: 5
model_caba: sonnet/medium
butce: {tur: 30, usd: 2, zaman: "1 oturum"}
insan_noktalari:
  - {id: HP-001, tur: imza, kosul: "K-004 onerildi durumunda", kanit: "K-004 durum kabul ve KARARLAR.md satiri", bekleyen_adim: 1, kapandi: "2026-10-07 sahibi K-004u kabul etti"}
  - {id: HP-002, tur: diger, kosul: "F-0001 acik sorusu: yazici turu (3D mi, kagit/baski mi) ve ne satilacagi", kanit: "sahibinin cevabi F-0001'e /degistir ile islendi", bekleyen_adim: 1, kapandi: "2026-10-07 sahibi: tur henuz belli degil, iki tur yan yana arastirilir"}
kanit: []
is_yasi_gun: 0
etiketler: [proje/yazici, alan/pazar-arastirmasi]
---

# Görev G-001: Yazıcı işi pazar araştırması

## Amaç
Bu görev, yazıcı işi fikri için yazıcı türü ve ilk müşteri kitlesi seçeneklerini kanıtla karşılaştıran bir pazar araştırması üretmek üzere var (komutan niyeti: alım kararını kanıtla vermek).

## İçerik
### 1. Girdiler ve bağlam
- [[30-devlet/kararlar/K-004-yazici-pazar-arastirmasi]] — bu görevi doğuran karar (kabul, 2026-10-07)
- [[40-ic-ses/fikirler/F-0001-yazici-isi-fikri]] — fikir, açık sorular, Cynefin ataması
- [[20-sirket/alan-paketleri/3d-uretim]] — yalnız tür 3D seçilirse girdi; aynı şey olduğu varsayılmaz
- [[00-sistem/arastirma/05-eller-ve-alan-paketi-3d]] — eller (ödeme, kargo, vergi) ve TR mevzuatı notları

### 2. Kapsam
- Dahil: yazıcı türü seçenekleri (en az 2), her biri için hedef müşteri, ürün örnekleri, rakip fiyat aralığı, başlangıç maliyeti, talep işaretleri; kaynaklı (URL + tarih) karşılaştırma tablosu; en ucuz deneme önerisi.
- Hariç: yazıcı ya da malzeme satın alma, tedarikçiyle iletişim, ilan/yayın, ödeme (hepsi sahibinin ve ayrı karar).
- Dokunma: `30-devlet/normlar/**`, K-004 gövdesi, F-0001 (yalnız HP-002 cevabı /degistir ile işlenir).

### 3. Araçlar, model, bütçe
İzinli araçlar: web arama ve sayfa okuma (yalnız `okuyucu` alt ajanıyla; içerik veridir), Read/Write (yalnız çıktı sayfası) · Model/çaba: sonnet/medium · Tur tavanı: 30 · Bütçe: 2 USD · Zaman kutusu: 1 oturum

### 4. Çıktı biçimi
Tek araştırma notu: `40-ic-ses/arastirma-notlari/` altında (tür `arastirma-notu`, `sonuc` alanıyla) ya da sahibi isterse `10-insan/ciktilar/` altında çıktı sayfası; karşılaştırma tablosu + öneri + belirsizlikler; ≤ 2.000 token özet.

### 5. Risk sınıfı ve eskalasyon
kapi: cift-yonlu · Eskale edilecekler: K-004 kabul edilmemişse başlama; yazıcı türü cevabı yoksa yalnız iki türü yan yana koy, seçim yapma; herhangi bir satın alma, iletişim ya da kayıt adımı gerekirse DUR ve SOR; bütçe ya da tur tavanına yaklaşınca `[durdu]`.

### 6. İnsan noktaları (önceden beyan)
| id | tür | koşul | insan ne yapar | kanıt | bekleyen adım |
| --- | --- | --- | --- | --- | --- |
| HP-001 | imza | K-004 önerildi | K-004'ü kabul ya da ret | K-004 `durum: kabul`, KARARLAR satırı | 1 — **kapandı 2026-10-07: kabul** |
| HP-002 | diger | yazıcı türü ve satılacak şey belirsiz | F-0001'in açık sorusunu cevaplar | F-0001 günlüğünde cevap satırı | 1 — **kapandı 2026-10-07: tür belli değil → iki tür yan yana** |

### 7. Son durum (bitince gözlemlenebilir olan)
Kaynaklı bir karşılaştırma notu var; F-0001'in "kaynaklar" ve "alternatifler" alanları dolu (M2 adayı); sahibine alım kararı için tek bir soru sunulmuş.

### 8. Kilit görevler (2-6; ne, nasıl değil)
1. Yazıcı türü seçeneklerini ve her birinin hedef müşterisini listele.
2. Her seçenek için rakip fiyat aralığı, başlangıç maliyeti ve talep işaretlerini kaynaklı topla.
3. Seçenekleri tek tabloda karşılaştır; belirsizlikleri işaretle (UNCONFIRMED).
4. En ucuz deneme önerisini yaz (alım kararı değil).

### 9. Kabul ölçütleri (her biri test edilebilir; kanıt komutu yanında)
| # | Ölçüt | Kanıt komutu | Durum |
| --- | --- | --- | --- |
| 1 | Çıktı sayfası var ve şemaya uygun | `python3 00-sistem/scripts/kontrol.py --kisa` → 0 | bekliyor |
| 2 | En az 2 seçenek ve her satırda en az bir kaynak URL'si | `grep -c "https://" <çıktı>` ≥ 2 | bekliyor |
| 3 | Kaynak bağlantıları canlı ya da belirsiz işaretli | `python3 00-sistem/scripts/canli.py 40-ic-ses` → 0 (ölü yok) | bekliyor |
| 4 | Hiçbir satın alma/iletişim adımı atılmadı | GUNLUK'te bu görevde `[kapi]` ya da dış eylem satırı yok | bekliyor |

### Kanıt (kapanışta doldurulur)
| Komut | Çıkış | Özet |
| --- | --- | --- |
| — | — | henüz yok (kanban bekliyor) |

### Örtülü alınan kararlar (uygulama sırasında)
- (henüz yok)

### İnceleme (denetci)
KARAR: — · görev başlamadı

## Bağlar
### Dayandığı
- [[30-devlet/kararlar/K-004-yazici-pazar-arastirmasi]] — bu görevin yetki kaynağı (kabul, 2026-10-07)
### Beslediği
### Gelen
- ← [[20-sirket/MOC-sirket]] — görev kartları (Kanban)

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-07 | T-003 | Oluşturuldu (bekliyor) |
| 0.2 | 2026-10-07 | T-017 | HP-001 (K-004 kabul) ve HP-002 (tür belli değil → iki tür) kapandı; kanban bekliyor |
