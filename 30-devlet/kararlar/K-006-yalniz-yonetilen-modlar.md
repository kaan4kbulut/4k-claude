---
id: 20261007-1850-k-006-yalniz-yonetilen-modlar
ad: k-006-yalniz-yonetilen-modlar
tur: karar
kat: 3
surum: 1.0
durum: kabul
amac: Bu karar kaydi, makine duzeyi managed settings ile yalniz yonetilen Claude Code mod'larinin yuklenmesi kararini, gerekcesini, kanitini ve izleme yolunu kalici olarak tutmak icin var.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: claude
talimat: T-038
dayandigi: [10-insan/kaynaklar/yz-teknoloji-taramasi-2026-10-07.md]
besledigi: [30-devlet/normlar/IMZA-MATRISI.md, 10-insan/araclar/ARAC-KAYDI.md]
ust: 30-devlet/MOC-devlet.md
kapi: cift-yonlu
karar_veren: kaan
danisilan: [claude]
bilgilendirilen: []
beklenen_sonuc_olasilik: 90
gozden_gecir: 2026-11-07
saklama: S
kaynaklar: ["https://code.claude.com/docs/en/plugins/mods/admin"]
alindi: 2026-10-07
etiketler: [karar/guvenlik, arac/claude-code]
---

# Karar K-006: Yalnız yönetilen mod'lar (managed settings)

## Amaç
Bu karar kaydı, makine düzeyi managed settings ile yalnız yönetilen Claude Code mod'larının yüklenmesi kararını, gerekçesini, kanıtını ve izleme yolunu kalıcı olarak tutmak için var.

## İçerik
### Bağlam ve problem
Claude Code v2.1.286'dan beri mod'lar varsayılan açık. Resmi dokümana göre (https://code.claude.com/docs/en/plugins/mods/admin, okundu 2026-10-07, okuyucu):
- Mod'lar sandbox'lı değildir ("Mods aren't sandboxed"); kullanıcının yetkileriyle çalışır.
- Koruma (guard) yüklüyken bir mod `deny` kuralının reddettiği çağrıyı onaylayamaz; ama `ask` kuralını ve **managed settings dışındaki PreToolUse hook'unun engelini** aşabilir ("can approve a call … that a `PreToolUse` hook outside managed settings blocked").
- Guard, managed settings varsa ya da Team/Enterprise girişi varsa yüklenir; yoksa bu koruma uygulanmaz.
4k-claude'un yazma korumaları (`yikici-koruma`, `kasa-disi-koruma`, `durus-kapisi`) proje/kullanıcı düzeyi PreToolUse hook'larıdır, managed değildir. Yani kullanıcının ya da bir Claude oturumunun yazdığı bir mod bu hook'ların engelini kaldırabilirdi.
Not: tarama raporunun "mod'lar deny kurallarını aşabilir" iddiası resmi dokümanla **çelişir** (guard varken deny kesindir); "yerel hook engelini aşar" kısmı doğrudur.

### Karar sürücüleri
- Anayasa ilke 6: korumalar metinde değil, araçta olmalı.
- Koruma hook'ları bir mod tarafından sessizce aşılmamalı.
- Sahibinin talimatı (2026-10-07, YZ taraması sonrası).

### Seçenekler
| # | Seçenek | Artı | Eksi | Maliyet / token | Risk |
| --- | --- | --- | --- | --- | --- |
| A | Managed settings: `allowManagedModsOnly: true` | Kullanıcı/`--plugin-dir`/Claude yazımı mod'lar yüklenmez; guard yüklenir | Kendi mod'umuzu denemek root ister | Yok | Düşük |
| B | Hook'ları managed settings'e taşımak | Hook engeli mod'a karşı da kesin | Her hook değişikliği root ister; proje taşınabilirliği düşer | Orta | Bakım yükü |
| 0 | Hiçbir şey yapma | — | Bir mod koruma hook'larını aşabilir | Yok | Yüksek |

### Karar
**Makine düzeyi managed settings ile yalnız yönetilen mod'lar yüklenecek** (seçilen: A). Sahibi 2026-10-07 18:24'te kurdurdu:
`/etc/claude-code/managed-settings.json` → `{"pluginConfigs":{"cc-plugin-sec-default@builtin":{"options":{"allowManagedModsOnly":true}}}}`
Kurallar:
- `allowModsToOverrideDenyRules` açılmaz (açılırsa mod `deny`'ı da aşar).
- Dosya değişikliği makine düzeyi ayardır: imza A12 (IMZA-MATRISI), root ister; Claude yazamaz (sandbox `denyWithinAllow`).
- B seçeneği (hook'ları managed'a taşımak) gerekirse ayrı karar.

### Kanıt
- `cat /etc/claude-code/managed-settings.json` (2026-10-07 18:47) → yukarıdaki içerik; değişiklik zamanı 18:24.
- `claude --version` → 2.1.292.
- Anahtar yolu ve etkisi resmi dokümanla doğrulandı (okuyucu, 2026-10-07). Linux'taki dosya yolu bu sayfada geçmiyor (`/docs/en/managed-settings`'e yönlendiriyor): UNCONFIRMED. Talimat listesindeki "debug günlüğünde 'seated outermost' görüldü" beyanı bu oturumda `~/.claude/debug/` içinde bulunamadı: UNCONFIRMED.

### Beklenen sonuç
Kullanıcı ya da Claude tarafından yazılmış bir mod yüklenmez; koruma hook'ları mod yoluyla aşılamaz. Olasılık %90; belirsizlik: Linux yolunun doğrulanmamış olması (dosya yanlış yerdeyse guard yüklenmez).

### Sonuçlar
- İyi: koruma hook'larının mod'a karşı açığı kapanır.
- Kötü: kendi mod denemesi için root ve managed ayar gerekir.
- Nötr / bilinmeyen: guard'ın gerçekten yüklendiği bu oturumda gözlenmedi.

### İzleme
- ayar-denetimi (SessionStart) dosyanın varlığını ve `allowManagedModsOnly: true` değerini denetlesin; yoksa uyarı + GUNLUK `[ayar]` (uygulama: liste T-c, ayar-denetimi genişletmesi).
- Linux yolunu `/docs/en/managed-settings` ile doğrula (T-c içinde).

## Bağlar
### Dayandığı
- [[10-insan/kaynaklar/yz-teknoloji-taramasi-2026-10-07]] — riski ilk bildiren tarama (iddia burada düzeltildi)
### Beslediği
- [[30-devlet/normlar/IMZA-MATRISI]] — A12 satırı bu karara dayanır
- [[10-insan/araclar/ARAC-KAYDI]] — managed settings satırı
### Gelen
- ← [[30-devlet/MOC-devlet]] — kararlar listesi

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 1.0 | 2026-10-07 | T-038 | Oluşturuldu; karar sahibinin, kurulum 18:24 |
