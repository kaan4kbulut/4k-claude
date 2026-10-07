---
id: YYYYMMDD-HHMM-slug
ad: slug
tur: kapi
kat: 3
surum: 0.1
durum: aktif
amac: Bu kapi kaydi, ... karari icin onay surecini, kriterleri ve sonucu tutmak icin var.
olusturma: YYYY-MM-DD
guncelleme: YYYY-MM-DD
yazar: claude
talimat: T-xxx
dayandigi: []
besledigi: []
ust: 30-devlet/MOC-devlet.md
kapi_turu: G3
kapi: tek-yonlu
karar_veren: kaan
bekci: kaan
sonuc: bekliyor
saklama: K
etiketler: []
---

<!--
KAPI = Stage-Gate: teslimatlar + kriterler (zorunlu ikili / istenen puanlı) + sonuç (go/kill/hold/recycle) + tek bekçi.
- kapi_turu: G0 brif (bekçi orkestratör), G1 plan (bekçi sahibi tek yönlüde / orkestratör), G2 DoD+inceleme (bekçi denetci), G3 yayın/dış eylem (bekçi sahibi), adhoc.
- Sahibinin kararı gerekiyorsa ASK.md yazılır ve tur biter; cevap gelince sonuc doldurulur, ASK.md silinir.
- Onay Dosyası ≤ yarım sayfa (~250 kelime). Aşıyorsa karar olgun değil.
-->

# Kapı KP-xxx: <başlık>

## Amaç
Bu kapı kaydı, … kararı için onay sürecini, kriterleri ve sonucu tutmak için var.

## İçerik
### Gerekli teslimatlar
- [[yol]] — hazır mı: evet/hayır
- A10 (yeni araç / eklenti / mod / MCP) kapısında ek teslimat: `claude plugin validate --json <dizin>` çıktısı (çıkış kodu + hooks:/calls: satırları; eklentinin hangi hook'a bağlandığı ve neyi çağırdığı). Yerel kanıttır; içerik dışarı gönderilmez (Snyk agent-scan yerine, T-039).

### Zorunlu kriterler (ikili)
| Kriter | Karşılandı |
| --- | --- |
| … | evet / hayır |

### İstenen kriterler (puanlı 0-3)
| Kriter | Puan | Not |
| --- | --- | --- |
| … | … | … |

### Onay Dosyası (≤ yarım sayfa)
**İstenen karar:** … (tek cümle, eylem odaklı)
**Gerekçe:** …
**Alternatifler:** A) … B) … C) yapma — …
**Etki:** maliyet/token …, süre …, geri alınabilirlik …
**Risk ve azaltma:** …
**Uygulama sorumlusu:** …
**Danışman / Denetim görüşü:** … (≤ 3 cümle)
**Bu kararı bilmeden verirsen ne olur:** …

### ASK (sahibine tek soru)
Soru: …
Varsayılan (cevap gelmezse): …
Seçenekler: A) … B) … C) …
Son tarih: …

### Sonuç
sonuc: bekliyor | go | kill | hold | recycle · tarih: … · gerekçe: … · disagree-and-commit: evet/hayır

## Bağlar
### Dayandığı
- [[yol]] — kapıya gelen iş (talimat, karar, fikir)
### Beslediği
### Gelen

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | T-xxx | Kapı açıldı |
