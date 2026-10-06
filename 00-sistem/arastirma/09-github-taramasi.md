---
id: 20261006-1908-arastirma-09
ad: github-taramasi
tur: kaynak
kat: 0
surum: 1.0
durum: aktif
amac: Ekim 2026 itibariyla Markdown-wiki tabanli bir Claude Code isletim sistemiyle ilgili acik kaynak projeleri (ekosistem, hafiza, karar/yonetisim, orkestrasyon, SOP-dosya, ses, 3D) taramak; benimse/odunc al/oku kararlarini vermek.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: []
besledigi: [10-insan/araclar/ARAC-KAYDI.md]
kaynaklar: ["https://github.com/anthropics/skills", "https://github.com/OthmanAdi/planning-with-files", "https://github.com/Astro-Han/karpathy-llm-wiki", "https://github.com/MrLesk/Backlog.md", "https://github.com/kenryu42/cc-safety-net", "https://github.com/zilliztech/memsearch", "https://github.com/dagucloud/dagu"]
alindi: 2026-10-06
guven: orta
kaynak_turu: github-taramasi
saklama: K
---

# GitHub taramasi (2026-10-06)

Yontem: github.com repo ve topic sayfalari dogrudan cekildi; yildiz ve "Updated" sayfa anindaki degerler. UNCONFIRMED = yalniz topic tablosunda goruldu.

## 1. Claude Code ekosistemi
- hesreallyhim/awesome-claude-code (53k) — kanonik liste; oku. shanraisshan/claude-code-best-practice (67k, MIT) — Research->Plan->Execute->Review->Ship; faz modelini odunc al. ai-boost/awesome-harness-engineering (4.7k, CC0) — harness ilkelleri (dongu, planlama, sikistirma, izin, hafiza, HITL, dogrulama); en iyi okuma listesi.
- **anthropics/skills** (177k, Apache-2.0) + **agentskills/agentskills** (25k) — SKILL.md standardi; BENIMSE: her rol karti/SOP/kapi gecerli skill klasoru olsun. anthropics/claude-plugins-official (37k) — plugin.json/marketplace.json sozlesmeleri. anthropics/claude-agent-sdk-python (8.1k, MIT) — basliksiz kosular icin.
- **OthmanAdi/planning-with-files** (27k, MIT) — `task_plan.md / findings.md / progress.md`, `.planning/<tarih>-<slug>/`, UserPromptSubmit/SessionStart/PreCompact hook'lari, tamamlama kapisi; dusunce->yurutme omurgasina en yakin; ODUNC AL. https://github.com/OthmanAdi/planning-with-files
- centminmod/my-claude-code-setup (2.6k) — parcali CLAUDE.md; parcadei/Continuous-Claude-v3 (3.9k, Oca 2026, agir) — defter/handoff sekilleri; mksglu/context-mode (20k).
- Alt ajan paketleri: wshobson/agents (40k, MIT; tek Markdown kaynak -> 7 harness), VoltAgent/awesome-claude-code-subagents (25k; Meta/Orkestrasyon ajanlari), revfactory/harness (9k; 6 topoloji: Pipeline, Fan-out, Expert Pool, Producer-Reviewer, Supervisor, Hierarchical).
- Hook'lar: **disler/claude-code-hooks-mastery** (3.9k) — 13 hook olayi uv tek dosya betikleri; kapi hook'lari icin SABLON. **kenryu42/cc-safety-net** (1.6k, MIT) — yikici git/fs komutlarini gercek komut ayristirarak engeller; BENIMSE.
- Is akisi cerceveleri: obra/superpowers (293k) — beyin firtinasi->plan->yurutme skill zinciri; affaan-m/ECC (273k) — "instincts" guven puanli hafiza (oku); **github/spec-kit** (139k) — `constitution` (her seyden once okunan dosya) + spec->plan->tasks; **Fission-AI/OpenSpec** (67k) — `openspec/changes/<ozellik>/` oneri klasoru + tamamlaninca `archive/` (ODUNC AL); BMAD-METHOD (54k) rol personalari; SuperClaude (24k) davranis modlari; ruvnet/ruflo (74k) daemon agir, yalniz oku; gemini-cli-extensions/conductor (3.7k) `tracks/<track>/{spec.md,plan.md}`; Yeachan-Heo/oh-my-claudecode (40k) verify->fix dongusu; automazeio/ccpm (8.3k, Mar 2026) "deterministik isler betikte"; a5c-ai/babysitter (1.6k) zorunlu `ctx.breakpoint()` insan kapilari + olay kaynakli gunluk.
- Markdown -> gorev panosu: **MrLesk/Backlog.md** (6.9k, MIT) — gorevler duz `.md`, terminal Kanban, 3 inceleme kontrol noktasi, MCP, DoD config; gorev karti kati icin BENIMSE/kopyala. gastownhall/beads (28k; Dolt, graf) yalniz bagimlilik fikri; claude-task-master (JSON, Commons Clause) hayir; EvolveHQ/docflow (13 yildiz) ADR + plan/todo,done kuyruklari.

