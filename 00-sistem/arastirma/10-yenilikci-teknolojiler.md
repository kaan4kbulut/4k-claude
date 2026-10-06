---
id: 20261006-2355-arastirma-10
ad: yenilikci-teknolojiler
tur: kaynak
kat: 0
surum: 1.1
durum: aktif
amac: 4k-claude'a eklenebilecek yenilikçi YZ araç ve teknolojilerini (bilgi grafı, yerel arama, ses hattı, belge alma, gözlemlenebilirlik, değerlendirme, otomasyon, sandbox, eller, görselleştirme) Ekim 2026 durumuyla taramak; 09-github-taramasi'nda verilen kararları tekrar etmeden yalnız yeni olanı ve durumu değişeni etiketlemek.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-007
dayandigi: [00-sistem/arastirma/09-github-taramasi.md, 00-sistem/arastirma/02-hafiza-ve-wiki-duzenleri.md, 00-sistem/arastirma/04-guvenilirlik-ve-kalite-teknikleri.md, 00-sistem/arastirma/05-eller-ve-alan-paketi-3d.md, 00-sistem/arastirma/08-ic-ses-yontemleri.md]
besledigi: [10-insan/araclar/ARAC-KAYDI.md, 30-devlet/kapilar/KP-001-sandbox-acilisi.md]
kaynaklar: ["https://github.com/Graphify-Labs/graphify", "https://pypi.org/project/graphifyy/", "https://github.com/tobi/qmd", "https://code.claude.com/docs/en/sandboxing", "https://code.claude.com/docs/en/hooks", "https://code.claude.com/docs/en/voice-dictation", "https://github.com/docling-project/docling", "https://github.com/lycheeverse/lychee", "https://github.com/snyk/agent-scan", "https://docs.livekit.io/agents/logic/turns/turn-detector/", "https://github.com/resemble-ai/chatterbox"]
alindi: 2026-10-06
guven: orta
kaynak_turu: urun-ve-repo-taramasi
saklama: K
---

# Yenilikçi YZ araçları ve teknolojileri (2026-10-06)

> Bu rapor bir taramadır, kurulum değildir. Öneriler sahibinin seçimiyle ayrı talimatlara döner; sandbox açmak ve yeni araç eklemek imza ister (IMZA-MATRISI). İç Ses ve gelen kutusu araçlarındaki Türkçe kalite ölçülmeden bağımlılığa çevrilmez.

## Amaç
4k-claude'a eklenebilecek yenilikçi YZ araç ve teknolojilerini Ekim 2026 durumuyla taramak; 09-github-taramasi'nda verilen kararları tekrar etmeden yalnız yeni olanı ve durumu değişeni etiketlemek.

## İçerik

**Yöntem.** Resmi repo, doküman, PyPI ve model kartı sayfaları 2026-10-06'da çekildi. Yıldız ve sürüm değerleri sayfanın o anki halidir. Çalışmanın bir kısmı paralel alt ajanlarla yürütüldü. Önerilere giren kritik iddiaları ana ajan birincil kaynaktan yeniden doğruladı; bunlar **[d]** ile işaretli: Graphify, qmd, sandbox, hook'lar, Obsidian CLI, basic-memory, ccusage, LiveKit, Chatterbox ve FreyaTTS. Geri kalanlar alt ajanların birincil kaynak okumasıdır. Yerel donanım ve kurulu araçlar komutla kontrol edildi: `bwrap`, `socat`, `rg`, `node`, `ffmpeg` ve `obsidian` kurulu; `uv`, `qmd`, `docling` ve `ccusage` yok. Claude Code 2.1.289. GPU: RTX 5070 Ti Laptop, 12 GB. Graphify 0.9.77 `~/Work/4k-core/eklentiler/graphify/venv` içinde zaten kurulu (ana ajan T-007'de yeniden doğruladı: `extractors/markdown.py` ağ kodu içermiyor, `input_tokens: 0` döndürüyor).

**Etiketler.** BENİMSE: doğrudan bağımlılık. ÖDÜNÇ AL: yalnız fikir ya da sözleşme. İZLE: henüz erken. UNCONFIRMED: birincil kaynakta doğrulanamadı.

## Öncelikli öneriler (10)

| # | Aday | Kat / yer | Etiket | Neden | Efor | İlk adım |
|---|---|---|---|---|---|---|
| 1 | Claude Code Bash sandbox'ı açmak (bubblewrap ve socat) | 00 / `.claude/settings.json` | BENİMSE (durumu değişti) | Bağımlılıklar artık kurulu. Kurulu değilse sandbox sessizce kapalı çalışır; `failIfUnavailable` bunu engeller. Kimlik bilgisi maskeleme de yeni. | S | İmzayla `sandbox.enabled: true`, `failIfUnavailable: true`, `allowUnsandboxedCommands: false`, `network.allowedDomains` boş başlatılır. Ardından `/sandbox` paneli kontrol edilir. |
| 2 | Graphify, yalnız kütüphane olarak ve LLM'siz | 00 / `00-sistem/scripts/graf.py` (yeni; `kontrol.py` ve `harita.py` yanına) | BENİMSE (kısıtlı) | Markdown çıkarıcısı deterministik: wikilink, frontmatter ve başlıkları LLM'siz grafa çevirir. Yetim sayfa, merkez düğüm ve topluluk tespiti `kontrol.py`'nin göremediği yapısal denetimi ekler. | M | Sahibin `yenile.py` desenini (allowlist + `extract()` + `to_json`) kopyala. Çıktı `00-sistem/graf/` altına gider, `.gitignore`'a eklenir. `graphify install` çalıştırılmaz. |
| 3 | qmd (yerel BM25 + vektör + reranker, MCP) | 00 / `.mcp.json` + ARAC-KAYDI; HARITA'dan sonra ikinci adım | BENİMSE (memsearch'ün yerine) | MIT lisanslı, yaklaşık 30k yıldız, tamamen yerel, stdio/HTTP MCP. memsearch'e göre çok daha olgun. | M | `QMD_EMBED_MODEL` Qwen3-Embedding-0.6B ile kurulur. Kat klasörleri ayrı koleksiyon olur. `01-gelen` hariç tutulur. 20 Türkçe sorguyla isabet ölçülür. |
| 4 | `ConfigChange` ve `PermissionDenied` hook'ları | 30 denetim / `.claude/hooks/ayar-denetimi.py` → GUNLUK | BENİMSE (yeni olay) | Ayar değişikliği exit 2 ile bloklanabiliyor. "Kural ile engel ayrıdır" ilkesini `.claude`'nin kendisine uygular. | S | `project_settings` ve `skills` eşleyicileriyle salt-ekleme GUNLUK satırı yazılır. İmzasız değişiklik bloklanır. |
| 5 | docling (+ docling-mcp); hafif yedek olarak markitdown | 00 / `01-gelen` → `inbox-triage` öncesi `00-sistem/scripts/al.py` | BENİMSE | MIT, yerel, ağsız çalışabilir. PDF, DOCX ve taranmış belgeyi markdown'a çevirir. Aktif: v2.134.0, bugün yayımlandı. | M | `uv tool install docling`. `01-gelen/ham/*.pdf` → `01-gelen/*.md` (frontmatter: kaynak, alindi). Okumayı yine `okuyucu` ajanı yapar. |
| 6 | lychee (bağlantı canlılık denetimi) | 00 / `kontrol.py` TAZELIK bölümü veya `/haftalik` | BENİMSE | "Web'den gelen her olgu URL taşır" kuralının canlılık yarısını deterministik denetler. Rust, Apache-2.0, yerel. | S | Haftada bir `lychee --format json 00-sistem/arastirma 40-ic-ses` çalıştırılır. Ölü URL'ler UNCONFIRMED'e düşürülür. |
| 7 | ccusage | 00 / `MALIYET.csv` mutabakatı, `/haftalik` | BENİMSE | MIT, yerel JSONL okur, `--offline` ve `--json` destekli. SessionEnd hook toplamlarını bağımsız bir kaynakla karşılaştırır. | S | `npx ccusage@latest daily --json --offline` çıktısı MALIYET.csv ile karşılaştırılır. Fark %5'i aşarsa GUNLUK'e `[durdu]` yazılır. |
| 8 | İç Ses ses hattı v1: `/voice` Türkçe + Chatterbox Multilingual V3 | 40 / `40-ic-ses` ses hattı; settings `language` | BENİMSE (/voice) · BENİMSE-deneme (Chatterbox) | `/voice` artık resmi olarak Türkçe destekliyor ve token tüketmiyor. Chatterbox MIT lisanslı, Türkçe doğrulanmış, 500M parametre; 12 GB GPU'ya sığar. | M | `"language": "turkish"`. Chatterbox ile 10 cümlelik Türkçe gecikme ve kalite testi yapılır, sonucu `arastirma-notlari`'na yazılır. |
| 9 | Snyk agent-scan (eski adı invariantlabs mcp-scan) | 30 / A10 araç ekleme kapısı → ARAC-KAYDI | BENİMSE | Yerel binary. MCP sunucularını ve skill'leri 14+ risk türü için tarar. Kayda girmeden önce kanıt üretir. | S | `/kapi` şablonuna "agent-scan çıktısı + çıkış kodu" kanıt alanı eklenir. |
| 10 | Gelen kutusu besleme: Obsidian Web Clipper + Syncthing-Fork | 00 / `01-gelen` | BENİMSE | Clipper resmi ve MIT; Syncthing-Fork resmi Android uygulamasının etkin halefi. İkisi de yerel ve buluta veri göndermiyor. | S | Clipper şablonu `01-gelen/` + frontmatter (`tur: kirpik`, `kaynak`, `alindi`). Telefon notları klasörü Syncthing ile `01-gelen/mobil/`'e eşlenir. |

