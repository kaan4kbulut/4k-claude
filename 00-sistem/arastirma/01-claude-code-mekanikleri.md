---
id: 20261006-1900-arastirma-01
ad: claude-code-mekanikleri
tur: kaynak
kat: 0
surum: 1.0
durum: aktif
amac: Claude Code'un CLAUDE.md, hafiza, alt ajan, hook, skill, izin ve oturum mekaniklerini resmi belgelerden dogrulanmis haliyle tek yerde toplamak; sistemin hicbir kurali var olmayan bir ozellige dayanmasin.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: []
besledigi: [00-sistem/SEMA.md, 00-sistem/arastirma/04-guvenilirlik-ve-kalite-teknikleri.md]
kaynaklar: ["https://code.claude.com/docs/en/memory.md", "https://code.claude.com/docs/en/sub-agents.md", "https://code.claude.com/docs/en/hooks.md", "https://code.claude.com/docs/en/skills.md", "https://code.claude.com/docs/en/best-practices.md"]
alindi: 2026-10-06
guven: orta
kaynak_turu: resmi-belge-taramasi
saklama: K
---

# Claude Code mekanikleri (resmi belgeler, Ekim 2026)

Kaynak: code.claude.com/docs. UNCONFIRMED = birincil kaynakta dogrulanamadi.

## 1. CLAUDE.md / hafiza
- Yukleme sirasi (genisten ozele): `~/.claude/CLAUDE.md` -> `.claude/CLAUDE.md` -> `.claude/CLAUDE.local.md` (gitignore, kisisel) -> alt klasorlerdeki CLAUDE.md. Ozel olan genisi ezer. Hepsi oturum basinda baglama acilir. https://code.claude.com/docs/en/memory.md
- `@path` import: tirnaksiz, bosluk `\ ` ile; goreli ve mutlak yol; en fazla 4 seviye ic ice; backtick icindeki `@` ve kod bloklari import sayilmaz; proje disi yol ilk yuklemede onay ister.
- Boyut: dosya basina 200 satirin alti hedef; uzun dosya baglami yer ve uyumu dusurur. Test: "bu satiri silsem Claude hata yapar mi?" Hayirsa sil. Icerik: tahmin edilemeyen komutlar, varsayilandan farkli stil, test talimatlari, mimari kararlar, tuzaklar. Disarida: apacik seyler, API dokumani (link ver), sik degisen bilgi, dosya dosya aciklama.
- `.claude/rules/*.md`: yol kapsamli kurallar (`paths:` frontmatter), eslesen yolda calisirken yuklenir. Kapsamsiz kurallar her oturumda yuklenir ve sikistirmadan sonra diskten yeniden enjekte edilir.
- `/init` baslangic CLAUDE.md uretir; `/doctor` sisirilmis dosyaya kesinti onerir. `AGENTS.md` alternatif; `projectInstructions` ayari hangisinin okunacagini belirler.
- UNCONFIRMED: `#` kisayolu, `/memory` komutu (belgede `/context` var).

## 2. Alt ajanlar (subagents)
- Konum: `.claude/agents/<ad>.md` (proje) veya `~/.claude/agents/` (kullanici). Oncelik: yonetilen ayarlar > `--agents` > proje > kullanici > eklenti. https://code.claude.com/docs/en/sub-agents.md
- Frontmatter: `name` (zorunlu), `description` (zorunlu; tum aciklamalar toplam ~15.000 token), `tools` (izin listesi), `disallowedTools`, `model` (sonnet|opus|haiku|fable|inherit), `permissionMode` (default|acceptEdits|auto|dontAsk|bypassPermissions|plan), `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory` (user|project|local), `background`, `omitClaudeMd`, `effort`, `isolation: worktree`, `color`, `initialPrompt`, `experimental.cacheTtl`.
- Arac kisiti: `tools` izin listesidir; salt okunur icin `permissionMode: plan` kullan. Bos arac kumesi hata verir. `tools: Agent(worker, researcher)` ile hangi alt ajanlari acabilecegi sinirlanir.
- Baglam: fork olmayan alt ajan TEMIZ baslar: kendi sistem istemi + gorev mesaji + CLAUDE.md (omitClaudeMd degilse) + git durumu + onyuklu skill'ler + kardes listesi. Konusma gecmisini GORMEZ. Fork her seyi devralir.
- Ic ice: varsayilan 3 seviye (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`). Es zamanli: varsayilan 20 (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`). Arka plan alt ajanlarinin arac kumesi kisitli.
- Devretme: `description` ile otomatik ("use proactively"), `@"ajan-adi"` ile acik, `claude --agent` ile oturum geneli; `SendMessage` ile devam.
- Hafiza: `memory:` alani ile `.claude/agent-memory/<ad>/` altinda `MEMORY.md` (ilk 200 satir / 25 KB yuklenir).

