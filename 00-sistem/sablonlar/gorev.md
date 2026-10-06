---
id: YYYYMMDD-HHMM-slug
ad: slug
tur: gorev
kat: 2
surum: 0.1
durum: aktif
amac: Bu gorev, ... icin ... uretmek uzere var (komutan niyeti: neden).
olusturma: YYYY-MM-DD
guncelleme: YYYY-MM-DD
yazar: claude
talimat: T-xxx
dayandigi: ["30-devlet/kararlar/K-xxx-....md"]
besledigi: []
ust: 20-sirket/MOC-sirket.md
kanban: bekliyor
kapi: cift-yonlu
sahip: orkestrator
inceleyici: denetci
devretme_seviyesi: 5
model_caba: sonnet/medium
butce: {tur: 25, usd: 2, zaman: "1 oturum"}
insan_noktalari: []
kanit: []
is_yasi_gun: 0
etiketler: []
---

<!--
GÖREV KARTI = 12 zorunlu alan (rules/20-sirket.md) + insan noktaları + kanıt.
- kanban: bekliyor → basladi → fiziksel-adim-bekliyor → kontrol → tamam | iptal. WIP tavanı 3.
- kanit BOŞKEN kanban tamam OLAMAZ (kontrol.py reddeder).
- insan_noktalari en başta beyan edilir: {id: HP-xxx, tur: fiziksel|odeme|imza|oauth|2fa|ilk-musteri-yaniti|diger, kosul: "...", kanit: "...", bekleyen_adim: N}
- devretme_seviyesi (Appelo): 1 söyle, 2 sat, 3 danış, 4 anlaş, 5 tavsiye et, 6 sor, 7 devret.
- İstem sırası: bağlam (girdiler) → kısıtlar (kapsam) → istek (kilit görevler + kabul ölçütleri) EN SONDA; alt ajan böyle okur.
- inceleyici ≠ sahip.
-->

# Görev G-xxx: <başlık>

## Amaç
Bu görev, … için … üretmek üzere var. (neden — komutan niyeti)

## İçerik
### 1. Girdiler ve bağlam
- [[30-devlet/kararlar/K-xxx-...]] — bu görevi doğuran karar
- [[yol]] — okunması gereken diğer sayfalar (yol ver, içerik yapıştırma)

### 2. Kapsam
- Dahil: (dosyalar / modüller / klasörler)
- Hariç: (açıkça yapılmayacaklar)
- Dokunma: (değiştirilmesi yasak dosyalar)

### 3. Araçlar, model, bütçe
İzinli araçlar: … · Model/çaba: sonnet/medium · Tur tavanı: 25 · Bütçe: 2 USD · Zaman kutusu: 1 oturum

### 4. Çıktı biçimi
… (biçim ve uzunluk tavanı; rapor ≤ 2.000 token)

### 5. Risk sınıfı ve eskalasyon
kapi: cift-yonlu | tek-yonlu · Eskale edilecekler: (hangi durumda DUR ve SOR)

### 6. İnsan noktaları (önceden beyan)
| id | tür | koşul | insan ne yapar | kanıt | bekleyen adım |
| --- | --- | --- | --- | --- | --- |
| HP-… | … | … | … | … | … |

### 7. Son durum (bitince gözlemlenebilir olan)
…

### 8. Kilit görevler (2-6; ne, nasıl değil)
1. …
2. …

### 9. Kabul ölçütleri (her biri test edilebilir; kanıt komutu yanında)
| # | Ölçüt | Kanıt komutu | Durum |
| --- | --- | --- | --- |
| 1 | … | `…` → 0 | bekliyor |

### Kanıt (kapanışta doldurulur)
| Komut | Çıkış | Özet |
| --- | --- | --- |
| … | … | … |

### Örtülü alınan kararlar (uygulama sırasında)
- (çift yönlü; sahibi itiraz ederse geri alınır)

### İnceleme (denetci)
KARAR: geçer | engelleyici-var (N) · tarih · engelleyiciler: …

## Bağlar
### Dayandığı
- [[30-devlet/kararlar/K-xxx-...]] — bu görevin yetki kaynağı
### Beslediği
- [[10-insan/ciktilar/...]] — bu görevin çıktısı
### Gelen

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | T-xxx | Oluşturuldu (bekliyor) |
