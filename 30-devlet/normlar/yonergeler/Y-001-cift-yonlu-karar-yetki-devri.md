---
id: 20261007-1100-y-001-cift-yonlu-karar-yetki-devri
ad: y-001-cift-yonlu-karar-yetki-devri
tur: yonerge
kat: 3
surum: 1.0
durum: aktif
amac: Bu yonerge, imza matrisinde sahibine ayrilmamis butun cift yonlu (geri alinabilir) kararlarin orkestrator tarafindan sahibine sorulmadan verilip kaydedilmesini ve brifingde bildirilmesini, sahibine yalniz imza matrisi kalemlerinin ve fiziksel eylemlerin sorulmasini belirlemek icin var.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-020
dayandigi: [30-devlet/normlar/IMZA-MATRISI.md]
besledigi: []
ust: 30-devlet/MOC-devlet.md
dayanak: 30-devlet/normlar/IMZA-MATRISI.md
imza: orkestrator (Baskan a.)
yururluk: 2026-10-07
sunset: 2027-01-05
yetki_devri: "Sahibinin 2026-10-07 sohbet talimati: 'bu tarz secimleri neden bana yaptiriyorsun ... bunu benim icin ayarlayamaz misin'"
saklama: S
etiketler: [norm/yetki-devri]
---

# Yönerge Y-001: Çift yönlü kararlarda yetki devri

## Amaç
Bu yönerge, imza matrisinde sahibine ayrılmamış bütün çift yönlü (geri alınabilir) kararların orkestratör tarafından sahibine sorulmadan verilip kaydedilmesini ve brifingde bildirilmesini, sahibine yalnız imza matrisi kalemlerinin ve fiziksel eylemlerin sorulmasını belirlemek için var.

## İçerik
### Madde 1 — Dayanak ve yetki
Anayasa Madde 6 (yetki devri yazılı, sınırlı, süreli; devreden gözetim sorumluluğunu korur) ve Madde 9 (çift yönlü kararlar hızlı verilir, kaydedilir, brifingde bildirilir); İmza Matrisi'nde yönerge orkestratörün "Başkan a." yetkisindedir. Yazılı devir: sahibinin 2026-10-07 sohbet talimatı ("bu tarz seçimleri neden bana yaptırıyorsun … bunu benim için ayarlayamaz mısın").

### Madde 2 — Devredilen yetki
Orkestratör şu kararları sahibine sormadan verir, `/karar` ile kaydeder (`karar_veren: orkestrator (Baskan a.)`) ve brifingde tek satırla bildirir:
1. Geri alınabilir her karar: yöntem, sıra, öncelik, araç denemesi, araştırma kapsamı, fikirlerin İç Ses modları (SOR, ZORLA, ARAŞTIR), deneme/ölçüm tasarımı.
2. Proje içinde, git ile geri alınabilir dosya değişiklikleri ve yerel araç kurulumu (dışarıya veri göndermeyen, `.araclar/` altında, git dışı).
3. Görev kartı açma, başlatma ve kanıtla kapatma (kabul ölçütleri ve bağımsız inceleme şartıyla).
4. Önerildi durumundaki kendi önerilerini, sahibinin itirazı yoksa ilerletme; sahibi itiraz ederse karar geri alınır ve kayda geçer.

### Madde 3 — Sahibine ayrılanlar (devredilemez)
Anayasa Madde 6 gereği bu liste yönergeyle daraltılamaz. Orkestratör şunlarda durur ve tek soru sorar (ASK.md ya da sohbet):
1. İmza Matrisi A1–A11: anayasa, rol açma/kapama, risk iştahı, kural yayımı/ilgası, bütçe ve token tavanı, geri alınamaz dış eylem (silme, yayın, ödeme, dış API yazımı, mesaj gönderme), teftiş, politika belirleyen talimat, kamuya açık çıktı, yeni dış erişimli araç, kabul edilmiş kararın yerine geçme.
2. Dışarıya veri gönderen her araç ya da hizmet (ör. içerik yükleyen tarama araçları, bulut ses/OCR).
3. Proje klasörü dışında silme ya da değiştirme.
4. Yalnız sahibin yapabileceği fiziksel ya da kimlik eylemleri (güven penceresi, mikrofon/kamera izni, dinleme/beğeni yargısı, hesap ve ödeme).
5. Sahibinin kişisel tercihi olan ve kanıtla belirlenemeyen seçimler (ör. hangi iş alanına ilgi duyduğu); bunlarda bile önce gerekçeli bir varsayılan önerilir.

### Madde 4 — Soru biçimi
Sorulması gereken bir şey varsa: tek soru, gerekçesiyle ve önerilen varsayılanla. Birden çok seçimi biriktirip sahibine seçim listesi sunmak yasaktır; çift yönlü olanlar Madde 2'ye göre verilir.

### Madde 5 — Gözetim ve rapor
Devredilen yetki tekrar devredilemez. Orkestratörün verdiği kararlar haftalık gözden geçirmede (/haftalik) listelenir; sahibi herhangi birini geri alabilir. Yetki aşımı Denetim'in uygunluk incelemesine girer.

### Madde 6 — Yürürlük
Bu yönerge 2026-10-07'de KARARLAR.md'ye yazılarak yürürlüğe girer; yürüten orkestratördür; `sunset` 2027-01-05'te gözden geçirilir.

## Bağlar
### Dayandığı
- [[30-devlet/normlar/IMZA-MATRISI]] — yönerge yetkisi orkestratörde ("Başkan a."); sahibine ayrılan A1–A11 listesi
### Beslediği
### Gelen
- ← [[30-devlet/MOC-devlet]] — normlar listesi

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 1.0 | 2026-10-07 | T-020 | Yayımlandı (orkestratör, Başkan a.; sahibinin yazılı talimatıyla) |
