---
id: 20261006-2201-imza-matrisi
ad: imza-matrisi
tur: referans
kat: 3
surum: 0.1
durum: aktif
amac: Hangi kararin kimin imzasini istedigini, yetki devrinin kurallarini ve kayitlarini tek tabloda tutar; orkestrator her kararda buraya bakar.
olusturma: 2026-10-06
guncelleme: 2026-10-07
yazar: kaan
talimat: T-000
dayandigi: [30-devlet/normlar/ANAYASA.md, 00-sistem/arastirma/07-devlet-yapilari.md]
besledigi: [30-devlet/normlar/yonergeler/Y-001-cift-yonlu-karar-yetki-devri.md]
saklama: S
etiketler: [norm/yetki]
---

# İmza matrisi

Anayasa Madde 6 ve 9'un uygulaması. Gerçek bakanlık imza yetkileri yönergelerinden türetildi: yetki devri yazılı, sınırlı, süreli; devreden gözetim sorumluluğunu korur; devredilen yetki tekrar devredilemez; devralan dönemsel bilgi verir; politika niteliği görülen konuda imzadan önce üste bilgi ve alternatif sunulur.

## Amaç
Hangi kararın kimin imzasını istediğini, yetki devrinin kurallarını ve kayıtlarını tek tabloda tutar; orkestratör her kararda buraya bakar.

## İçerik

### A. Sahibi bizzat imzalar (tek yönlü; `/kapi` + ASK.md zorunlu)
| # | Karar | Araç / engel |
| --- | --- | --- |
| A1 | Anayasa değişikliği | permissions.deny: yalnız insan düzenler |
| A2 | Rol (bakanlık) açma, kapama, birleştirme; Denetim başı atama | kadro kapısı |
| A3 | Risk iştahı: hangi hatalar kabul edilir, hangi bulgular risk kabulüyle kapanır | kapı + karar kaydı |
| A4 | Kural yayımı ve ilgası (KR-xxx) | KARARLAR.md'ye yazılarak yürürlük |
| A5 | Bütçe ve token tavanı; model politikası değişikliği | MODEL-POLITIKASI.md |
| A6 | Geri alınamaz dış eylem: silme (fiziksel), yayınlama, ödeme, dış API'ye yazma, e-posta/mesaj gönderme (ilk müşteri yanıtı dahil) | permissions.ask; hook |
| A7 | Teftiş / olay bazlı inceleme başlatma | Denetim |
| A8 | Politika belirleyen talimat: önceliklerin sırasını, bir katın işleyişini değiştiren her şey | kapı |
| A9 | Kamuya açık çıktı (web, pazar yeri listesi, duyuru) | kapı |
| A10 | Yeni araç/MCP sunucusu ekleme (dış sisteme erişim veren) | ARAC-KAYDI + karar |
| A11 | Kabul edilmiş kararın yerine yeni karar (supersede) | /karar + kapı |

### B. Orkestratör "Başkan a." imzalar (çift yönlü; kaydet, brifingde bildir)
| # | Karar | Dayanak |
| --- | --- | --- |
| B1 | Yönerge yayımı (Y-xxx), kurala aykırı olmamak kaydıyla | Anayasa 7 |
| B2 | Görev önceliklendirme ve sıralama (SLE içinde) | rules/20-sirket |
| B3 | Roller arası ihtilafta ilk karar; çözülmezse sahibine | write-round |
| B4 | İş büyüklüğü sınıflandırması (küçük/orta/büyük) | CLAUDE.md |
| B5 | Çift yönlü kararların kabulü (K-xxx, kapi: cift-yonlu) | /karar |
| B6 | Acil Seviye 1-2 geçici karar; ilk çevrimde sahibine Late Notice | Anayasa 7 |
| B7 | Alt ajan açma (model politikası sınırları içinde) | MODEL-POLITIKASI |

### C. Rol ajanı imzalar (yönergeyle devredilen yetki; tekrar devredilemez)
| # | Karar |
| --- | --- |
| C1 | Görev talimatı: kendi kartı içindeki adım sırası ve yöntem |
| C2 | Rutin wiki güncellemesi: gözlem, not, çıktı sayfası, kendi kartının kanıt alanı |
| C3 | İç görev dağılımı (kendi alt görevleri) |
| C4 | Bilgi notu, taslak, öneri (yürürlük değil) |

### D. Paraf ve hazırlık
- İlk hazırlayanın parafı esastır; en az imza. Paraf edenler içeriği düzeltebilir; son söz imza sahibinde.
- Birden çok rolü ilgilendiren yazıda koordine birimlerin parafı (write-round sonucu) eklenir.
- Alt birim sahibine sunmadan önce orkestratörün parafını alır.

### E. Yetki devri kuralları
1. Yazılı: yönerge (Y-xxx) ile; hangi yetki, kime, hangi sınır, ne süre.
2. Sınırlı ve süreli: sunset tarihi; uzatma gözden geçirmeyle.
3. Devreden gözetim sorumluluğunu korur.
4. Devredilen yetki tekrar devredilemez.
5. Devralan çekimser kalmaz; yetkiyi kullanır ve dönemsel (oturum sonu / haftalık) rapor verir.
6. Politika niteliği görürse imzadan önce üste bilgi + alternatif sunar.
7. Perm-sec kuralı: orkestratör sahibinin talimatını Anayasa'ya aykırı görürse yazılı teyit ister; teyit edilirse sorumluluk sahibinde, kayıt denetim dosyasına.

### F. Yetki devri kayıtları
| Yönerge | Yetki | Devreden | Devralan | Sınır | Sunset | Durum |
| --- | --- | --- | --- | --- | --- | --- |
| — | (pilotta rol yok; ilk kayıt kadro kapısıyla) | | | | | |

### G. Onay seviyesi evrimi
Her karar sınıfı "onay" (B/C satırı için orkestratör onayı; A için sahibi) seviyesinde başlar. 4-8 hafta sıfır hata ile geçen bir sınıf, sahibinin kararıyla "otomatik" seviyesine indirilebilir; bu da bir kayıttır (K-xxx) ve geri alınabilir.

## Bağlar
### Dayandığı
- [[30-devlet/normlar/ANAYASA]] — Madde 6 (yetkinin kaynağı) ve Madde 9 (kapılar)
- [[00-sistem/arastirma/07-devlet-yapilari]] — bakanlık imza yönergeleri, yetki devri ilkeleri, Late Notice
### Beslediği
### Gelen
- ← [[30-devlet/normlar/yonergeler/Y-001-cift-yonlu-karar-yetki-devri]] — çift yönlü kararlarda orkestratöre yetki devri (A1–A11 dışı)
- ← [[30-devlet/normlar/ANAYASA]] — Madde 6 ve 9'un ayrıntısı

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-06 | T-000 | Oluşturuldu |
