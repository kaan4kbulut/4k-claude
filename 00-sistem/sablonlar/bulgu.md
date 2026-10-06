---
id: YYYYMMDD-HHMM-slug
ad: slug
tur: bulgu
kat: 3
surum: 0.1
durum: aktif
amac: Bu bulgu, ... denetiminde saptanan ... uygunsuzlugunu, nedenini, etkisini ve kapanis yolunu kayit altina alir.
olusturma: YYYY-MM-DD
guncelleme: YYYY-MM-DD
yazar: denetci
talimat: T-xxx
dayandigi: []
besledigi: []
ust: 30-devlet/MOC-devlet.md
denetim_turu: uygunluk
ilgili_rol: orkestrator
cevap_son_tarih: YYYY-MM-DD
mutabik: belirlenmedi
eylem_plani: 
kapanis_turu: belirlenmedi
saklama: S
etiketler: []
---

<!--
BULGU = Sayıştay / İç Denetim mantığı: kriter + durum + neden + etki + öneri.
- İlgili rol 30 gün / 3 çevrim içinde cevap verir: mutabık mı?
- Mutabıksa eylem planı (denetim/eylem-planlari/EP-xxx.md): sahip + tarih + ilerleme.
- YALNIZ Denetim kapatır (kapanis_turu: dogrulandi); rol kendi bulgusunu kapatamaz.
- Mutabık olunmayan bulgu yalnız sahibinin risk kabulü imzasıyla kapanır (kapanis_turu: risk_kabulu; KP-xxx).
- denetim_turu: uygunluk | mali | performans | sistem | inceleme.
-->

# Bulgu B-xxx: <başlık>

## Amaç
Bu bulgu, … denetiminde saptanan … uygunsuzluğunu, nedenini, etkisini ve kapanış yolunu kayıt altına alır.

## İçerik
### Kriter (olması gereken)
(hangi norm/kural/şema maddesi)

### Durum (olan)
(ne saptandı; dosya:satır; kanıt komutu)

### Neden
…

### Etki
(risk, maliyet, güvenilirlik)

### Öneri
…

### Sınıf
ENGELLEYİCİ | ÖNERİ

### Rolün cevabı
Tarih: … · Mutabık: evet/hayır · Gerekçe: …

### Eylem planı
[[30-devlet/denetim/eylem-planlari/EP-xxx-...]] — sahip: … · tarih: … · ilerleme: …

### Kapanış
kapanis_turu: dogrulandi | risk_kabulu · tarih: … · doğrulayan: denetci · (risk kabulü ise KP-xxx)

## Bağlar
### Dayandığı
- [[yol]] — denetlenen sayfa / kart
### Beslediği
### Gelen

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | T-xxx | Bulgu açıldı |
