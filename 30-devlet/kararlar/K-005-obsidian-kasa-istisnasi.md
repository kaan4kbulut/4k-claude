---
id: 20261007-1124-k-005-obsidian-kasa-istisnasi
ad: k-005-obsidian-kasa-istisnasi
tur: karar
kat: 3
surum: 1.0
durum: kabul
amac: Bu karar kaydi, Obsidian'in kok dizinde actigi .obsidian/ ayar klasorunun kural 7'ye dar bir istisna olarak git disinda tutulmasini, alternatifleri ve dogrulama yolunu kalici olarak tutmak icin var.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-024
dayandigi: [10-insan/araclar/ARAC-KAYDI.md]
besledigi: []
ust: 30-devlet/MOC-devlet.md
kapi: cift-yonlu
karar_veren: kaan
danisilan: [claude]
bilgilendirilen: []
beklenen_sonuc_olasilik: 85
gozden_gecir: 2026-11-07
saklama: S
etiketler: [karar/arac, arac/obsidian]
---

# Karar K-005: Obsidian kasası için `.obsidian/` dar istisnası

## Amaç
Bu karar kaydı, Obsidian'ın kök dizinde açtığı `.obsidian/` ayar klasörünün kural 7'ye dar bir istisna olarak git dışında tutulmasını, alternatifleri ve doğrulama yolunu kalıcı olarak tutmak için var.

## İçerik
### Bağlam ve problem
Web Clipper insan noktası (ARAC-KAYDI, T-012) bu klasörün Obsidian kasası olarak açılmasını ister. Obsidian kasayı açınca köke `.obsidian/` ayar klasörünü yazar ve sürekli günceller. CLAUDE.md kural 7 yazmayı kat klasörleri, 00-sistem, 01-gelen, 90-arsiv ve .claude ile sınırlar; `.gitignore` bu klasörü bilmediği için git durumu da kirlenir. Ayrıca Obsidian varsayılan olarak yeni notları ve ekleri köke koyar; bu da kat dışı dosya doğurur.

### Karar sürücüleri
- Kural 7 (kat dışına yazma yok) ve kural 2 (haritasız dosya yok) bozulmamalı.
- Sahibinin Web Clipper ve Obsidian ile çalışabilmesi (ARAC-KAYDI insan noktası).
- Geri alınabilirlik: Y-001 Madde 2.2 (proje içi, git ile geri alınabilir değişiklik); sahibinin sohbet onayı (2026-10-07).

### Seçenekler
| # | Seçenek | Artı | Eksi | Maliyet / token | Risk |
| --- | --- | --- | --- | --- | --- |
| A | `.obsidian/` git dışı + dar istisna + yeni not/ek yolu `01-gelen` ön ayarı | Kural metni değişmez; git temiz; yeni notlar inbox'a düşer | Obsidian ayarları sürümlenmez | Çok düşük | Obsidian ön ayarı yok sayarsa notlar köke düşer |
| B | Kasayı ayrı bir klasörde açıp yalnız `01-gelen`'i oraya bağlamak (symlink) | Kök hiç değişmez | Sahibi wiki'yi Obsidian'da göremez; symlink kırılgan | Düşük | Senkron/bağ hatası |
| C | `.obsidian/`'ı git'e almak | Ayarlar sürümlenir | workspace.json sürekli değişir, commit gürültüsü | Düşük | Durmadan kirli çalışma ağacı |
| 0 | Hiçbir şey yapma | Emek yok | Git kirli; kural 7 belirsiz; notlar köke düşer | Yok | Bütünlük ve git karmaşası |

### Karar
**`.obsidian/` klasörünü git dışı tutacağız ve kural 7'ye dar istisna sayacağız**, çünkü bu klasör sahibinin aracının ayar klasörüdür, wiki sayfası değildir ve tarama betikleri (yscommon `TARANAN`, `IZ_KOKLER`) onu zaten görmez. İstisnanın sınırları:
- Claude `.obsidian/` içine yalnız bu kararla belirlenen ön ayarı (`app.json`: yeni not ve ek yolu `01-gelen`) yazar; başka ayara dokunmaz.
- `.obsidian/` içinde `.md` sayfa tutulmaz; kök dizine başka Obsidian dosyası istisnaya girmez.
(seçilen: A)

### Beklenen sonuç
Kasa açıldıktan sonra `git status` temiz kalır ve `kontrol.py` sıfır hata verir; olasılık %85; gerekçe: Obsidian nokta ile başlayan klasörleri dizinlemez, betikler köke bakmaz; belirsizlik `app.json` anahtarlarının Obsidian sürümünce aynen okunması (UNCONFIRMED, ilk açılışta doğrulanır).

### Sonuçlar
- İyi: Web Clipper kurulumunun önü açılır; kural metni ve betikler değişmeden kalır.
- Kötü: Obsidian ayarları yedeklenmez (git dışı).
- Nötr / bilinmeyen: Sahibi Obsidian'da boş not açarsa not `01-gelen`'e frontmatter'sız düşer ve /inbox-triage işleyene kadar kontrol.py onu raporlar.

### Doğrulama
`git check-ignore .obsidian/app.json` çıkış 0 · kasa ilk açıldıktan sonra `git status --short` ve `kontrol.py --kisa` · ne zaman: ilk açılış ve 2026-11-07 · kim: orkestratör.

### Kapı ve roller
kapi: cift-yonlu · karar veren: kaan (sohbet onayı, 2026-10-07) · danışılan: claude · bilgilendirilen: —

## Bağlar
### Dayandığı
- [[10-insan/araclar/ARAC-KAYDI]] — Web Clipper insan noktası kasa olarak bu klasörü istiyor
### Beslediği
### Gelen
- ← [[30-devlet/MOC-devlet]] — kararlar listesi

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 1.0 | 2026-10-07 | T-024 | Oluşturuldu ve kabul (sahibinin sohbet onayı) |
