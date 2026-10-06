---
id: 20261006-1901-arastirma-02
ad: hafiza-ve-wiki-duzenleri
tur: kaynak
kat: 0
surum: 1.0
durum: aktif
amac: Yapay zeka ajan hafiza sistemlerinin ve kisisel bilgi/wiki yontemlerinin, duz Markdown ve frontmatter ile isletilen bir ajan wiki'sine donusturulebilecek kurallarini toplamak.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: []
besledigi: [00-sistem/SISTEM.md, 00-sistem/SEMA.md]
kaynaklar: ["https://docs.letta.com/concepts/memory-management", "https://arxiv.org/pdf/2504.19413", "https://arxiv.org/html/2501.13956v1", "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f", "https://www.zettelkasten.de/posts/backlinks-are-bad-links/", "https://johnnydecimal.com/documentation/the-standard-zeros.md", "https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html"]
alindi: 2026-10-06
guven: orta
kaynak_turu: literatur-taramasi
saklama: K
---

# Hafiza sistemleri ve wiki duzenleri

## A. Ajan hafiza sistemleri

### Letta / MemGPT
- Uc katman: cekirdek hafiza bloklari (baglamda, sistem istemine sabit), arsiv (baglam disi, semantik arama), geri cagirma (mesaj gunlugu). https://docs.letta.com/concepts/memory-management
- Blok semasi: `label`, `description`, `value`, `limit`, `read_only`. "description" ajanin bloga nasil yazip okuyacagini belirleyen ana bilgidir. Araclar: append / replace / rethink (tum blogu yeniden yaz). Bloklar ajanlar arasi paylasilabilir. https://docs.letta.com/guides/agents/memory-blocks
- Uyku-zamani ajani (arka plan konsolidasyon): eklemeden once ara (tekrar onleme), oturum sonunda hafif, haftalik tam yeniden duzenleme, aylik hiyerarsik ozet. Topluluk politikasi: oturum baglami 30 gun (3+ atif varsa uzar), karar/tercih hic silinmez, hata notu 14 gun, TODO 90 gunde gozden gecir; "arsiv dizini blogu" = arsivde ne var indeksi. https://forum.letta.com/t/sleeptime-agents-for-memory-consolidation-best-practices-guide/154

### Mem0 (arXiv 2504.19413)
- Iki faz: cikarim (son mesaj cifti + ozet -> "dikkate deger hafizalar") ve guncelleme (benzerleri getir, LLM ADD / UPDATE / DELETE / NOOP secer). Mem0g graf: iliskiler silinmez, gecersiz isaretlenir. https://arxiv.org/pdf/2504.19413

### Zep / Graphiti (arXiv 2501.13956)
- Uc alt graf: epizot (ham), varlik (olgu kenarlari), topluluk. Cift zamanli model: `created_at/expired_at` ve `valid_at/invalid_at`; celiski -> `invalid_at` set, silme yok, olgu metni gecmis zamana cevrilir. https://www.getzep.com/blog/beyond-static-knowledge-graphs/

### LangGraph
- Kisa vadeli (thread) vs uzun vadeli (Store, hiyerarsik namespace + key). Turler: semantik (olgu), epizodik (olay/ornek), prosedurel (kural). Profil (tek JSON, buyudukce kayip riski) vs koleksiyon (cok kucuk belge, LLM icin kolay). Yazim zamani: sicak yol (anlik) vs arka plan. https://docs.langchain.com/oss/python/concepts/memory

### Anthropic memory tool
- `memory_20250818`: `/memories` altinda view/create/str_replace/insert/delete/rename; "KESINTIYI VARSAY, tum ilerlemeyi kaydet". https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool

### Claude Code otomatik hafiza (2026)
- `~/.claude/projects/<proje>/memory/MEMORY.md` indeks (satir basina bir hafiza; ilk 200 satir / 25 KB yuklenir) + konu dosyalari. Turler: `user`, `feedback`, `project`, `reference`. Koddan turetilebileni ve CLAUDE.md'de olani kaydetme. `modified` alanini otomatik ekler. https://code.claude.com/docs/en/memory

### Generative Agents (Park ve ark. 2023)
- Hafiza akisi: aciklama + olusturma zamani + son erisim. Getirme puani = yenilik (0.995^saat) + onem (LLM 1-10) + ilgi (kosinus). Yansima: son olaylarin onem toplami > 150 olunca "en belirgin 3 ust duzey soru" -> kanit atifli icgoruler, agac olarak saklanir. https://arxiv.org/pdf/2304.03442

### CoALA taksonomisi
- Calisma hafizasi + uzun vadeli: epizodik, semantik, prosedurel. https://arxiv.org/pdf/2309.02427