## 2. Hafiza ve bilgi
- letta-ai/letta (25k; kod letta-code'a tasindi) oku. mem0ai/mem0 (67k) DB-oncelikli, yan kart. getzep/graphiti (29k; Neo4j) "gecerlilik penceresi, silme degil" odunc. topoteretes/cognee (31k). thedotmack/claude-mem (97k, Apache) oturum geri cagirma eklentisi (opsiyonel). **zilliztech/memsearch** (2.7k, MIT) — ".md dosyalari gercek, Milvus yeniden kurulabilir golge indeks", dosya izleyici; mimari olarak birebir ihtiyac; BENIMSE/kopyala. volcengine/OpenViking (39k, AGPL) L0/L1/L2 katmanlari (oku). NousResearch/hermes-agent (250k) "karmasik gorevden sonra skill olustur" dongusu (oku).
- LLM-wiki: **Astro-Han/karpathy-llm-wiki** (1.9k, MIT) — raw/, wiki/, index.md, log.md, ingest/query/lint; ODUNC AL. inkeep/open-knowledge (4k, GPL). kiwifs/kiwifs (624, BSL-1.1) Markdown FS + git denetim + FTS + DQL (tasarim referansi). agenticnotetaking/arscontexta (3.5k, MIT) self/notes/ops ayrimi. lsaint/aikito (134) kapsam modeli. **AgriciDaniel/claude-obsidian** (15k, MIT) — isciler taslak dondurur, tek orkestrator atomik uygular, SHA-256 onay kapilari; ODUNC AL.
- Obsidian kopruleri: **kepano/obsidian-skills** (49k, MIT) BENIMSE (gecerli Obsidian Markdown/Bases/Canvas). **YishenTu/claudian** (15.5k, MIT) Obsidian icinde Claude Code (insan arayuzu). coddingtonbear/obsidian-local-rest-api (2.8k, MCP dahili). aka-kika/kika-obsidian-mcp (.base dogrulama).
- Lint: DavidAnson/markdownlint (6.3k) hook'ta; karpathy-llm-wiki lint skill.

## 3. Karar / yonetisim
- ADR: npryce/adr-tools (5.7k, durgun), **adr/madr** (2.4k) BENIMSE govde, **joshrotenberg/adrs** (110, Rust, MCP sunucu dahil, doctor lint) BENIMSE, **me2resh/agent-decision-record** (42) AgDR frontmatter (`id, timestamp, agent, model, trigger, status`) ODUNC AL, mbeacom/adrkit `affects:` alani, rvdbreemen/adr-kit "duzenlemeden once yonetici ADR'leri enjekte et", archgate/cli ADR + yurutulebilir kural cifti, tikalk/adlc-team-skills Maker/Checker ayrimi, clay-good/OpenLore (ADR graf dugumu).
- Insan dongude: humanlayer/humanlayer (11k) — kod "deprecated", HAYIR. **infinri/Writ** (206, MIT) — Plan kapisi (plan.md onaylanana kadar kaynak yazimi engelli), Test kapisi, tek kullanimlik insan sirri "YZ kendini onaylayamaz"; dosya uzerinde yeniden uygula. **ucsandman/DashClaw** (309, MIT) onay gelen kutusu (CLI/PWA/Telegram), fail-closed PreToolUse; opsiyonel uzak onay kanali.
- Politika-olarak-kod: **sipyourdrink-ltd/bernstein** (1.4k, Apache) YAML manifest (fazlar, roller, bagimliliklar, onay kapilari, artefakt sozlesmeleri) + deterministik zamanlayici + imzali kosu makbuzlari; ODUNC AL. omnigent-ai/omnigent (10k) 3 seviyeli YAML politika. **s0912758806p/agentic-sop-to-work** (209, MIT) SOP -> tek-arac skill'ler + adim basina kapi (sema/iz/yeniden hesap), sinirli dongu, tek-yazar kurali; ODUNC AL.
- Denetim gunlugu: bernstein makbuzlari, babysitter gunlugu, DashClaw kaniti; Yeni Sistem icin salt-ekleme GUNLUK.md + git yeterli.

## 4. Orkestrasyon cerceveleri (2026)
| Cerceve | Yildiz | Durum |
|---|---|---|
| anthropics/claude-agent-sdk-python | 8.1k | aktif, dogal — BENIMSE |
| openai/openai-agents-python | 28.6k | aktif; Claude LiteLLM uzerinden |
| google/adk-python | 21k | aktif; Gemini-oncelikli |
| langchain-ai/langgraph | 38k | aktif; Claude birinci sinif |
| crewAIInc/crewAI | 59k | aktif; rol/gorev YAML sekli odunc |
| microsoft/autogen | 60k | bakim modu — HAYIR |
| microsoft/agent-framework | 12.6k | GA; Azure-merkezli |
| ag2ai/ag2 | 4.9k | gonullu fork — HAYIR |
| FoundationAgents/MetaGPT | 71k | 2025'ten beri durgun; "Code = SOP(Team)" tezini oku |
| pydantic/pydantic-ai | 19.6k | aktif; Anthropic birinci sinif — alternatif |
| sipyourdrink-ltd/bernstein / omnigent | 1.4k / 10k | CC-dogal orkestrasyon — aday |
Egilim: buyume CC-dogal orkestrasyonda (oh-my-claudecode, wshobson, ruflo, superpowers, ECC, stablyai/orca 56k, superset, herdr); Python cerceveleri (AutoGen/AG2/MetaGPT) geriliyor.

## 5. Gorev / SOP / is akisi dosya olarak
- **dagucloud/dagu** (4.3k, GPL-3) — tek binary YAML DAG; dahili MCP; `harness.run` ile Claude Code adimi; insan gorevleri; zamanlama; kod disi SOP yurutucusu olarak BENIMSE. windmill (17.5k) agir; n8n (205k) entegrasyon icin; dagger CI; temporal ornekleri.
- rogerchappel/agent-runbook-skill — Markdown baslik/liste/checkbox -> sinirli kuru-kosu plani; adim siniflari inspect / external-read / local-change / external-write / **approval-required**; taksonomiyi ODUNC AL.
- Obsidian: obsidian-tasks (4k, aktif) checkbox/tarih grameri BENIMSE; dataview (9.4k, yavasliyor; Bases halef); obsidian-kanban (bakimci ariyor) -> Backlog.md.

## 6. Ses -> not
- openai/whisper (109k; Turkce destekli), **ggml-org/whisper.cpp** (53k) BENIMSE yerel, SYSTRAN/faster-whisper (26k, GPU), m-bain/whisperX (24k; diarizasyon), **cjpais/Handy** (31.5k, MIT) masaustu push-to-talk (Linux x64; Wayland notlari) BENIMSE, k2-fsa/sherpa-onnx (14k), KoljaB/RealtimeSTT (10k), **mbailey/voicemode** (1.4k, MIT) Claude Code ile sesli konusma eklentisi BENIMSE, elevenlabs-mcp bulut yedek, nikdanilov/whisper-obsidian-plugin (376) vault ici yakalama, **rillmd/rill** (7, MIT; Eki 2026) `inbox/ -> /distill -> knowledge/, tasks/`; `/focus` `/close` fiillerini ODUNC AL. FunASR/SenseVoice Turkce yok.

## 7. 3D baski otomasyonu (alan testi)
- Klipper (12k), Arksine/moonraker (1.4k) hedef API, OctoPrint (9k, v1.11.8 Haz 2026). **DMontgomery40/mcp-3D-printer-server** (245, GPL-2; OctoPrint/Moonraker/Duet/Repetier/Bambu/Prusa/Creality; STL donusum, Orca ile otomatik dilimleme) BENIMSE. joeltelling/print-farm-manager (205, MIT; Eki 2026). maziggy/bambuddy (3k, AGPL; Bambu). TheSpaghettiDetective/obico-server (1.9k, AGPL) hata tespiti -> kapi testi. Donkie/Spoolman (2.7k) filament stok API. mainsail/fluidd/KlipperScreen aktif; Frix-x/klippain + shaketune kalibrasyon; mkuf/prind donanimsiz test.
- Dilimleyici: OrcaSlicer (15.4k, CLI), Cura/CuraEngine (7k); PrusaSlicer UNCONFIRMED yildiz.
- Kod-CAD: CadQuery (5.7k), gumyr/build123d (2.9k), **jdilla1277/agentcad** (117, Apache) CAD CLI+MCP (build123d/CadQuery betikleri, STEP+metrik, PNG, A/B diff) BENIMSE, openscad (9.9k), diff3d gorsel diff.
- Metin/gorsel -> 3D: microsoft/TRELLIS.2 (10.9k, MIT; buyuk GPU), Hunyuan3D-2/2.1 (15k; ozel lisans), img2threejs (11.7k); eskiler (dreamfusion, dreamgaussian) terk edilmis.
- Mesh onarim: **mikedh/trimesh** (3.7k, MIT) BENIMSE (watertight -> onar -> eskale), MeshFix, meshlab/pymeshlab.

## Son 90 gun (Tem-Eki 2026) ivme sinyalleri
- CC icin yonetisim/onay araclari en sicak nis: DashClaw, Writ, bernstein, omnigent, agents-shipgate (Eyl sonu-Eki 2).
- LLM-wiki deseni 20+ uygulama; Markdown-gercek-kaynak tasarim hedefi (memsearch, kiwifs, aikito, EverOS, arscontexta).
- Cok ajanli filo kosuculari (orca, superset, herdr, paseo, cmux) oturumlari yonetir, bilgiyi degil; tamamlayici.
- Obsidian: claudian ve claude-obsidian 2026 ortasindan beri ikiye katlandi.
- ADR: 26 Tem 2026'da ~15 yeni "ajanlar icin ADR" reposu; fikir birligi: YAML frontmatter + `affects:` + lint + duzenlemeden once enjekte.

## Benimse / odunc al — ilk 15
1 anthropics/skills + agentskills (BENIMSE format) 2 planning-with-files (ODUNC: uc dosya + PreCompact) 3 karpathy-llm-wiki (ODUNC: raw/wiki/index/log/lint) 4 kepano/obsidian-skills (BENIMSE) 5 Backlog.md (BENIMSE/kopyala gorev karti) 6 agent-decision-record + madr + adrs (BENIMSE karar kati) 7 claude-code-hooks-mastery (ODUNC kapi hook'lari) 8 Writ (ODUNC kapi semantigi) 9 cc-safety-net (BENIMSE) 10 memsearch (BENIMSE/kopyala) 11 bernstein (ODUNC manifest semasi) 12 agentic-sop-to-work + agent-runbook-skill (ODUNC kapi ve yan etki taksonomisi) 13 dagu (BENIMSE yurutucu) 14 claudian + obsidian-local-rest-api (BENIMSE insan arayuzu) 15 claude-obsidian (ODUNC taslak->atomik commit).
Alan testi: mcp-3D-printer-server, agentcad, trimesh, obico-server, Orca CLI. Ses: whisper.cpp/faster-whisper, Handy, voicemode, rill.
Terk edilmis/gerileyen: humanlayer, autogen, ag2, MetaGPT (OSS), get-shit-done (arsiv -> gsd-core), TRELLIS v1, log4brains, adr-tools (durgun), mcp-server-whisper (tasindi), claude-code-spec-workflow, obsidian-kanban (bakimci), Continuous-Claude-v3, ccpm.
