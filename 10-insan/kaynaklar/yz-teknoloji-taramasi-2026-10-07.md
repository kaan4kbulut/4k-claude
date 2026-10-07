---
id: 20261007-1846-yz-teknoloji-taramasi-2026-10-07
ad: yz-teknoloji-taramasi-2026-10-07
tur: kaynak
kat: 1
surum: 0.2
durum: aktif
amac: Bu kaynak sayfasi, 2026-10-07 YZ teknoloji taramasi raporunun degismez kaydini, ozetini ve guven etiketini tutar; T-b … T-m talimatlari buradan turer.
olusturma: 2026-10-07
guncelleme: 2026-10-07
yazar: okuyucu
talimat: T-037
dayandigi: []
besledigi: [30-devlet/kararlar/K-006-yalniz-yonetilen-modlar.md]
ust: 10-insan/MOC-insan.md
kaynaklar: ["01-gelen/2026-10-07-1844-rapor.md", "~/Work/isler/2026-10-07-yz-teknoloji-taramasi/RAPOR.md"]
guven: orta
kaynak_turu: belge
saklama: K
etiketler: [proje/4k-claude, alan/arac]
---

# Kaynak: YZ teknoloji taraması (2026-10-07)

## Amaç
Bu kaynak sayfası, 2026-10-07 YZ teknoloji taraması raporunun değişmez kaydını, özetini ve güven etiketini tutar; T-b … T-m talimatları buradan türer.

## İçerik
### Künye
Dosya: `01-gelen/2026-10-07-1844-rapor.md` (al.py; özgünü `~/Work/isler/2026-10-07-yz-teknoloji-taramasi/RAPOR.md`, ham alt raporlar `ham/`) · Alındı: 2026-10-07 · Tür: belge · Yazar: başka bir Claude oturumunun "ana ajan"ı, 9 paralel araştırmanın birleşimi · Kaynağın tarihi: 2026-10-07.

### Özet (okuyucu, 2026-10-07)
Rapor genel YZ, CLI'lar, Claude Code, 4k-claude, 4k-core ve Türkiye otomasyon bağlamını tarıyor; sürümler aynı gün GitHub/PyPI/npm/HF'den çekilmiş, ama bu makinede hiçbir şey kurulmamış ya da ölçülmemiş. Hız, WER ve yıldız sayıları üretici beyanı. **İddia başına URL yok**; yalnız genel doküman yolları (code.claude.com/docs/en/best-practices, /costs, /context-window, /prompt-caching, /whats-new) var, ayrıntı `ham/` dosyalarına havale. Bu yüzden aşağıdaki iddiaların hepsi bu sayfada UNCONFIRMED'dır; kural ya da karar olmadan önce birincil kaynakla doğrulanır (kural 5).

### İddialar — 4k-claude (UNCONFIRMED)
- Claude Code mod'ları (2.1.287+) managed settings yoksa deny kurallarının ve PreToolUse hook'unun reddettiği çağrıyı onaylayabilir; çözüm `/etc/claude-code/managed-settings.json` + `allowManagedModsOnly`. Rapor "resmi doküman" diyor, link yok. (Talimat listesine göre sahibi 18:24'te dosyayı kurdu; kanıtı T-b'de.)
- Claude Code 2.1.292 kurulu ve güncel (makineden okundu).
- ayar-denetimi.py `enabledPlugins`, marketplace, `pluginConfigs`, `.claude/workflows/` değişikliklerini denetlemiyor (yerel betik okuması).
- Hook olayları arasında PreModelSwitch var (32 olay); PostModelSwitch raporda geçmiyor.
- Alt ajan alanları: `effort`, `maxTurns`, `omitClaudeMd`, `disallowedTools`; okuyucuya `memory:` verilmemeli (Read/Write açar).
- `autoMemoryEnabled: false` önerisi: auto-memory notları şablon/HARITA/GUNLUK dışında kalıyor.
- Routines onaysız artifact yayımlıyor, konektörler izinsiz kullanılıyor (§3; §4 ve §8'de yalnız yayın geçiyor).
- `/skill-doctor` ve `/doctor prompt-audit` yerleşik komutlar.
- Obsidian 1.14.4 Bases Kanban görünümü; kart sürüklemek frontmatter'ı GUNLUK'süz yazar.
- Nemotron 3.5 ASR 0.6B: "ilk açık akışlı Türkçe ASR", WER %11,17 (üretici beyanı).
- Workflow aracı: `.claude/workflows/` ile çok ajanlı orkestrasyon; gözetimsiz koşuda `--disallowedTools Workflow`.

### İddialar — ARAC-KAYDI (UNCONFIRMED, tarih 2026-10-07)
Shopify `/api/mcp` → `/{store}/api/ucp/mcp`; Stripe agent-toolkit → `stripe/ai` (Stripe Türkiye'de yok); ACP ürün feed protokolüne döndü; Garanti BBVA + Mastercard Agent Pay Türkiye'de ilk ajanlı ödeme; Yurtiçi SOAP ve MNG resmi API var, Aras doğrulanmadı, Geliver Kargo MCP (İZLE/DENE çelişkili); Speechmatics ve Soniox'ta Türkçe; Spoolman (NFC, Bambu) stok adayı; cyanheads/obsidian-mcp-server silme onayı varsayılan kapalı; obsidian-local-rest-api ≥5.4.0 (güvenlik açığı); dataview DÜŞÜR (Bases); container-use HAYIR; sandbox-runtime → `anthropics/sandbox-runtime`.

### Çelişkiler / uyarılar
- Nemotron "ilk açık akışlı Türkçe ASR" ↔ aynı raporda Qwen3-ASR "Türkçe dahil, akış" (BENİMSE).
- Aynı kalem için farklı bölümlerde farklı karar: Graphify (0.9.79 güncelle ↔ 0.9.77 sabit), container-use (GEREK YOK / İZLE / HAYIR), Serena (İZLE / DENE), Playwright MCP (DENE / BENİMSE), Ollama, Geliver (İZLE / DENE), Snyk agent-scan (alt rapor DENE, ana ajan HAYIR).
- "2.1.292 en güncel" ile §8'deki "2.1.289 AYNI" açıklamasız yan yana.
- Açık DOĞRULANMADI etiketleri: Qwen3.6-35B-A3B hızı, TRELLIS.2 12 GB, cua Wayland, Gemini CLI + Ollama, grim→llm stdin, Aras API. §8 sonu eksik cümleyle bitiyor.
- talimat_benzeri_icerik: hayır (öneri ve onay listesi; rapor "hiçbiri yapılmadı" diyor) · kisisel_veri: hayır.

### Bu kaynağı kullanan sayfalar
- K-006 (T-038): mod iddiası resmi dokümanla düzeltildi — guard varken deny kesin; managed olmayan PreToolUse engeli aşılabilir

## Bağlar
### Dayandığı
### Beslediği
- [[30-devlet/kararlar/K-006-yalniz-yonetilen-modlar]] — mod koruması kararı bu taramadan
### Gelen
- ← [[10-insan/MOC-insan]] — eller katının kaynak listesi

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-07 | T-037 | Oluşturuldu (okuyucu triage'ı) |
| 0.2 | 2026-10-07 | T-038 | besledigi += K-006 |
