---
id: YYYYMMDD-HHMM-slug
ad: slug
tur: belirlenmedi
kat: 0
surum: 0.1
durum: taslak
amac: Bu sayfa ... icin var. (tek cumle; govdedeki Amac ile ayni)
olusturma: YYYY-MM-DD
guncelleme: YYYY-MM-DD
yazar: claude
talimat: T-xxx
dayandigi: []
besledigi: []
ust: 
etiketler: []
takma_adlar: []
---

<!--
GENEL ŞABLON — her tür bunu genişletir. Doldurma kuralları:
- Boş alan bırakma; bilinmiyorsa "belirlenmedi".
- id bir daha değişmez. ad = dosya adının uzantısız, numara öneksiz hali.
- kat, klasörle uyuşmalı (00→0, 10→1, 20→2, 30→3, 40→4). tur, SEMA §2'deki klasöre uymalı.
- ust: kat 1-4 için zorunlu, o katın MOC'u. kat 0 için boş bırakılabilir (alanı sil).
- dayandigi/besledigi: uzantılı yollar. Buraya yazdığın her dayanılan sayfanın besledigi alanına bu sayfayı ekle.
- Bu yorum bloğunu doldurduktan sonra sil.
-->

# Başlık

## Amaç
Bu sayfa … için var. (frontmatter `amac` ile birebir aynı cümle)

## İçerik
(türe göre alt başlıklar; tür şablonu belirler)

## Bağlar
### Dayandığı
- [[yol/sayfa]] — neden dayanıyor
### Beslediği
- [[yol/sayfa]] — neyi besliyor
### Gelen
- ← [[yol/sayfa]] — (başka sayfa buna bağlanınca otomatik değil, elle yazılır)

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | T-xxx | Oluşturuldu |