## 1. Bilgi grafı ve hafıza

### Graphify (Graphify Labs) [d]
- **Ne yapar.** Bir klasörü (kod, doküman, PDF, görsel, video) sorgulanabilir bilgi grafına çevirir. Çıktılar: `graph.json`, `GRAPH_REPORT.md` (merkez düğümler, şaşırtıcı bağlar, önerilen sorular) ve `graph.html`. İsteğe bağlı olarak Obsidian vault, markdown wiki, GraphML ve Neo4j/FalkorDB dışa aktarımı yapar. MCP sunucusu `python -m graphify.serve graphify-out/graph.json` ile açılır; araçları `query_graph`, `get_node`, `get_neighbors` ve `shortest_path`'tir.
- **Yerel kaynakta doğrulanan.** Kurulu 0.9.77'nin `extractors/markdown.py` dosyası okundu. Markdown çıkarımı saf satır ayrıştırmasıyla yapılıyor ve `input_tokens: 0` dönüyor. Sayfa, başlık, `[[wikilink]]` ve `[metin](yol.md)` bağları alınıyor. Frontmatter sayfa düğümüne ekleniyor; frontmatter içindeki wikilink'ler de izleniyor. Kaynakta telemetri ya da analitik çağrısı bulunmadı; ağ kodu yalnız `llm.py`, `prs.py` ve `cli.py`'de. Sahibin `yenile.py`'si zaten "allowlist + AST, LLM yok" modunda çalışıyor.
- **Önemli boşluk.** 4k-claude'un `dayandigi` ve `besledigi` alanları düz yol listesi, wikilink değil. Graphify bunlardan kenar üretmez. Bu yüzden `graf.py` bu iki alanı networkx ile kendisi kenar olarak eklemeli. Böylece iki yönlülük ihlali ve yetim sayfa graf üzerinden ikinci kez denetlenir.
- **Yer.** `00-sistem/scripts/graf.py`, `kontrol.py` ve `harita.py`'nin yanına. Çıktı `00-sistem/graf/` altına gider ve git dışında tutulur. `/uyku` ve `/haftalik` "en zayıf bağlı 10 sayfa" ve "topluluk sınırını aşan bağ" listesini buradan okur. MCP sunucusu isteğe bağlı ve stdio üzerinden.
- **Lisans, maliyet.** Apache-2.0 + MIT (yerel METADATA). Kod ve markdown modu ücretsiz. `--mode deep` ile doküman, PDF ve görsel LLM'e gider; bu modda maliyet ve veri dışarı çıkışı vardır.
- **Çatışma.** `graphify install --project` şunları yapar: `.claude/CLAUDE.md`'ye blok yazar, `.claude/settings.json`'a PreToolUse hook'u ekler, `--strict` ile ham dosya okumayı bloklar ve `graphify hook install` ile post-commit ve post-checkout git hook'ları kurar. Bunlar HARITA-önce protokolüyle, `yikici-koruma.py` zinciriyle ve `.claude/**` için tanımlı `ask` kuralıyla çakışır. Bu yüzden **kurulum yapılmaz; yalnız kütüphane API'si kullanılır.**
- **Olgunluk.** PyPI'da 0.9.78, 2026-10-06; neredeyse günlük sürüm çıkıyor. GitHub sayfasında 124.4k yıldız ve yaklaşık 2.1k commit görünüyor. İkincil bir kaynak 74.8k yıldız ve YC S26 diyor; bu UNCONFIRMED. Hızlı sürüm temposu sürüm sabitlemeyi zorunlu kılıyor.
- **Etiket.** BENİMSE (kütüphane, LLM'siz). `install` / `--strict` / `--mode deep`: HAYIR.

### Rakipler ve güncel durum
| Aday | Durum (Eki 2026) | Uygunluk | Etiket |
|---|---|---|---|
| **basic-memory** [d] | AGPL-3.0, 4.1k yıldız, v0.23 (ön sürüm). Markdown-yerli: frontmatter, `- [kategori] gözlem` satırları, `ilişki [[Hedef]]`. Yerel SQLite ve FastEmbed. MCP'de `write_note`, `delete_note` ve `move_note` var. | Biçimi sisteme çok yakın, ama MCP üzerinden doğrudan yazar ve siler. Bu, şablon, HARITA ve GUNLUK zorunluluğunu by-pass eder. | ÖDÜNÇ AL ("ilişki türü + [[hedef]]" satır biçimi, `schema_validate` fikri) |
| zilliztech/memsearch | MIT, 2.7k yıldız, v0.4.21 (2026-09-24). Varsayılan gömme modeli bge-m3 ONNX; MCP UNCONFIRMED. | qmd daha olgun ve MCP'si var. | BENİMSE → ÖDÜNÇ AL'a düştü (gölge indeks fikri kalır) |
| topoteretes/cognee | Apache-2.0, ~31.5k yıldız, v1.6.2 (2026-09-29). MCP var. Varsayılan sağlayıcı OpenAI; Ollama ile yerel çalışabilir. | Markdown-yerli değil, altyapısı ağır. | İZLE |
| getzep/graphiti | Apache-2.0, ~31.5k yıldız, v0.30.2 (2026-09-08). Neo4j veya FalkorDB gerekir, varsayılan OpenAI. Telemetri açık, `GRAPHITI_TELEMETRY_ENABLED=false` ile kapanır. | Daha önce ÖDÜNÇ AL denmişti (geçerlilik penceresi); değişiklik yok. | — |
| letta / letta-code | letta 0.16.8 (2026-05-14) ve yavaşlıyor. letta-code v0.34.4 (2026-10-04); git tabanlı "MemFS" kullanıyor, varsayılan durum Letta Cloud'da. | Git-hafıza fikri sistemle zaten aynı. | İZLE |
| mem0 | Apache-2.0, ~66.7k yıldız. Varsayılan OpenAI. OpenMemory MCP UNCONFIRMED. | Veritabanı-öncelikli. | — (değişiklik yok) |
| HKUDS/LightRAG | MIT, ~40k yıldız, v1.5.7 (2026-09-02). LLM ve gömme sağlayıcısı gerekir. | İndeksleme LLM maliyeti getirir. | İZLE |
| microsoft/graphrag | v3.2.0 (2026-09-24). README "büyük ölçüde bakım modunda" diyor. İndeksleme pahalı. | — | HAYIR (durumu değişti) |
| thedotmack/claude-mem | ~97k yıldız, v13.34.2 (2026-10-06). Oturum sıkıştırması dış bir YZ ile yapılıyor (CMEM gözlemcisi, deneme süreli). | Veri dışarı çıkıyor. | HAYIR (önceki "opsiyonel" geri alındı) |
| GitNexus | PolyForm **Noncommercial**, 47.8k yıldız, 19 araçlı MCP. Odak kod; markdown dokümanları değil. | Lisans ticari kullanımı engelliyor. | HAYIR |

### Obsidian entegrasyonu
- **Resmi Obsidian CLI** [d]: masaüstü 1.12.4 sürümünde geldi (2026-02-27); önerilen sürüm 1.12.7+. Komutları: `create`, `read`, `search`, `property:set`, `base:query` ve ayrıca `delete`, `move`, `sync`, `publish`. **Uygulamanın çalışıyor olmasını gerektirir.** Sahibinde `obsidian` kurulu. Değeri Bases sorgusunu ve bağ çözümlemesini Obsidian'ın kendisine yaptırmasında. Risk: `delete` ve `publish` imza gerektiren eylemler. Bu yüzden `permissions.deny: ["Bash(obsidian delete*)", "Bash(obsidian publish*)", "Bash(obsidian sync*)"]` şart. Etiket: İZLE (GUI bağımlılığı), okuma komutları için ÖDÜNÇ AL.
- MCP sunucuları: MarkusPfundstein/mcp-obsidian (MIT, ~4.5k yıldız, sürüm yok), cyanheads/obsidian-mcp-server (Apache-2.0, v3.7.0, 2026-10-06), obsidian-local-rest-api 5.4.0 (2026-10-06). Hepsi Obsidian'ın açık olmasını ister. Kural "yerel CLI > MCP" olduğundan dosya sistemi + qmd yeterli. Etiket: İZLE.
- Smart Connections 4.7.2 (2026-08-06): lisans GitHub'da NOASSERTION görünüyor, yani UNCONFIRMED. qmd aynı işi ajan tarafında görüyor. Etiket: —.

## 2. Yerel arama ve indeksleme
- **tobi/qmd** [d]: MIT, 30.2k yıldız, v2.8.3 (2026-08-16; MCP 2026-07-28 revizyonu ve güvenlik sertleştirmesi). İlk kullanımda üç GGUF modeli `~/.cache/qmd/models/` altına indirir: EmbeddingGemma-300M (~300 MB), Qwen3-Reranker-0.6B (~640 MB) ve bir sorgu genişletme modeli (1.7B, ~1.1 GB). İşleme node-llama-cpp ile yerel. `qmd context add` ile yol bağlamı eklenebilir ("30-devlet = normlar ve kararlar" gibi); bu HARITA'nın tek satır özetleriyle örtüşüyor. **Yer:** `.mcp.json` (stdio) + ARAC-KAYDI; HARITA'dan sonra ikinci arama adımı. **Risk:** Varsayılan gömme modeli İngilizce ağırlıklı. Türkçe için `QMD_EMBED_MODEL=hf:Qwen/Qwen3-Embedding-0.6B-GGUF/...` gerekir; Türkçe isabeti UNCONFIRMED ve ölçülmeli. Etiket: **BENİMSE**.
- **Gömme modeli seçimi (Türkçe).** TR-MTEB (EMNLP 2025 Findings) bulgusu: genel sıralamada multilingual-E5 önde, Türkçe'ye özel modeller henüz geçemiyor. Adaylar: Qwen3-Embedding-0.6B (Apache-2.0, 32K bağlam), bge-m3 (MIT, 8192 token, yoğun + seyrek + çoklu vektör), multilingual-e5-large (MIT, 512 token sınırı), EmbeddingGemma-300M (Gemma lisansı, OSI değil). Öneri: Qwen3-0.6B ve bge-m3 kendi notlarımızla karşılaştırılsın. Etiket: ÖDÜNÇ AL (ölçüm protokolü).
- **asg017/sqlite-vec**: Apache/MIT, ~8.2k yıldız, sürüm 1.0 öncesi. Kendi betiğimizi yazarsak doğru yapı taşı, ama qmd varken gerek yok. Etiket: İZLE.
- 2026'nın yeni markdown-vault MCP'leri (cxrobx/vault-mcp, wirux/mcp-markdown-vault, mikebronner/markdown-vault-mcp): lisans, yıldız ve sürüm UNCONFIRMED; aynı adlı çatallar var. Etiket: UNCONFIRMED.

## 3. İç Ses ses hattı
**Durumu değişenler**
- **Claude Code `/voice`** (resmi doküman): Türkçe (`tr`) resmi listedeki 20 dilden biri. `language` ayarını izler; boşsa İngilizce kullanır. Dikte yapar, sohbet değil. Ses transkripsiyon için Anthropic'e gider ve claude.ai girişi gerekir. Transkripsiyon token tüketmez. 15 saniye sessizlikte ya da 2 dakikada durur. Linux'ta `arecord` veya SoX'a geri düşer. **Yer:** `.claude/settings.json` `"language": "turkish"`; İç Ses DİNLE modunda kısa girdi için. Etiket: **BENİMSE**.
- **Claude uygulaması sesli mod**: yardım sayfası İngilizce dışı dillerin beta olduğunu söylüyor; Türkçe adıyla geçmiyor, yani UNCONFIRMED. Uygulamanın dil menüsünden bakmak en kısa doğrulama.
- **Anthropic'in resmi gerçek zamanlı konuşma API'si**: bulunamadı (UNCONFIRMED). Sesli sohbet için Claude API'nin çevresine STT ve TTS kendimiz kurmalıyız.

**Sıra algılama**
- **LiveKit multilingual turn detector** [d]: Türkçe destekleniyor; doğru pozitif %99.3, doğru negatif %87.3. CPU'da yerel çalışır, 500 MB'tan az RAM ister. Lisans "LiveKit Model License" (OSI değil). livekit-agents 1.8.5 (2026-10-06), Apache-2.0. WebRTC ve sunucu odaklı olduğu için tek kişilik yerel döngü için ağır. Etiket: İZLE (model tek başına ÖDÜNÇ AL). Smart Turn v3.2 kararı geçerli.
- **Pipecat** v1.12.0 (2026-09-26): Anthropic LLM servisi ile yerel Whisper, Kokoro ve Piper servisleri var. Lisans UNCONFIRMED. İç Ses için "mikrofon → Smart Turn → whisper → Claude → TTS" döngüsünün en kısa yolu. Etiket: İZLE (prototip T-xxx olarak).

**TTS (Türkçe)**
| Aday | Türkçe | Lisans / yer | Not | Etiket |
|---|---|---|---|---|
| **Chatterbox Multilingual V3** [d] | Evet (`tr`, 23 dil) | MIT, yerel, 500M parametre, 26.8k yıldız | 12 GB GPU'ya sığar. Ses klonlama var; sahibinin sesini klonlamak bir karar konusu. Gerçek zamanlı hızı UNCONFIRMED. | BENİMSE-deneme |
| **FreyaTTS-small** [d] | Türkçe-öncelikli | Apache-2.0, 183M parametre, RTF 0.10–0.11, dizüstü CPU'da gerçek zamanlı, 1.5 GB VRAM. 0.1.0 (2026-07), 164 yıldız | Yeni ve küçük topluluk. | İZLE |
| Piper (OHF-Voice/piper1-gpl) | `tr_TR` (dfki) | GPL-3.0, yerel; bakımcı aranıyor | Robotik ses, ama en hafif seçenek. | Yedek |
| XTTS-v2 (idiap çatalı) | UNCONFIRMED | Kod MPL-2.0, ağırlıklar CPML (ticari olmayan) | — | HAYIR |
| Kokoro, F5-TTS, Dia, Kyutai TTS | Yok veya UNCONFIRMED | — | — | HAYIR |
| ElevenLabs (Flash v2.5, v3; v4 sayfada geçiyor) | Evet | Bulut; $0.011–0.08 / 1K karakter; Scribe v2 Realtime $0.39/sa | Veri dışarı çıkar. | Bulut yedeği |
| Cartesia Sonic 3.6 | Evet (44 dil) | Bulut; Pro $5/ay | — | Bulut yedeği |
| Gemini 3.8 Flash TTS | Evet | Bulut; fiyat UNCONFIRMED | — | İZLE |

**ASR (durumu değişen).** Açık gerçek zamanlı modellerin hiçbirinde Türkçe yok: Kyutai STT (en/fr), Parakeet v3 ve Canary v2 (25 Avrupa dili), Voxtral Realtime (13 dil), Cohere Transcribe 03-2026 (14 dil). Yerelde Whisper ailesi (BuzzASR/turkish) kararı geçerli. Türkçe'si doğrulanan bulut seçenekleri: AssemblyAI Universal-3.6 Pro Streaming, ElevenLabs Scribe v2 Realtime, Speechmatics (gerçek zamanlı modu UNCONFIRMED). Soniox'un Türkçe'si UNCONFIRMED.

**Wayland dikte.** Handy kararı geçerli. Alternatifler: **voxtype** (MIT, ~1.6k yıldız, Hyprland, CUDA, Arch için belgeli) ve **hyprwhspr** (MIT, AUR, Waybar). İkisi de whisper ile `language=tr` destekliyor. Etiket: İZLE (Handy sorun çıkarırsa voxtype).

## 4. Belge alma ve gelen kutusu besleme
| Aday | Ne / durum | Yer | Risk | Etiket |
|---|---|---|---|---|
| **docling** + docling-mcp | MIT; v2.134.0 ve docling-mcp v3.3.0 (ikisi de 2026-10-06); ~68.5k yıldız; ağsız çalışabilir | `00-sistem/scripts/al.py`: `01-gelen/ham/` → `01-gelen/*.md` | Model indirme boyutu; Türkçe OCR UNCONFIRMED | **BENİMSE** |
| markitdown (+ markitdown-mcp) | MIT, v0.1.8 (2026-09-21); hafif Office/HTML dönüştürücü | Aynı betikte hafif yol | İsteğe bağlı LLM görsel açıklaması veriyi dışarı gönderir; kapalı tutulmalı | BENİMSE (yedek) |
| marker 2.0.0 | Apache-2.0 (ağırlık lisansı UNCONFIRMED); CPU'da çalışan yeniden yazım (2026-07-20) | — | Hız ve kalite iddiası üreticiden | İZLE |
| PaddleOCR-VL-1.6 (v3.7.0) | Apache-2.0; 0.9B; OmniDocBench %96.3 (üretici iddiası) | Taranmış belge için | Türkçe adıyla belirtilmemiş | İZLE |
| MinerU 4.0.10 | Apache-2.0 + ek ticari eşik maddesi | — | Lisans | HAYIR |
| Mistral OCR 3 | Bulut; ~$2 / 1.000 sayfa (UNCONFIRMED) | — | Veri dışarı çıkar | HAYIR (varsayılan) |
| **Obsidian Web Clipper** | Resmi, MIT, 1.7.1 (2026-07-22) | `01-gelen/` şablonu | Kırpılan içerik güvenilmez; okuyucu ajan şart | **BENİMSE** |
| defuddle (kepano) | MIT, 0.19.4; Clipper'ın çekirdeği, CLI olarak da var | `al.py` içinde URL → md | — | BENİMSE |
| trafilatura 2.3.1 / crawl4ai 0.9.4 | Apache-2.0, yerel | Toplu web alma | — | İZLE |
| Jina Reader (r.jina.ai), firecrawl (AGPL) | Bulut / AGPL | — | Veri dışarı çıkar / lisans | HAYIR |
| **Syncthing-Fork** (researchxxl/syncthing-android) | MPL-2.0, v2.1.6.0 (2026-10-06), F-Droid; resmi Android uygulamasının halefi | Telefon not klasörü → `01-gelen/mobil/` | Eşleme çakışması; gelen klasör salt-ekleme olmalı | **BENİMSE** |
| himalaya | Apache-2.0, v2.2.1 (2026-10-02); IMAP, JMAP, Gmail API | `al.py --eposta`: etiketli postalar → md | Yalnız okuma; gönderim imza gerektirir (A6) | BENİMSE-deneme |
| Claude Code **channels** (Telegram/Discord) | Araştırma önizlemesi; Bun gerekir; yalnız oturum açıkken çalışır; eşleştirme + allowlist | İç Ses mobil girişi | Mesajlar üçüncü taraftan geçer; uzaktan talimat kanalı enjeksiyon yüzeyi açar | İZLE |
| ntfy 2.28.0 | Apache-2.0, kendi sunucunda barındırılabilir | Durum ve kapı bildirimi (ASK.md açıldı) | Yalnız bildirim; onay kanalı yapılmamalı | ÖDÜNÇ AL |

## 5. Gözlemlenebilirlik ve maliyet
- **ccusage** [d]: MIT, 18.9k yıldız, v20.0.26 (2026-09-27). Repo `ryoppippi/ccusage`'dan `ccusage/ccusage`'a taşındı. Yerel JSONL okur; `daily`, `weekly`, `session` ve `blocks` (5 saatlik pencere) komutları, `--json` ve `--offline` seçenekleri var. Yer: `/haftalik` ve MALIYET.csv mutabakatı. Etiket: **BENİMSE**.
- **Claude Code OTel** (değişenler): olay listesine `api_refusal`, `skill_activated`, `hook_registered`, `mcp_server_connection` ve `permission_mode_changed` eklendi. İzler (trace) beta (`CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`). İçerik günlüğü varsayılan kapalı. Tek kişilik sistemde bir toplayıcı kurmak ağır; `OTEL_METRICS_EXPORTER=console` → dosya yeterli. Etiket: ÖDÜNÇ AL.
- **`/insights`** (yerel oturumların HTML raporu) ve `/usage` (takma adları `/cost` ve `/stats`) resmi dokümanda doğrulandı. Yer: `/haftalik` adımı. Etiket: BENİMSE (yerleşik).
- Claude Code Analytics API: Admin API anahtarı ister, bireysel hesapta yok. Etiket: HAYIR.
- Langfuse v4.53.0: çekirdek MIT, `ee/` ayrı; ClickHouse yığını ağır; Claude Code entegrasyonu UNCONFIRMED. Arize Phoenix ve SigNoz Elastic tarzı lisanslı, yani OSI değil. OpenLIT 2.1.0 Apache-2.0. Etiket: hepsi İZLE.

## 6. Kalite ve değerlendirme
- **`claude plugin eval`** (değişenler): `claude plugin eval init`; `--ablation none` taban çizgisini kapatır ve maliyeti yarıya indirir; `--judge-model`; sahte (mock) desteği; CI kapısı. Her koşu gerçek bir model çağrısıdır. Yer: `.claude/` skill'leri için `evals/<vaka>/`. Ücretsiz değerlendiriciler (`regex`, `file_exists`, `tool_order`) önce gelmeli. Etiket: kararı geçerli; maliyet kuralı eklenmeli.
- **lychee** (Apache-2.0, v0.24.2): ölü URL denetimi. Uydurma atıfı yakalamaz, yalnız canlılığı denetler. Yer: kontrol.py TAZELIK veya `/haftalik`. Etiket: **BENİMSE**.
- promptfoo v0.124.0: Mart 2026'dan beri OpenAI'ın; MIT olarak kalıyor. Etiket: İZLE (plugin eval yeterli; sahiplik değişti).
- DeepEval 4.2.4, Inspect AI (MIT; UK AISI) ve Braintrust autoevals: tek kişilik wiki için fazla. Inspect'in "görev/çözücü/puanlayıcı" ayrımı ÖDÜNÇ AL.
- Lint: markdownlint-cli2 v0.23.3 (MIT), hook'ta. vale v3.24.0'ın Türkçe desteği UNCONFIRMED; terim tutarlılığı (ASCII alan adları, yasak kelimeler) için kendi kural seti yazılabilir; etiket İZLE. remark-lint-frontmatter-schema bayat (son sürüm 2023); onun yerine `check-jsonschema` ve `00-sistem/sema/*.schema.json` ÖDÜNÇ AL.

## 7. Otomasyon ve zamanlama
- **Claude Code hook olayları** [d] (33 olay). Yeni ve sisteme değenler:
  - `ConfigChange`: `project_settings` ve `skills` eşleyicileri; exit 2 değişikliği bloklar. Etiket: **BENİMSE**.
  - `PermissionDenied`: auto modun reddettiği çağrıları GUNLUK'e yazar.
  - `FileChanged`: yalnız dosya adı eşleyicisi alır; **bağlam enjekte edemez, bloklayamaz** ve yalnız oturum açıkken çalışır. Gelen kutusu izleyicisi olamaz; systemd `.path` birimi kararı geçerli. Etiket: ÖDÜNÇ AL (`.env` gibi tekil dosyalar için).
  - `mcp_tool` hook türü (örneğin qmd yeniden indeksleme); `PostCompact`, `InstructionsLoaded`, `PreModelSwitch`.
- **Routines** (araştırma önizlemesi): yalnız bulutta çalışır, her koşu repoyu baştan klonlar, **izin sorusu yoktur** ve tüm bağlayıcılar varsayılan olarak açıktır. En kısa aralık 1 saat. API tetikleyicisinin `text` alanı güvenilmeyen veri olarak sarılır. Sistemin imza kuralıyla çelişir. Etiket: yalnız "hazırla" adımı için; bağlayıcısız ve salt-okuma bir rutin ÖDÜNÇ AL.
- **Masaüstü zamanlı görevler**: yerel, en kısa aralık 1 dakika, `~/.claude/scheduled-tasks/<ad>/SKILL.md`. Linux masaüstü uygulaması UNCONFIRMED.
- `/loop` ve Cron araçları oturum kapsamında; 7 günde sona erer. `.claude/loop.md` ile özelleştirilebilir. Etiket: ÖDÜNÇ AL (oturum içi gelen kutusu yoklama).
- dagu v2.18.2 (2026-10-04, GPL-3.0); kararı geçerli. lefthook v2.1.17 (MIT): git hook'larını (pre-commit `kontrol.py --kisa`) tek dosyada toplar. Etiket: BENİMSE-deneme (Graphify'ın kendi git hook'larının yerine).
- claude-code-action v1.0.244 (2026-10-06): yalnız GitHub'da barındırılan wiki için. Etiket: —.

## 8. Güvenlik ve sandbox
- **Bash sandbox** [d]: Linux'ta bubblewrap + socat; ikisi de kurulu. Bash, PowerShell ve Monitor komutlarını kapsar. **Dosya araçları, MCP sunucuları ve hook'lar sandbox dışında kalır.** Bağımlılık eksikse varsayılan davranış sandbox'sız çalışmaktır; `sandbox.failIfUnavailable: true` bunun yerine açılışta çıkış yaptırır. `allowUnsandboxedCommands: false` ile `dangerouslyDisableSandbox` kaçışı kapanır. Yeni: `credentials.mask` + `network.tlsTerminate` kullanıldığında komut gerçek anahtar yerine bir yer tutucu görür; proxy gerçek değeri yalnız izinli hostta enjekte eder. Bu, Paraşüt ve Stripe anahtarları için idealdir, ama yalnız kullanıcı ayarlarında ya da `--settings` ile çalışır, proje ayarında çalışmaz. Etiket: **BENİMSE** (öncelik 1).
- **sandbox-runtime (srt)**: Apache-2.0, 5.4k yıldız, beta. `npx @anthropic-ai/sandbox-runtime claude` tüm süreci sarar (MCP ve hook'lar dahil). Varsayılan ağ engeli; `.git/hooks`, `.mcp.json` ve `.claude/agents` yazımı engellenir. Linux'ta engel listesi açılışta bir kez kurulur. Etiket: İZLE (gözetimsiz `calistir.sh` koşuları için aday).
- Docker Sandboxes (`sbx`, mikroVM; Linux desteği kısmen doğrulandı) ve dagger/container-use (Apache-2.0, deneysel): İZLE.
- **Snyk agent-scan** (Apache-2.0, 3.1k yıldız): yerel; Claude yapılandırmasını kendisi keşfeder ve MCP ile skill'leri tarar. Etiket: **BENİMSE** (A10 kapısında kanıt).
- **Meta "Agents Rule of Two"** (2025-10-31): bir oturumda şu üçünden en fazla ikisi olmalı: güvenilmeyen girdi, hassas veri, durum değişikliği veya dış iletişim. Üçü birden varsa insan onayı gerekir. Sistemin `okuyucu` + imza tasarımının resmi adlandırması. Etiket: ÖDÜNÇ AL (`IMZA-MATRISI`'ne her ajan için "hangi ikisi" sütunu).
- CaMeL (Apache-2.0, 401 yıldız): yazarlar bakımın sürmediğini ve güvenli olmayabileceğini söylüyor. Yetenek izleme fikri ÖDÜNÇ AL; kodu HAYIR. LlamaFirewall / PromptGuard 2 ayrıntıları UNCONFIRMED.

## 9. "Eller" (kısa)
- **Google Workspace resmi uzak MCP'leri** (Mayıs 2026: Gmail, Drive, Calendar, Chat, People): topluluk Gmail ve Calendar MCP'lerinin yerine geçer. Taslak yazmak serbest; gönderim A6 imzası ister. Etiket: BENİMSE (ihtiyaç doğunca, A10).
- Tarayıcı: Playwright MCP (Apache-2.0, 37.9k yıldız) kararı geçerli. Chrome DevTools MCP (53k yıldız) hata ayıklama içindir; ekleme gereksiz.
- Türkiye: resmi Paraşüt MCP **bulunamadı**. Topluluk projeleri: bir TS SDK + MCP (lobehub listesi), `turkey-payments-mcp` (iyzico, varsayılan sandbox) ve `reyhansunduk/efatura-mcp-server` (fatura oluşturma ve iptal). Olgunlukları UNCONFIRMED; yazma araçları imza dışında kalmamalı. PayTR, Logo, Mikro ve Uyumsoft için MCP bulunamadı. Etiket: ÖDÜNÇ AL (araç adları ve sandbox varsayılanı); Paraşüt REST'e kendi salt-okuma betiğimiz.
- Ödeme protokolleri: AP2 (açık yönetişime geçti), ACP (OpenAI + Stripe), x402 (x402 Foundation, V2 Aralık 2025), MPP (Stripe + Tempo, 2026-03-18), Visa Intelligent Commerce (MCP sunucusu ve sandbox) ve Mastercard Agent Pay (AU, NZ ve ES'de canlı). Türkiye'de kullanılabilirlik UNCONFIRMED. Tek kişilik sistemde Stripe dışında gereksiz. Etiket: İZLE. Kaynakların bir kısmı ikincil.

## 10. Görselleştirme
- **Graphify `graph.html`** (bölüm 1): wiki grafı için sıfır ek bağımlılık; `graf.py` yan ürünü. Etiket: BENİMSE (2 numaralı önerinin parçası).
- Obsidian Bases (çekirdek eklenti, 1.9.0'dan beri): tablo, kart ve liste görünümleri; Obsidian CLI üzerinden `base:query`. Çekirdek pano veya kanban görünümü UNCONFIRMED. Topluluk eklentileri (`kanban-bases-view`, `bases-timeline`) var, olgunlukları UNCONFIRMED. Etiket: İZLE (`.base` dosyaları kepano/obsidian-skills ile zaten geçerli).
- Backlog.md (MIT, 6.9k yıldız; `backlog board` ve `backlog browser` web arayüzü): kararı geçerli. Güncel sürüm UNCONFIRMED.
- Quartz v5 (MIT, 13.3k yıldız): statik site; kamuya açık yayın imza ister. v5'te graf görünümü UNCONFIRMED. Etiket: İZLE.
- Mermaid `timeline` ve `gantt`: KARARLAR ve GUNLUK için üretilen düz markdown; Obsidian'da yerel olarak işlenir. Etiket: ÖDÜNÇ AL (sürüm ayrıntısı doğrulanmadı).

## Kendi bulgularım (listede yoktu)
1. **Sandbox kimlik bilgisi maskeleme** (`credentials.mask` + `injectHosts`): dış API anahtarı ajanın göreceği bir değer olmaktan çıkar; "dış API yazımı imza ister" kuralına teknik bir katman ekler.
2. **FreyaTTS** (Temmuz 2026): Türkçe-öncelikli, CPU'da gerçek zamanlı ve Apache-2.0 lisanslı tek TTS.
3. **Graphify'ın deterministik markdown modu + sahibin mevcut `yenile.py` deseni**: grafı LLM'siz, allowlist'li ve hash manifestli kurmak sistemin "kanıt = komut + çıkış kodu" kuralına doğrudan uyuyor.

## Kaynaklar (erişim: 2026-10-06)
- https://github.com/Graphify-Labs/graphify · https://pypi.org/project/graphifyy/ · https://github.com/Graphify-Labs/graphify/releases · https://docs.graphify.com · yerel: `graphify` 0.9.77 `extractors/markdown.py`, `install.py`, `always_on/claude-md.md`
- https://www.augmentcode.com/learn/graphify-knowledge-graph-codebase-skill (ikincil; YC S26 / 74.8k iddiası)
- https://github.com/abhigyanpatwari/GitNexus
- https://github.com/basicmachines-co/basic-memory · https://github.com/zilliztech/memsearch · https://github.com/topoteretes/cognee · https://github.com/getzep/graphiti · https://github.com/getzep/zep · https://github.com/letta-ai/letta · https://github.com/letta-ai/letta-code · https://github.com/mem0ai/mem0 · https://github.com/HKUDS/LightRAG · https://github.com/microsoft/graphrag · https://github.com/thedotmack/claude-mem
- https://obsidian.md/help/cli · https://obsidian.md/changelog/2026-02-27-desktop-v1.12.4/ · https://obsidian.md/changelog/2025-05-21-desktop-v1.9.0/ · https://github.com/MarkusPfundstein/mcp-obsidian · https://github.com/cyanheads/obsidian-mcp-server · https://github.com/coddingtonbear/obsidian-local-rest-api · https://github.com/brianpetro/obsidian-smart-connections
- https://github.com/tobi/qmd · https://github.com/tobi/qmd/releases · https://github.com/asg017/sqlite-vec · https://huggingface.co/Qwen/Qwen3-Embedding-0.6B · https://huggingface.co/BAAI/bge-m3 · https://huggingface.co/intfloat/multilingual-e5-large · https://huggingface.co/google/embeddinggemma-300m · https://research.itu.edu.tr/en/publications/tr-mteb-a-comprehensive-benchmark-and-embedding-model-suite-for-t/ · https://huggingface.co/trmteb
- https://github.com/cxrobx/vault-mcp · https://github.com/wirux/mcp-markdown-vault · https://github.com/mikebronner/markdown-vault-mcp (UNCONFIRMED)
- https://code.claude.com/docs/en/voice-dictation · https://support.claude.com/en/articles/11101966 · https://docs.livekit.io/agents/logic/turns/turn-detector/ · https://github.com/livekit/agents · https://github.com/pipecat-ai/pipecat · https://github.com/resemble-ai/chatterbox · https://github.com/freyavoiceai/FreyaTTS · https://github.com/OHF-Voice/piper1-gpl · https://huggingface.co/rhasspy/piper-voices · https://github.com/idiap/coqui-ai-TTS · https://huggingface.co/hexgrad/Kokoro-82M · https://github.com/SWivid/F5-TTS · https://github.com/nari-labs/dia · https://github.com/microsoft/VibeVoice · https://github.com/fishaudio/fish-speech · https://github.com/canopyai/Orpheus-TTS
- https://elevenlabs.io/docs/overview/models · https://elevenlabs.io/pricing/api · https://docs.cartesia.ai/build-with-cartesia/tts-models/latest · https://ai.google.dev/gemini-api/docs/speech-generation · https://developers.openai.com/api/docs/models/gpt-realtime
- https://github.com/kyutai-labs/delayed-streams-modeling · https://huggingface.co/nvidia/canary-1b-v2 · https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3 · https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602 · https://huggingface.co/CohereLabs/cohere-transcribe-03-2026 · https://github.com/moonshine-ai/moonshine · https://www.assemblyai.com/docs/streaming/universal-streaming/multilingual-transcription · https://docs.speechmatics.com/speech-to-text/languages · https://soniox.com/pricing · https://github.com/peteonrails/voxtype · https://github.com/goodroot/hyprwhspr
- https://github.com/docling-project/docling · https://github.com/docling-project/docling-serve · https://github.com/docling-project/docling-mcp · https://github.com/microsoft/markitdown · https://github.com/datalab-to/marker · https://github.com/opendatalab/MinerU · https://github.com/PaddlePaddle/PaddleOCR · https://github.com/allenai/olmocr · https://github.com/deepseek-ai/DeepSeek-OCR · https://github.com/studio-dots-ai/dots.ocr · https://mistral.ai/pricing
- https://github.com/obsidianmd/obsidian-clipper · https://github.com/kepano/defuddle · https://github.com/adbar/trafilatura · https://github.com/unclecode/crawl4ai · https://github.com/jina-ai/reader · https://github.com/firecrawl/firecrawl · https://github.com/pimalaya/himalaya · https://github.com/researchxxl/syncthing-android · https://github.com/binwiederhier/ntfy · https://code.claude.com/docs/en/channels · https://github.com/GongRzhe/Gmail-MCP-Server
- https://github.com/ccusage/ccusage · https://github.com/ryoppippi/ccusage · https://code.claude.com/docs/en/monitoring-usage · https://code.claude.com/docs/en/commands · https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api · https://github.com/langfuse/langfuse · https://github.com/Arize-ai/phoenix · https://github.com/openlit/openlit · https://github.com/SigNoz/signoz
- https://code.claude.com/docs/en/plugin-evals · https://github.com/promptfoo/promptfoo · https://github.com/confident-ai/deepeval · https://github.com/UKGovernmentBEIS/inspect_ai · https://github.com/lycheeverse/lychee · https://github.com/DavidAnson/markdownlint-cli2 · https://github.com/vale-cli/vale · https://github.com/JulianCataldo/remark-lint-frontmatter-schema
- https://code.claude.com/docs/en/hooks · https://code.claude.com/docs/en/routines · https://code.claude.com/docs/en/desktop-scheduled-tasks · https://code.claude.com/docs/en/scheduled-tasks · https://github.com/anthropics/claude-code-action · https://github.com/dagu-org/dagu · https://github.com/evilmartians/lefthook · https://github.com/pre-commit/pre-commit
- https://code.claude.com/docs/en/sandboxing · https://code.claude.com/docs/en/sandbox-environments · https://code.claude.com/docs/en/devcontainer · https://code.claude.com/docs/en/permission-modes · https://github.com/anthropic-experimental/sandbox-runtime · https://docs.docker.com/ai/sandboxes/ · https://github.com/dagger/container-use · https://github.com/snyk/agent-scan · https://github.com/google-research/camel-prompt-injection · https://arxiv.org/abs/2503.18813 · https://simonw.substack.com/p/new-prompt-injection-papers-agents · https://github.com/meta-llama/PurpleLlama
- https://developers.google.com/workspace/guides/configure-mcp-servers · https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html · https://github.com/microsoft/playwright-mcp · https://github.com/ChromeDevTools/chrome-devtools-mcp · https://lobehub.com/mcp?q=parasut · https://mcp.so/servers/turkey-payments-mcp · https://github.com/reyhansunduk/efatura-mcp-server · https://github.com/google-agentic-commerce/AP2 · https://github.com/agentic-commerce-protocol/agentic-commerce-protocol · https://github.com/coinbase/x402 · https://fortune.com/2026/03/18/stripe-tempo-paradigm-mpp-ai-payments-protocol (ikincil) · https://corporate.review.visa.com/en/sites/visa-perspectives/innovation/visa-mcp-server-agent-acceptance-toolkit.html
- https://github.com/MrLesk/Backlog.md · https://jsoncanvas.org · https://github.com/jackyzha0/quartz · https://community.obsidian.md/plugins/bases-timeline

## Bağlar
### Dayandığı
- [[00-sistem/arastirma/09-github-taramasi]] — önceki tarama; buradaki BENİMSE/ÖDÜNÇ AL kararları tekrar edilmez, yalnız değişenler yazılır
- [[00-sistem/arastirma/02-hafiza-ve-wiki-duzenleri]] — hafıza ve wiki düzeni kararları (bilgi grafı, arama bölümleri)
- [[00-sistem/arastirma/04-guvenilirlik-ve-kalite-teknikleri]] — sandbox, hook, değerlendirme ve maliyet kararları
- [[00-sistem/arastirma/05-eller-ve-alan-paketi-3d]] — eller ve MCP kararları (Türkiye'ye özgü araçlar)
- [[00-sistem/arastirma/08-ic-ses-yontemleri]] — ses hattı kararları (whisper, Smart Turn, Handy)
### Beslediği
- [[30-devlet/kapilar/KP-001-sandbox-acilisi]] — öncelik 1 (sandbox) bu raporla kapıya geldi
- [[10-insan/araclar/ARAC-KAYDI]] — benimsenecek araçların kayda girmeden önceki dayanağı
### Gelen

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 1.0 | 2026-10-06 | T-007 | Araştırma alt ajanının raporu sisteme alındı; ad, yol ve gövde yapısı (Amaç/İçerik/Bağlar) düzeltildi |
| 1.1 | 2026-10-06 | T-008 | besledigi += KP-001 (öncelik 1 uygulamaya alındı) |