## 3. Hook'lar
- Olaylar: SessionStart, Setup, SessionEnd, UserPromptSubmit, UserPromptExpansion, Stop, StopFailure, PreToolUse, PostToolUse, PostToolUseFailure, PostToolBatch, PermissionRequest, PermissionDenied, Notification, MessageDisplay, SubagentStart, SubagentStop, TaskCreated, TaskCompleted, TeammateIdle, FileChanged, CwdChanged, DirectoryAdded, WorktreeCreate/Remove, ConfigChange, InstructionsLoaded, PreCompact, PostCompact, PreModelSwitch, PostModelSwitch, Elicitation, ElicitationResult. https://code.claude.com/docs/en/hooks.md
- Yer: `settings.json` (`hooks` blogu). Eslestirici: `*`/bos = hepsi; harf-rakam listesi = tam eslesme (`Edit|Write`); diger = regex.
- Cikis kodu: 0 = basari (stdout JSON ise islenir); **2 = ENGELLE** (PreToolUse, UserPromptSubmit, Stop, SubagentStop, PostToolBatch, ConfigChange, PreCompact, TaskCreated, TaskCompleted, TeammateIdle vb.); diger = engellemeyen hata. Zaman asimi: 600 sn varsayilan; PreToolUse zaman asimi araci ENGELLEMEZ.
- JSON cikti: `continue`, `stopReason`, `systemMessage`, `hookSpecificOutput` (PreToolUse: `permissionDecision` allow|deny|ask|defer, `updatedInput`, `additionalContext`; PostToolUse: `updatedToolOutput`; Stop: `decision: block`, `reason`, `additionalContext`; SessionStart: `additionalContext`, `sessionTitle`, `watchPaths`, `initialUserMessage`).
- Stop hook: Claude'un gordugu metin `additionalContext`tir, `reason` kullaniciya gider; ust uste 8 engelden sonra durur (`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`); `stop_hook_active` ile dongu onlenir. Isleyici turleri: command, http, mcp_tool, prompt, agent (deneysel).
- Ornek PreToolUse (yazmayi klasorle sinirla): `jq` ile `tool_name` ve `tool_input.file_path` oku; izinli yol disindaysa `permissionDecision: deny` dondur. Ornek Stop: betik basarisizsa `decision: block` + `additionalContext`.

## 4. Skill'ler
- `.claude/skills/<ad>/SKILL.md`; frontmatter: `name`, `description`, `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context: fork`, `agent`, `background`, `hooks`, `paths`, `shell`, `metadata`, `license`, `compatibility`. https://code.claude.com/docs/en/skills.md
- Tetikleme: Claude otomatik (`description` eslesirse ve `disable-model-invocation` degilse) veya `/ad arg`. `!`komut`` ile dinamik enjeksiyon; `$ARGUMENTS`, `$0`, `$ad`. SKILL.md 500 satir alti onerilir.
- Maliyet: aciklamalar her istekte, govde kullanimda; `disable-model-invocation: true` = cagrilana kadar sifir maliyet (yan etkili komutlar icin ideal).

