---
id: 20261006-2202-model-politikasi
ad: model-politikasi
tur: referans
kat: 3
surum: 0.1
durum: aktif
amac: Hangi isin hangi modele ve cabaya gidecegini, tur ve butce tavanlarini, onbellek ve maliyet disiplinini belirler; alt ajan tanimlari ve calistir.sh buna uyar.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: kaan
talimat: T-000
dayandigi: [30-devlet/normlar/ANAYASA.md, 00-sistem/arastirma/04-guvenilirlik-ve-kalite-teknikleri.md]
besledigi: []
kaynaklar: ["https://platform.claude.com/docs/en/about-claude/pricing", "https://code.claude.com/docs/en/model-config", "https://code.claude.com/docs/en/costs"]
alindi: 2026-10-06
saklama: S
etiketler: [norm/maliyet]
---

# Model politikası

Anayasa Madde 13: kaynaklar kıttır. Bu belge model seçimini, çabayı ve bütçeyi kurala bağlar. Fiyatlar resmi sayfadan (alındı 2026-10-06); çeyreklik yeniden kontrol.

## Amaç
Hangi işin hangi modele ve çabaya gideceğini, tur ve bütçe tavanlarını, önbellek ve maliyet disiplinini belirler; alt ajan tanımları ve calistir.sh buna uyar.

## İçerik

### Fiyat referansı (USD / milyon token; giriş / çıkış / önbellek okuma)
| Model | Giriş | Çıkış | Önbellek okuma | Not |
| --- | --- | --- | --- | --- |
| Fable 5.1 | 10 | 50 | 0.25 | En üst katman; yalnız kritik sentez |
| Opus 5.5 | 4 | 20 | 0.20 | Mimari, çok adımlı akıl, inceleme |
| Sonnet 5.5 | 2 | 10 | 0.20 | Varsayılan işçi; kodlama; alt ajan |
| Haiku 4.5 | 1 | 5 | 0.10 | Triage, okuyucu, hakem, özet |
Batch API %50 indirim; gece toplu özetler Batch'e. Abonelikte önbellek TTL 1 saat.

### Rol → model → çaba
| İş | Model | Çaba | maxTurns | Bütçe tavanı |
| --- | --- | --- | --- | --- |
| Orkestratör (ana oturum) | Oturumun modeli (Sonnet varsayılan; büyük işte Opus) | medium | — | oturum: 5 USD |
| Danışman işlevi: yönlendirme notu, steelman, pre-mortem | Opus | high | 20 | 3 USD |
| Plan / mimari karar hazırlığı | Opus | high | 20 | 3 USD |
| Uygulayıcı (kod, belge, görev kartı işleme) | Sonnet | medium | 25 | 2 USD |
| denetci (bağımsız inceleme) | Sonnet | medium | 15 | 1 USD |
| okuyucu (karantinalı okuma, triage) | Haiku | low | 12 | 0.3 USD |
| Hakem (3 oy, kapı yargısı) | Haiku ×3 | low | 5 | 0.3 USD |
| /uyku hafif | Sonnet | low | 15 | 1 USD |
| /uyku tam, aylık özet | Sonnet (sentez Opus) | medium | 30 | 3 USD |
| Araştırma alt ajanı (alan paketi) | Sonnet | medium | 30 | 2 USD |
| Gözetimsiz koşu (calistir.sh) | Sonnet; yedek Sonnet | medium | 30 | 2 USD |

### Kurallar
1. Tek ajanla yapılabilen iş için alt ajan açılmaz; ikinci ajan yalnız yalıtım (uzun çıktı), temiz bağlamlı inceleme ya da gerçek paralellik için.
2. Çaba katmanları: basit arama = 1 ajan, 3-10 araç çağrısı; karşılaştırma = 2-4 alt ajan, 10-15 çağrı; karmaşık araştırma = 10+ yalnız açık iş bölümüyle.
3. Her alt ajan çağrısı `maxTurns` ve bütçe taşır; brifte yazılır. Alt ajan harcaması ana bütçeden düşer.
4. Çok ajanlı iş sohbetin ~15 katı token tüketir; iş büyüklüğü kuralı bunun için vardır. Haftalık token toplamı SCORECARD'da izlenir.
5. Önbellek disiplini: CLAUDE.md ve rules sabit kalır; tarih ve durum SessionStart çıktısında. Alt ajanlar aynı önekle açılır.
6. Düşünme kapatılamaz (Opus/Sonnet/Fable); çaba `effort` ile ayarlanır.
7. Oturum tavanı aşılırsa iş durur, `[durdu]` yazılır, sahibine bütçe kapısı açılır (A5).
8. Model yoksa yedek Sonnet; Haiku'ya düşme yalnız triage için.
9. Maliyet SessionEnd hook'u ile MALIYET.csv'ye; aylık toplam haftalık gözden geçirmede.

### Yeniden kontrol
Fiyatlar ve model adları çeyreklik kontrol edilir (TAZELIK 90 gün); değişiklik `/degistir` ile, sürüm artar.

## Bağlar
### Dayandığı
- [[30-devlet/normlar/ANAYASA]] — Madde 13 kaynak ve maliyet
- [[00-sistem/arastirma/04-guvenilirlik-ve-kalite-teknikleri]] — fiyatlar, yönlendirme kuralları, önbellek
### Beslediği
### Gelen
- ← [[30-devlet/normlar/ANAYASA]] — Madde 13'ün ayrıntısı

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-06 | T-000 | Oluşturuldu |