### "LLM wiki" deseni (Karpathy, Nisan 2026)
- Uc katman: `raw/` (degismez kaynaklar), `wiki/` (LLM'in sahibi oldugu sayfalar), sema (CLAUDE.md/AGENTS.md). `index.md` icerik katalogu (link + tek satir ozet), `log.md` kronolojik, salt ekleme. Is akislari: ingest, query, lint (celiskiler, bayat iddialar, yetim sayfalar). Sayfalar artimli guncellenir, yeniden uretilmez. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Topluluk frontmatter'i: `title, type, sources, related, created/updated, confidence`. Lint skill ornegi: olu/belirsiz link, yetim, zorunlu alan eksik, bos bolum, bayat indeks. https://github.com/Astro-Han/karpathy-llm-wiki

## B. Kisisel bilgi / wiki yontemleri
- Zettelkasten: atomiklik, kalici kimlik, **baglantinin nedeni yazilir** ("otomatik backlink kotu linktir"). https://www.zettelkasten.de/posts/backlinks-are-bad-links/
- Evergreen notlar (Matuschak): atomik, kavram odakli, yogun baglantili, basliklar API gibi. https://notes.andymatuschak.org/Evergreen_notes_should_be_concept-oriented
- LYT / MOC (Milo): icerik haritasi notu, "sikisma noktasinda" acilir; `up:: [[Ust]]` alani. https://notes.linkingyourthinking.com/Cards/MOCs+Overview
- Johnny.Decimal: alanlar 10-19, kategoriler 11, kimlikler 11.01; en fazla 10 alan, 10 kategori, 100 kimlik; standart sifirlar: 00-09 sistem, .00 indeks, .01 gelen kutusu, .03 sablonlar, .05 "yapay zeka ajani icin yer", .09 arsiv. https://johnnydecimal.com/documentation/the-standard-zeros.md
- PARA: Projeler / Alanlar / Kaynaklar / Arsiv; eyleme gore duzenle. https://fabric.so/learn/para-method
- Dendron: hiyerarsi dosya adinda (`a.b.c.md`), sema dosyalari ile dogrulama. https://wiki.dendron.so/
- Obsidian: ozellikler = YAML (`tags`, `aliases`; linkler tirnakli `"[[Not]]"`); wikilink varsayilan; linkler vs etiketler vs klasorler birbirine dik; Dataview cikti grep/git/ajan icin gorunmez -> onemli sonuclar duz Markdown'a yazilir; Bases `.base` dosyalari duz dosya alternatifi. https://obsidian.md/help/properties
- Lint araclari: obsidian-linter (yaml-timestamp, yaml-key-sort, header-increment...), Vault Inspector (kirik link, yetim), Vault Link Check (yeniden adlandirilmis vs planlanmis). https://github.com/platers/obsidian-linter

## C. Muhendislik belge sozlesmeleri
- ADR (Nygard): Baslik, Baglam, Karar, Durum (onerildi/kabul/kaldirildi/yerine gecildi), Sonuclar; degisiklik yerine gecme ile. https://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions
- MADR 4.0: frontmatter `status, date, decision-makers, consulted, informed`; bolumler: baglam ve problem, surucu etkenler, secenekler, karar, sonuclar (iyi/kotu), dogrulama, artı/eksi. https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html
- Diataxis: tutorial / how-to / referans / aciklama; karistirma. https://www.diataxis.fr/start-here/
- Keep a Changelog 1.1.0: surum basina giris; Eklendi/Degisti/Kaldirildi/Duzeltildi/Guvenlik; en yeni ustte; ISO tarih. https://keepachangelog.com/en/1.1.0/
- SemVer 2.0.0. https://semver.org/

## Sentez: ajan-bakimli duz Markdown wiki icin onerilen sozlesmeler
1. **Frontmatter** (her sayfa): `id` (degismez zaman damgali), `ad`, `tur`, `kat`, `durum` (taslak|aktif|kabul|reddedildi|yerine-gecildi|arsiv), `surum`, `olusturma`, `guncelleme`, `son_gozden_gecirme`, `yazar`, `kaynaklar` (list), `guven` (yuksek|orta|dusuk), `onem` (1-10), `ust` (tek MOC), `dayandigi`, `besledigi`, `yerine_gecti`, `yerine_gecen`, `gecerli_baslangic/bitis`, `etiketler`, `takma_adlar`, `talimat`.
2. **Baglanti**: yalniz wikilink; govdede her link `[[Hedef]] — neden` bicimiyle; iki yonlu: A -> B yazilinca B'de `<- [[A]] — ayni neden` satiri; her sayfanin tek `ust` MOC'u; yansima/karar kanit atifli.
3. **Indeks/MOC**: `HARITA.md` satir basina bir sayfa, ~200 satir tavan, asinca MOC'lere bolunur; `GUNLUK.md` salt ekleme, sabit onekli; `DEGISIKLIKLER.md` keep-a-changelog; her ingest = sayfa yaz -> etkilenenleri guncelle -> HARITA -> GUNLUK (atomik).
4. **Tur taksonomisi**: gozlem (epizodik), fikir (aday semantik), karar (ADR), gorev (calisma), yansima (icgoru, >=2 kanit), kural (prosedurel), kisi/varlik, kavram (evergreen), kaynak (ozet), referans (isaretci), moc.
5. **Terfi/unutma/arsiv**: sicak yol yalniz gozlem/gorev/karar yazar; arka plan "uyku" konsolide eder. gozlem -> fikir (>=2 bagimsiz gozlem), fikir -> kavram/kural (guven yuksek + >=2 atif), yansima (onem toplami > esik). ADD/UPDATE/DELETE(->gecersiz)/NOOP once ara. Celiski = eski sayfaya `gecerli_bitis` + `yerine_gecen`, silme yok. Varsayilan sureler: gozlem 30 gun (>=3 atif yoksa), gorev 90 gunde gozden gecir, karar/kural hic. Koddan turetilebileni ve CLAUDE.md'de olani kaydetme. `son_gozden_gecirme` > 60 gun -> bayat.
6. **Lint (13 denetim)**: frontmatter var/gecerli/enum; id tekil; olu/belirsiz link; yetim (gelen link yok ve HARITA'da yok); karsiliklilik (A->B ise B'de <-A ve neden dolu); `ust` var ve MOC; HARITA butunlugu ve boyutu; GUNLUK kaydi; bayat (gozden gecirme, gecerli_bitis gecmis); ADR butunlugu (kabulden sonra yalniz yerine_gecen degisir, simetrik); bos bolum/placeholder/baslik hiyerarsisi; semantik celiski (LLM, raporla, duzeltme); Dataview sonucu duz Markdown'a serilestirilmis mi.
