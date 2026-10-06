---
id: YYYYMMDD-HHMM-slug
ad: slug
tur: sop
kat: 2
surum: 0.1
durum: taslak
amac: Bu SOP, ... isinin her seferinde ayni kalitede ve ayni kayitla yapilmasi icin adimlari, karar noktalarini ve kontrol listesini belirler.
olusturma: YYYY-MM-DD
guncelleme: YYYY-MM-DD
yazar: claude
talimat: T-xxx
dayandigi: []
besledigi: []
ust: 20-sirket/MOC-sirket.md
sahip: orkestrator
raci: {R: "", A: "", C: [], I: []}
insan_noktalari: []
gozden_gecirme: YYYY-MM-DD
etiketler: []
---

<!--
SOP = EPA QA/G-6 yapısı + BPMN kulvar/gateway mantığı + Gawande kontrol listesi.
- Her adımda: kim (ajan/insan), araç, beklenen çıktı, YAN ETKİ SINIFI: inspect | external-read | local-change | external-write | approval-required.
- approval-required adım ASK.md olmadan geçilemez.
- Kontrol listesi: DO-CONFIRM (yaptın, duraklayıp doğrula) ya da READ-DO (oku, yap); duraklama noktası başına 5-9 madde; yalnız kritik maddeler.
- gozden_gecirme ≤ 12 ay.
-->

# SOP-xxx: <başlık>

## Amaç
Bu SOP, … işinin her seferinde aynı kalitede ve aynı kayıtla yapılması için adımları, karar noktalarını ve kontrol listesini belirler.

## İçerik
### Kapsam ve uygulanabilirlik
(hangi durumda uygulanır, hangi durumda uygulanmaz)

### Tanımlar
- …

### Ön koşullar
- Girdiler: … · Araçlar/erişimler: … · Yetki: (hangi yönerge)

### Güvenlik / uyarılar
(fiziksel adımlar için zorunlu; dijital için veri/sır uyarıları)

### Roller (RACI)
R: … · A: … (tek) · C: … · I: …

### Adımlar
| # | Adım | Kim | Araç | Beklenen çıktı | Yan etki sınıfı |
| --- | --- | --- | --- | --- | --- |
| 1 | … | ajan | … | … | inspect |
| 2 | … | ajan | … | … | local-change |
| 3 | … | insan | — | … | approval-required |

### Karar noktaları (gateway)
| Noktada | Koşul | Yol | Yetki |
| --- | --- | --- | --- |
| Adım N | … | → adım M / → eskale | tek başına / eskale |

### Durma noktaları ve kontrol listesi
**Durma noktası A (adım N sonrası) — DO-CONFIRM**
- [ ] …
- [ ] …

### Kayıtlar
(hangi dosyaya ne yazılır: kart alanı, HARITA, GUNLUK, çıktı sayfası)

### Definition of Done
- …

### KPI
- (bu SOP'un ölçtüğü 1-3 gösterge)

### İstisnalar ve eskalasyon
- …

### Referanslar
- [[yol]] — …

## Bağlar
### Dayandığı
### Beslediği
### Gelen

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | T-xxx | Oluşturuldu |
