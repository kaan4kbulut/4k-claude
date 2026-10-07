---
id: 20261007-1927-kp-004-kr-002-yayimi
ad: kp-004-kr-002-yayimi
tur: kapi
kat: 3
surum: 0.1
durum: aktif
amac: Bu kapi kaydi, KR-002 zamanli kosular kuralinin yayimi karari icin sahibinin imzasini, kriterleri ve sonucu tutmak icin var.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-043
dayandigi: [30-devlet/normlar/kurallar/KR-002-zamanli-kosular.md]
besledigi: []
ust: 30-devlet/MOC-devlet.md
kapi_turu: adhoc
kapi: tek-yonlu
karar_veren: kaan
bekci: kaan
sonuc: bekliyor
saklama: S
etiketler: [kapi/kural-yayimi]
---

# Kapı KP-004: KR-002 zamanlı koşular kuralının yayımı

## Amaç
Bu kapı kaydı, KR-002 zamanlı koşular kuralının yayımı kararı için sahibinin imzasını, kriterleri ve sonucu tutmak için var.

## İçerik
### Onay Dosyası
- **İstenen karar:** KR-002 yürürlüğe girsin mi: zamanlı/gözetimsiz koşular (Routines, calistir.sh, cron) yalnız okur ve taslak üretir; bağlayıcı bağlanmaz; yayın, mesaj, ödeme ve dış API yazımı içeren rutin kurulmaz.
- **Gerekçe:** Gözetimsiz koşuda onay sorulamaz; yayın ve dış yazım geri alınamaz (A6). Taramanın Routines iddiası doğrulanmadı ama kural ondan bağımsız önleyici.
- **Alternatifler:** kural yok (ilke metinde kalır) · Routines tümden yasak (hazırlık işleri de durur).
- **Etki:** rutin kurulumu kapı adımı ister; bugün kurulu rutin yok.
- **Risk:** düşük; yanlış çıkarsa sunset (2027-01-05) ya da ilga.
- **Uygulayan:** orkestratör.

### Gerekli teslimatlar
- [[30-devlet/normlar/kurallar/KR-002-zamanli-kosular]] — kural metni, DEA-lite, uygunluk notu: hazır

### Kriterler
- Zorunlu: A6/A9'u daraltmıyor, uygulamasını tarif ediyor — evet.
- Zorunlu: KP-003 otomatik push kapsam dışı — evet (Madde 1).

### İmza
Bekleniyor (IMZA-MATRISI A4).

### Sonuç
bekliyor — bekçi: kaan.

## Bağlar
### Dayandığı
- [[30-devlet/normlar/kurallar/KR-002-zamanli-kosular]] — imzası istenen kural
### Beslediği
### Gelen
- ← [[30-devlet/MOC-devlet]] — kapılar listesi

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-07 | T-043 | Açıldı (bekliyor) |
