---
id: 20261006-2348-k-003-ad-degisikligi-4k-claude
ad: k-003-ad-degisikligi-4k-claude
tur: karar
kat: 3
surum: 1.0
durum: kabul
amac: Bu karar kaydi, sistemin adinin sahibinin istegiyle Yeni Sistem yerine 4k-claude olmasini ve Anayasa'daki ad degisikliginin Madde 14 usulune dayanagini kalici olarak tutar.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: kaan
talimat: T-006
dayandigi: [30-devlet/normlar/ANAYASA.md]
besledigi: []
ust: 30-devlet/MOC-devlet.md
kapi: cift-yonlu
karar_veren: kaan
danisilan: [claude]
bilgilendirilen: []
beklenen_sonuc_olasilik: 95
gozden_gecir: belirlenmedi
saklama: S
etiketler: [karar/ad]
---

# Karar K-003: Sistemin adı 4k-claude

## Amaç
Bu karar kaydı, sistemin adının sahibinin isteğiyle Yeni Sistem yerine 4k-claude olmasını ve Anayasa'daki ad değişikliğinin Madde 14 usulüne dayanağını kalıcı olarak tutar.

## İçerik
### Bağlam ve problem
"Yeni Sistem" geçici bir çalışma adıydı. Sahibi 2026-10-06 tarihinde sistemin adını "4k-claude" olarak belirledi. Ad, Anayasa'nın girişinde, Amaç bölümünde ve Madde 1'de geçiyor; Anayasa yalnız sahibi tarafından, Madde 14 usulüyle değişir.

### Karar sürücüleri
- Sahibinin açık isteği (ad bir sahip kararıdır).
- Anlam değişmemeli: katlar, ilkeler, yetkiler aynı kalır.
- Kayıt bütünlüğü: GUNLUK salt eklemelidir; tarihî metin yeniden yazılmaz.

### Seçenekler
| # | Seçenek | Artı | Eksi | Maliyet | Risk |
| --- | --- | --- | --- | --- | --- |
| A | Canlı dosyalarda ad değişir, tarihî kayıtlar kalır | Kayıt dürüst kalır; sistem yeni adıyla konuşur | Eski raporlarda eski ad görünür | düşük | yok denecek kadar az |
| B | Her yerde (GUNLUK ve raporlar dahil) değiştir | Tek tip görünüm | Salt ekleme ilkesini ve kaynak değişmezliğini bozar | düşük | denetim izi bozulur |
| 0 | Ad değişmez | — | Sahibinin isteği yerine gelmez | — | — |

### Karar
**Sistemin adı 4k-claude olur; canlı dosyalar ve klasör adı değişir, tarihî kayıtlar değişmez** (seçenek A), çünkü ad sahibinin kararıdır ve salt ekleme ilkesi korunmalıdır.

### Beklenen sonuç
Ad değişikliği anlamı etkilemeden tamamlanır; kontrol.py sıfır hata; olasılık %95.

### Sonuçlar
- İyi: sistem kalıcı adını alır.
- Kötü: eski Claude Code oturum geçmişi eski klasör yoluna bağlı kalır (`claude --resume` yeni klasörde eski oturumları listelemez).
- Nötr: arşiv niteliğindeki metinlerde "Yeni Sistem" geçmeye devam eder.

### Doğrulama
`grep -rI "Yeni Sistem"` canlı dosyalarda boş; `kontrol.py --kisa` → 0.

### Kapı ve roller
kapi: cift-yonlu · karar veren: kaan · danışılan: claude · bilgilendirilen: —

## Bağlar
### Dayandığı
- [[30-devlet/normlar/ANAYASA]] — Madde 14 değişiklik usulü; ad giriş, Amaç ve Madde 1'de geçer
### Beslediği
### Gelen
- ← [[30-devlet/MOC-devlet]] — kararlar listesi

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 1.0 | 2026-10-06 | T-006 | Sahibinin isteğiyle kabul edildi |
