---
id: 20261006-1903-arastirma-04
ad: guvenilirlik-ve-kalite-teknikleri
tur: kaynak
kat: 0
surum: 1.1
durum: aktif
amac: Bir LLM/ajan sistemini daha iyi ve daha guvenilir yapan teknikleri (baglam muhendisligi, uzun sureli ajan guvenilirligi, degerlendirme, MCP, model yonlendirme ve maliyet, yapili cikti, korkuluklar, bilgi temellendirme, gozlemlenebilirlik, ses) ve her birinin Yeni Sistem'de tam olarak hangi dosyaya/hook'a/skill'e girdigini belirlemek.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: [00-sistem/arastirma/01-claude-code-mekanikleri.md]
besledigi: [30-devlet/normlar/MODEL-POLITIKASI.md, 30-devlet/normlar/HAKEM-KURALLARI.md, 10-insan/araclar/ARAC-KAYDI.md, 00-sistem/arastirma/10-yenilikci-teknolojiler.md]
kaynaklar: ["https://research.trychroma.com/context-rot", "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents", "https://code.claude.com/docs/en/hooks", "https://code.claude.com/docs/en/goal", "https://platform.claude.com/docs/en/about-claude/pricing", "https://www.anthropic.com/engineering/claude-code-sandboxing", "https://arxiv.org/abs/2506.08837"]
alindi: 2026-10-06
guven: orta
kaynak_turu: literatur-ve-belge-taramasi
saklama: K
---

# Guvenilirlik ve kalite teknikleri (2024-2026)