## 5. Ayarlar ve izinler
- Oncelik: CLI bayraklari > `.claude/settings.local.json` > `.claude/settings.json` > `~/.claude/settings.json` > yonetilen ayarlar > ortam degiskenleri. https://code.claude.com/docs/en/settings-reference.md
- Kurallar: `permissions.allow / ask / deny`, bicim `Arac(icerik)`: `Bash(git commit:*)`, `Edit(src/**)`, `Read(./.env)`, `mcp__github`. Oncelik deny > ask > allow; genis kural dar kurali ezmez. Bash eslesmesi metinseldir (`git -C d push` kacar) -> tam komut denetimi icin PreToolUse hook.
- Modlar: default/manual, acceptEdits, auto (siniflandirici; Pro/Max/Team varsayilani), dontAsk, bypassPermissions, plan (salt okunur). `permissions.deny` auto-mode siniflandiricidan once uygulanir ve ezilemez; `permissions.ask` auto modda bile insan sorusu zorlar.
- Sandbox: `sandbox.enabled`, `network.allowedDomains`, `failIfUnavailable`; hook'lar, MCP sunuculari, Read/Edit/WebFetch sandbox disinda calisir. Linux: bubblewrap + socat.

## 6. Oturum
- `/compact [odak]`, `/clear`, `--continue`, `--resume <ad|id>`, `/export`. Baslangicta CLAUDE.md'ler + git durumu yuklenir, SessionStart hook'lari calisir. https://code.claude.com/docs/en/sessions.md
- Sikistirmadan sag cikanlar: sistem istemi, kok CLAUDE.md, kapsamsiz `.claude/rules`, otomatik hafiza, plan; yol kapsamli kurallar ve hook metni OZETLENIR; CLAUDE.md'de `## Compact instructions` bolumu korunacaklari soyler.
- Checkpoint (dosya anlik goruntusu, `/rewind`) git degildir; Bash degisiklikleri izlenmez. Gercek geri alma = git.
- `/goal <kosul>`: her turdan sonra kucuk model transkriptten "oldu/olmadi/imkansiz" yargilar; "veya 20 turdan sonra dur" ile sinirla.
- Zamanlama: `/loop`, CronCreate (oturum ici, 7 gun), Masaustu zamanli gorevler (yerel, 1 dk), Bulut Rutinler (1 saat, onay istemez), kanallar (Telegram/Discord) arastirma onizlemesi.
- `/voice`: tut/tiklamali dikte; Turkce destekli; prompt'a yazar, dosyaya degil; 2 dk tavan.

## 7. Resmi en iyi uygulamalar
- Kesfet -> Planla -> Uygula -> Commit; tek cumleyle anlatilabilen degisiklikte plani atla. https://code.claude.com/docs/en/best-practices.md
- "Claude'a calistirabilecegi bir kontrol ver": test, derleme, ekran goruntusu; kanit iste, iddia degil. Kapi sertlik merdiveni: istem ici kontrol -> `/goal` -> Stop hook (deterministik) -> dogrulama alt ajani (temiz baglam).
- Alt ajanlari baglami korumak icin kullan; Yazar/Inceleyici ayrimi; "bosluklari raporla, stil degil".
- Iki basarisiz duzeltmeden sonra `/clear` ve istemi yeniden yaz.
- Hook deterministik, CLAUDE.md tavsiyedir: her seferinde olmasi gerekenler hook'a.

## Yeni Sistem icin dogrudan sonuclar
1. Kural (CLAUDE.md) ile engel (hook) ayri seylerdir; "yarim yolda kalmama" hook'larla saglanir.
2. Alt ajan konusmayi gormez; gorev karti ve dosyaya yazim zorunludur.
3. Dinamik durum (ilerleme, tarih) CLAUDE.md'ye degil, SessionStart hook ciktisina girer (onbellek kararliligi).
4. Devlet kati dosyalari `permissions.ask` ile korunur; anayasa `permissions.deny` ile yalnizca insan tarafindan degisir.