## 1. Baglam muhendisligi
- **Context rot**: dogruluk girdi buyudukce duser (18 model testi, Chroma); Anthropic "dikkat butcesi". Baglam kit kaynaktir. https://research.trychroma.com/context-rot
- **Tam zamaninda getirme**: yol/link baglamda, govde gerektiginde. HARITA yalniz yol + tek satir. Buyuk belgeleri CLAUDE.md'ye `@import` etme.
- **Sikistirma**: otomatik sikistirma modele gore (~967K / 200K); sag cikanlar: sistem istemi, kok CLAUDE.md, kapsamsiz rules, otomatik hafiza, plan; yol kapsamli rules ve hook metni ozetlenir; skill govdeleri 5.000 token/skill sinirli yeniden enjekte. `## Compact instructions` bolumu korunacaklari belirtir; `SessionStart` `matcher: compact` ile ILERLEME yeniden okunur; `PreCompact` hook exit 2 ile sikistirmayi engelleyip once ilerleme yazdirir. https://code.claude.com/docs/en/context-window
- **Istem sirasi**: uzun belgeler ustte, istek sonda (%30'a kadar iyilesme); "once ilgili satirlari alintila, sonra uygula". https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- **Boyut**: CLAUDE.md < 200 satir; SKILL.md < 500; `/doctor prompt-audit`. Butunluk betigi bu sinirlari da denetler.
- **Ozellik maliyeti**: CLAUDE.md her istekte; rules oturum/yol eslesmesinde; skill aciklamasi her istekte govde kullanimda; MCP yalniz ad; alt ajan yalitik; hook metin dondurmedikce sifir. Yan etkili skill'ler `disable-model-invocation: true`.

## 2. Uzun sureli ajan guvenilirligi
- **Harness deseni**: baslatici (init.sh, ilerleme, ozellik listesi `passes`) + oturum basina tek ozellik + ucten uca dogrulama + commit + ilerleme guncelle; "testleri silmek kabul edilemez". https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **Kesintiyi varsay**: her adim yeniden calistirilabilir (kontrol-et-sonra-yap); eylemden once durum kaydet; checkpoint != git; Bash degisiklikleri checkpoint'te yok; devam ederken kesilen arac cagrisi "etkili oldu mu once kontrol et" uyarisiyla gelir. https://code.claude.com/docs/en/checkpointing
- **Deterministik kapilar (hook)**: Stop hook `last_assistant_message` ve `tool_uses[]` alir; `decision: block` + `additionalContext`; 8 ardisik engel tavani; `stop_hook_active`. TaskCompleted kanitsiz kapatmayi engeller (Task araclari yeni modellerde varsayilan kapali: `CLAUDE_CODE_ENABLE_TODO_TOOLS=1`). https://code.claude.com/docs/en/hooks
- **/goal**: transkriptten yargilayan kucuk model; "veya N turdan sonra dur" ile sinirla; duraklama tespiti. https://code.claude.com/docs/en/goal
- **Tekrar butcesi**: `claude -p --bare --max-turns N --max-budget-usd X --fallback-model sonnet --output-format json`; `StopFailure` hook hata sinifini GUNLUK'e yazar. https://code.claude.com/docs/en/headless
- **Dogrulama once, cekismeli inceleme**: "calistirabilecegi bir kontrol ver"; kanit goster; inceleyici alt ajan yalniz diff + olcutleri gorur; bosluk avcisi inceleyiciyi dogruluga sinirla. https://code.claude.com/docs/en/best-practices

## 3. Degerlendirme
- Gorev/deneme/hakem; pass@k vs pass^k (%75 -> ~%42 pass^3); kod tabanli hizli, model tabanli kalibrasyon ister ("Bilinmiyor" izinli), insan altin; urunu ve transkripti puanla; gercek hatalardan 20-50 gorev. https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- `claude plugin eval`: `evals/<case>/prompt.md`, `graders/*.md` (`regex`, `tool_used`, `tool_order`, `file_exists`, `llm`, `baseline`), her vaka 3x eklentiyle 3x eklentisiz, `--threshold`, `report.html`. https://code.claude.com/docs/en/plugin-evals
- LLM-hakem onyargilari (CALM 12 onyargi): kisa ciktilarda somut PASS/FAIL; uzun artefaktlari regex/dosya ile puanla; farkli model ailesi/temiz baglam; sirayi karistir; "iyilestirildi" deme. https://arxiv.org/abs/2410.02736
- Dis geri bildirimsiz oz-duzeltme guvenilir degil -> her dogrulama dis bir sey calistirir (test, derleme, diff, sema). https://arxiv.org/abs/2310.01798

## 4. Arac / MCP ekosistemi
- MCP 2026-07-28: durumsuz (oturum kimligi yok), `subscriptions/listen`, MRTR (sunucu baslatmali sampling/elicitation yerine), Roots/Sampling/Logging kullanimdan kaldirildi, OTel `traceparent`, deterministik `tools/list`. Kendi sunucun durumsuz, dizinler parametre. https://modelcontextprotocol.io/specification/2026-07-28/changelog
- Kayitlar: resmi registry (onizleme 2025-09), Docker MCP Catalog, Anthropic Directory (guvenlik denetimi yapmaz), referans sunucular (Filesystem, Git, Memory, Fetch...). Topluluk kataloglari dogrulanamaz.
- Onemli sunucular: GitHub resmi (uzak), Playwright MCP (erisilebilirlik agaci), Stripe (uzak, OAuth), Blender MCP. Resmi tavsiye: CLI araclari (`gh`, `aws`) MCP'den daha baglam-verimli. MCP cikti tavani 25K token. https://code.claude.com/docs/en/costs
- Arac tasarimi: az ve birlesik; ad alani; anlamli kimlik; sayfalama; "yeni ekip uyesine anlatir gibi". Butunluk betigi <=40 satir yapili karar dondurur, ham dokum degil.
- Skill standardi (agentskills.io; Claude Code, Cursor, Gemini CLI, Codex, Copilot...); Anthropic skills reposu; resmi eklenti pazari. https://agentskills.io
- AGENTS.md: CLAUDE.md yoksa okunur; `claude-md-and-agents-md` ile ikisi.

## 5. Model yonlendirme ve maliyet
- Fiyatlar ($/M token giris/cikis; resmi sayfa): Fable 5.1 10/50; Opus 5.5 4/20; Sonnet 5.5 2/10; Haiku 4.5 1/5; Batch %50 indirim; onbellek okuma Opus/Sonnet 0.20, Haiku 0.10. https://platform.claude.com/docs/en/about-claude/pricing
- Kurallar: Sonnet cogu kodlama ve isci; Opus mimari ve cok adimli akil; Haiku basit alt ajan, hakem, ozet; `opusplan`; `CLAUDE_CODE_SUBAGENT_MODEL`; caba seviyeleri low..max. https://code.claude.com/docs/en/model-config
- Onbellek: tools -> system -> messages sirasi; min 512 token; arac tanimi/thinking/effort degisirse gecersiz; abonelikte 1 saat TTL; `/usage` isabet oranini gosterir. Dinamik durum CLAUDE.md'ye DEGIL, SessionStart ciktisina. https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Izleme: `/usage`, `--output-format json` -> `total_cost_usd`, OpenTelemetry `claude_code.cost.usage`; SessionEnd hook token toplamlarini MALIYET.csv'ye yazar.

## 6. Yapili cikti ve dogrulama
- `output_config.format = json_schema` (kisitli kod cozme; recursion/min-max yok); Claude Code `claude -p --json-schema`; kapi raporlari sema ile (`{kapi, durum, kanit[], soru?}`); frontmatter JSON Schema ile dogrulanir. https://platform.claude.com/docs/en/build-with-claude/structured-outputs
- Uret-sonra-dogrula: Stop `type: agent` hook testleri calistirir; `/verify`, `/code-review` (temiz baglam), inceleyici yalniz diff + kart gorur.
- Oy verme: yuksek riskli kapi yargilari 3x Haiku, oybirligi; anlasmazlik -> ASK.md.
- TDD: once basarisiz test; kok neden; testleri silme.

## 7. Korkuluklar ve guvenlik
- Izinler: `allow/ask/deny`; `deny` siniflandiricidan once ve ezilemez; `ask` auto modda bile insan sorusu; Bash eslesmesi metinsel -> tam komut icin PreToolUse hook. https://code.claude.com/docs/en/permissions
- Auto-mode siniflandirici: `autoMode.environment`, `hard_deny` > `soft_deny` > `allow`; ajanlar arasi mesaj guvenilmez (onay aktaramaz). https://code.claude.com/docs/en/auto-mode-config
- Sandbox: bubblewrap+socat (Linux); yazma = cwd + temp; ag yalniz proxy allowlist; hook/MCP/Read/Edit/WebFetch sandbox disinda; `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB`. https://www.anthropic.com/engineering/claude-code-sandboxing
- Istem enjeksiyonu: WebFetch yalitik kucuk model; `--bare` CI'da; "olumcul uclu" (ozel veri + guvenilmeyen icerik + sizdirma kanali -> birini kaldir); alti tasarim deseni (Dual LLM, Plan-Then-Execute, Context-Minimization...). Gelen kutusu/web = Dual-LLM: karantinali `okuyucu` alt ajani (Read/WebFetch, Write/Bash yok, `omitClaudeMd`) yapili not uretir; yalniz ana ajan eylem yapar. https://arxiv.org/abs/2506.08837
- Sirlar ve yikici eylem: `permissions.deny: ["Read(./.env*)", "Read(**/*.pem)"]`; `FileChanged` hook .env; `ConfigChange` hook ayar degisikligini kaydeder; PreToolUse `if: "Bash(rm *)"` exit 2.
- Insan dongude: `permissions.ask`; `AskUserQuestion`; kanallar (Telegram) izin sorusu aktarabilir. Beyan edilen kapi = `ASK.md` (tek soru) + tur biter; Stop hook ASK.md veya Kanit blogu yoksa gecirmez.

## 8. Bilgi temellendirme
- <~200K token korpus -> tamamini onbellekle istemde; ustu -> Contextual Retrieval (parca baglami + BM25 + yeniden siralama, hata %5.7 -> %1.9). Birkac yuz sayfalik wiki icin indeks + grep (ajanik arama) once; BM25 yalniz iskalar sikca kaydedilince. https://www.anthropic.com/news/contextual-retrieval
- Alinti disiplini: webden gelen her olgu `kaynak`, `alindi`, `page_age` tasir; butunluk betigi 90 gunden eski `alindi`yi "TAZELIK" altinda listeler.

## 9. Gozlemlenebilirlik
- Claude Code OpenTelemetry: `CLAUDE_CODE_ENABLE_TELEMETRY=1`, metrikler (`session.count`, `cost.usage`, `token.usage`, `commit.count`...), olaylar (`tool_result`, `tool_decision`, `skill_activated`). https://code.claude.com/docs/en/monitoring-usage
- Ajanin geri okuyabildigi gunluk: transkript JSONL'i ayristirma; hook'lar repo ici salt-ekleme GUNLUK.md yazar; SessionStart son 30 satiri okur.
- Panolar: `/usage`, `/insights`, Langfuse (OTel), Braintrust (UNCONFIRMED).

## 10. Ses / dikte
- Claude Code `/voice`: tut/tikla; Turkce destekli; prompt'a yazar; 2 dk tavan. Kisa notlar icin.
- Yerel: Whisper large-v3 (99 dil, Turkce), whisper.cpp / faster-whisper; Parakeet v3 25 dil (Turkce UNCONFIRMED).
- Bulut (Artificial Analysis 2026): Scribe v2 %2.2, Voxtral Small %2.8, AssemblyAI U-3 %3.1, Deepgram Nova-3 %5.2; fiyat 1.000 dk: $0.74-16.
- Tasarim: kisayol -> kayit -> yerel STT -> `01-gelen/YYYY-MM-DD-HHMM.md` (frontmatter: tur dikte, kaynak ses, dil tr, model, islendi false) -> triage skill -> not/gorev. Telefon: Telegram kanali.

## Yeni Sistem'e nasil girer (eslesme tablosu)
| Teknik | Yeri |
|---|---|
| Ilerleme dosyasi / kesintiyi varsay | `00-sistem/ILERLEME.md`; `SessionStart` (startup/resume/compact) hook yazdirir + `git log -5` + `tail -30 GUNLUK.md`; `kapat` skill ve `PreCompact` hook yazar |
| `passes` bayrakli gorev listesi | `20-sirket/gorevler/*.md` frontmatter `durum`, `kanit[]`; kontrol.py kanitsiz `tamam` reddeder |
| Sessiz durmama | Stop hook `durus-kapisi.sh`: `## Kanit` blogu VEYA `ASK.md` yoksa `decision: block`; `stop_hook_active` honor |
| TaskCompleted kaniti | `gorev-kaniti.sh` (Task araclari acilirsa) |
| /goal | `kapi-kosusu` skill (`disable-model-invocation: true`) olcutleri /goal'e cevirir |
| Gozetimsiz kosu | `00-sistem/scripts/calistir.sh`: `-p --bare --max-turns --max-budget-usd --fallback-model --json-schema`; `StopFailure`/`PostToolUseFailure` hook GUNLUK'e |
| Gelen kutusu | `01-gelen/`; `Monitor`/`/loop 10m`; `inbox-triage` skill `context: fork`, `agent: okuyucu` |
| Sikistirma | CLAUDE.md `## Compact instructions`; kapsamsiz rules; SessionStart compact matcher |
| CLAUDE.md boyutu | <=200 satir: kimlik, 4 kat haritasi, 10 sert kural, HARITA isaretcisi; `.claude/rules/*.md` yol kapsamli; prosedurler skill'e |
| Istem sirasi | gorev karti: baglam -> kisitlar -> istek SONDA |
| Tam zamaninda getirme | HARITA.md yol + tek satir; "once HARITA, sonra gerekeni ac" |
| Evals | `.claude/` eklenti olarak; `evals/<case>/`; pass^3 |
| Hakem kurallari | `30-devlet/normlar/HAKEM-KURALLARI.md` |
| Yapili kapi raporu | `00-sistem/sema/kapi-raporu.schema.json`, `sayfa.schema.json` |
| Cekismeli inceleme | `.claude/agents/denetci.md` (Read/Grep/Glob/Bash, sonnet, maxTurns 15) |
| Dis dogrulama | Kural: "Kanit = calistirilmis komut + cikis kodu + cikti" |
| Izinler | deny: .env, pem, force push, ANAYASA edit; ask: git push, 30-devlet/** edit |
| Sandbox | settings `sandbox.enabled`, `allowedDomains` |
| Yikici koruma | `yikici-koruma.sh` PreToolUse (rm -rf, reset --hard, DROP) |
| Dual-LLM | `.claude/agents/okuyucu.md` (haiku, Read/WebFetch/Grep, Write/Edit/Bash yasak, omitClaudeMd) |
| Model politikasi | `30-devlet/normlar/MODEL-POLITIKASI.md` |
| Onbellek | dinamik durum SessionStart ciktisinda |
| Maliyet | SessionEnd -> `00-sistem/MALIYET.csv` |
| Tazelik | frontmatter `alindi`, kontrol.py TAZELIK listesi |
| Ses | `/voice tap` kisa; yerel STT -> 01-gelen uzun; Telegram telefon |

Ilk uygulanacak 5: (1) oturum-basi.sh + ILERLEME.md, (2) durus-kapisi.sh, (3) yikici-koruma.sh + devlet `ask`, (4) kontrol.py JSON-sema cikisli, (5) calistir.sh.
