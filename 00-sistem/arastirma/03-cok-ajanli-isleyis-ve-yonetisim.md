---
id: 20261006-1902-arastirma-03
ad: cok-ajanli-isleyis-ve-yonetisim
tur: kaynak
kat: 0
surum: 1.0
durum: aktif
amac: Cok ajanli mimari desenlerini, insan-dongude yonetisim araclarini (kapilar, karar haklari, karar kayitlari, brifing bicimleri), orgut tasarimi kurallarini ve fikir olgunlastirma yontemlerini isletim kurallarina donusturmek.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: []
besledigi: [30-devlet/normlar/ANAYASA.md, 30-devlet/kararlar/K-001-pilotta-kadro-yok.md]
kaynaklar: ["https://www.anthropic.com/engineering/building-effective-agents", "https://www.anthropic.com/engineering/multi-agent-research-system", "https://arxiv.org/abs/2503.13657", "https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/", "https://adr.github.io/madr/", "https://en.wikipedia.org/wiki/BLUF_(communication)"]
alindi: 2026-10-06
guven: orta
kaynak_turu: literatur-taramasi
saklama: K
---

# Cok ajanli isleyis, yonetisim ve orgut tasarimi

## A. Cok ajanli mimari desenleri
- Anthropic "Building effective agents" (Ara 2024): is akislari (onceden tanimli yol) vs ajanlar (kendi yolunu secer). Bes desen: istem zinciri, yonlendirme, paralellestirme, orkestrator-isci, degerlendirici-iyilestirici. Basitlik, seffaflik, iyi arac arayuzu; karmasikligi yalniz basit cozum yetmeyince ekle. https://www.anthropic.com/engineering/building-effective-agents
- Anthropic cok ajanli arastirma sistemi (Haz 2025): gorev tanimi = hedef + cikti bicimi + arac/kaynak rehberi + sinirlar. Caba olcegi: basit = 1 ajan 3-10 cagri; karsilastirma = 2-4 ajan 10-15 cagri; karmasik = 10+ ajan. 3-5 paralel ajan sureyi %90 kisaltir; maliyet ~15x sohbet; token kullanimi performans varyansinin ~%80'ini aciklar. Son-durum degerlendirmesi, LLM-hakem rubrigi. Hatalar: basit soruya cok ajan, var olmayan kaynagi aramak, gorev bolusmeden tekrar, sirali calisma. https://www.anthropic.com/engineering/multi-agent-research-system
- Baglam muhendisligi (Eyl 2025): "context rot"; dogru irtifada sistem istemi; araclar cakismasin; tam zamaninda getirme (yol/kimlik); sikistirma; yapili not alma (NOTES.md); alt ajan 1-2K token ozet dondurur. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Araclar icin yazim (Eyl 2025): az ve birlesik arac; ad alani; okunabilir kimlikler; sayfalama; "yeni ekip uyesine anlatir gibi". https://www.anthropic.com/engineering/writing-tools-for-agents
- Uzun sureli ajanlar icin harness: baslatici ajan (init.sh, ilerleme dosyasi, ozellik listesi `passes: false`), oturum basina tek ozellik, "testleri silmek/duzenlemek kabul edilemez", oturum acilis listesi (pwd, git log, ilerleme oku, smoke test). https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Evals: gorev/deneme/hakem; kod tabanli, model tabanli, insan; sureci degil urunu puanla; pass@k vs pass^k; 20-50 gercek hata senaryosu. https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Claude Code alt ajan ve ajan takimlari: 3-5 takim arkadasi ile basla, isci basina 5-6 gorev, "uc odakli bes daginiktan iyidir"; her isci farkli dosyalara sahip; ajan mesaji onay degildir; maliyet ~7x. https://code.claude.com/docs/en/agent-teams
- OpenAI "practical guide": tek ajanla basla; cakisan araclar sayidan daha onemli; yonetici vs merkezi olmayan devir; korkuluklar; insan mudahale tetikleyicileri (tekrar esigi, yuksek riskli eylem). https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- Google ADK: koordinator, sirali, paralel, hiyerarsik, uretici-elestirmen, insan dongude. https://adk.dev/workflows/
- Magentic-One: Gorev Defteri (olgular, tahminler, plan) + Ilerleme Defteri (tamam mi? ilerliyor mu? takildi mi? sonraki konusmaci); duraklama sayaci yeniden planlama tetikler. https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/
- MetaGPT: SOP'lar istem dizisi; roller yapili artefakt uretir; yurutulebilir geri bildirim (test, 3 deneme). https://arxiv.org/abs/2308.00352
- AGENTS.md: ajanlar icin README; 60.000+ repo; Agentic AI Foundation. https://agents.md/
- MAST (Cemri 2025): 1600+ iz, 14 hata modu, 3 sinif: spesifikasyon (gorev ihlali %11.8, adim tekrari %15.7, bitisi bilmeme %12.4), ajanlar arasi (acikliga kavusturma istememe %6.8, raydan cikma %7.4, akil-eylem uyumsuzlugu %13.2), dogrulama (erken bitirme %6.2, eksik dogrulama %8.2, yanlis dogrulama %9.1). CEO onayi +9.4, ust duzey hedef dogrulamasi +15.6 puan. https://arxiv.org/abs/2503.13657
- Cognition "Don't build multi-agents": tam izi paylas; paralel uygulayicilar uyumsuz ciktilar uretir; tek thread + sikistirma tercih. https://cognition.com/blog/dont-build-multi-agents
- LLM-hakem onyargilari (Zheng 2023): konum, uzunluk, kendini begenme. https://arxiv.org/abs/2306.05685

## B. Insan-dongude yonetisim
- Stage-Gate (Cooper): her kapi = teslimatlar + kriterler (zorunlu/istenen) + cikti (Go/Kill/Hold/Recycle); kapi bekcileri kaynak sahipleri. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- Kalite kapilari (SonarQube): yeni kodda sifir sorun, kapsama >=%80; Definition of Done (Scrum): karsilamayan artim yayinlanamaz; INVEST (gorev kartlari). https://scrumguides.org/scrum-guide.html
- Karar haklari: RACI (tek Accountable), DACI (tek Approver; karar belgesi alanlari), RAPID (Recommend/Agree/Perform/Input/Decide), Appelo 7 devretme seviyesi (Tell, Sell, Consult, Agree, Advise, Inquire, Delegate). https://www.atlassian.com/team-playbook/plays/daci https://management30.com/practice/delegation-poker/
- Amazon: tek yonlu kapi (geri alinamaz, yavas) vs cift yonlu (hizli, %70 bilgiyle); disagree and commit; PR/FAQ; iki pizza takimi. https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders
- Gorevler ayriligi, dort goz, IIA Uc Hat (3. hat bagimsiz denetim, yonetim kuruluna hesap verir). https://en.wikipedia.org/wiki/Three_lines_of_defence
- Karar kayitlari: Nygard ADR, MADR 4.0 (`status, date, decision-makers, consulted, informed`; dogrulama bolumu), karar gunlugu (Farnam Street: durum, cerceve, alternatifler, beklenen sonuc + olasilik, zihinsel durum), pre-mortem (Klein, +%30 neden tespiti). https://adr.github.io/madr/ https://fs.blog/decision-journal/ https://hbr.org/2007/09/performing-a-project-premortem
- Brifing: BLUF (ACTION/INFO/DECISION), SBAR, komutan niyeti (amac + kilit gorevler + son durum; "ne ve neden, nasil degil"), AAR (ne planlandi/ne oldu/neden/ne surdurulur). https://en.wikipedia.org/wiki/BLUF_(communication) https://armypubs.army.mil/epubs/DR_pubs/DR_a/ARN34403-ADP_6-0-000-WEB-3.pdf

## C. Orgut tasarimi (kadro yoneticisi icin)
- Team Topologies: akis-hizali, etkinlestirici, karmasik-alt-sistem, platform; etkilesim: isbirligi (pahali, sureli), hizmet, kolaylastirma; her parcanin tek sahibi; bilissel yuk asinca bol; takim 5-9. https://teamtopologies.com/learn
- Conway yasasi; kontrol araligi 3-6 klasik (standart isler daha genis); Brooks yasasi; Greiner (yaraticilik->liderlik krizi, yon->ozerklik, devretme->kontrol, koordinasyon->kirtasiye, isbirligi). https://en.wikipedia.org/wiki/Span_of_control

## D. Ic Ses katmani (dusunceden brife)
- GTD: yakala, netlestir (eyleme donusur mu?), duzenle, gozden gecir (haftalik), yap. https://gettingthingsdone.com/what-is-gtd/
- Zettelkasten (Ahrens): ucucu not 1-2 gunde islenir; kalici not tek fikir, kendi kelimeler, bagimsiz, nedenli link. https://zettelkasten.de/introduction/
- Olgunluk merdivenleri: TRL 1-9 (kanitla terfi), Double Diamond (kesfet-tanimla-gelistir-teslim), Stage-Gate ideation, PR/FAQ (cogu asla yayinlanmaz). https://www.designcouncil.org.uk/our-resources/framework-for-innovation/

## Sentez: isletim kurallari
1. **Gorev karti (12 alan)**: kimlik ve ust kayit; amac (neden, tek cumle); hedef/son durum (gozlemlenebilir); kilit gorevler (2-6; ne, nasil degil); kabul olcutleri (her biri test edilebilir, kanit komutu adli); kapsam sinirlari (dahil dosyalar, acikca haric, dokunma listesi); girdiler (yol/link, yapistirilmis icerik degil); izinli araclar + model/caba + butce (tur/token/zaman); cikti bicimi ve uzunluk tavani; kisitlar ve risk sinifi (tek/cift yonlu kapi; eskalasyon); devretme seviyesi (1-7); sahip (tek) ve inceleyici (uygulayicidan farkli).
2. **Devir-teslim**: brif yazan spawner; alici sifir gecmisle baslar; donus = 1-2K token, once kanit, sonra acik sorular ve "ortulu aldigim kararlar"; kabul = son durum kontrolu, yazar disinda biri; inceleyici yalnizca dogruluk/gereksinim bosluklarini raporlar; DoD: kanitla karsilanmis olcutler, testler zayiflatilmamis, kapsam disi degisiklik yok, notlar guncel, commit. Belirsiz olcut -> uygulamadan once DUR ve SOR. Paralel uygulayicilar dosya paylasmaz. Her seferinde olmasi gerekenler hook ile.
3. **Onay kapilari**: her karari sinifla: cift yonlu -> devret (seviye 5-7), %70 bilgiyle karar, sonradan kaydet; tek yonlu -> kapi + insan Decide + buyuklerde pre-mortem. Varsayilan tek yonlu kapilar: acik API/sema degisikligi, veri silme/goc, bagimlilik/mimari secimi, yayin, guvenlik/izin degisikligi, butce esigi ustu harcama, kimlik bilgisi/uretim, anayasa degisikligi. Kapi = gerekli teslimatlar + zorunlu (ikili) ve istenen (puanli) kriterler + Go/Kill/Hold/Recycle + tek bekci. Minimum merdiven: G0 fikir->brif, G1 plan onayi, G2 DoD + bagimsiz inceleme, G3 yayin. Gorev ayriligi: uygulayici != inceleyici != yayinci; denetim insana rapor verir. Eskalasyon tetikleyicileri: 2 basarisiz duzeltme, N turda ilerleme yok, yuksek riskli eylem, butce asimi, olcut ihtilafi. Ajan mesaji onay degildir.
4. **Karar kaydi alanlari**: id, tarih, baslik, durum, kapi turu + devretme seviyesi, surucu, karar veren (tek), danisilan, bilgilendirilen, baglam/problem, kriterler, secenekler (arti/eksi/maliyet), karar ("... yapacagiz"), beklenen sonuc + guven (%), sonuclar (iyi/kotu/notr), dogrulama (nasil ve ne zaman), gorev karti ve commit baglantilari. Silinmez, yerine gecilir.
5. **Brifing (BLUF)**: konu etiketi ACTION/DECISION/INFO; BLUF 1-2 cumle; durum (istek kimligi); kanit (komut, test, degisen dosyalar); degerlendirme (risk, sapma, ortulu kararlar); oneri/istek (karar, tarih, varsayilan secenek); acik sorular ve sonraki adim; tavan 1.500-2.000 token (ajan->orkestrator), tek sayfa (orkestrator->insan).
6. **Fikir olgunluk basamaklari**: M0 ucucu (48 saatte islenir/atilir), M1 netlestirilmis (eyleme donusur mu; sonraki adim tek cumle), M2 kalici not (soguk okur anlar), M3 problem cercevelenmis, M4 secenek + pre-mortem (>=2 secenek, geri alinabilirlik, maliyet; tek yonluler karar gunlugune), M5 brif (12 alan dolu, INVEST gecer). Yalniz M5 sirket katina girer. Oldurme/bekletme her basamakta normal cikis; haftalik gozden gecirme M1-M4'u yeniden eler.
7. **Ajan sayisi ve maliyet**: varsayilan tek ajan; ikinciyi yalniz yalitim, temiz baglamli inceleme veya gercek paralellik icin ekle. Caba katmanlari (1 / 2-4 / 10+). Takim 3-5, isci basina 5-6 gorev. Butce: cok ajan ~15x sohbet; isciler Sonnet/Haiku, mimar/inceleme Opus; her brife maxTurns ve butce; bos isciyi kapat. Orkestrator 3-6 es zamanli isciyi dogrudan yonetir; derinlik <=2.
8. **Hata modlari listesi** (pre-mortem ve AAR'da): spesifikasyon (hedef/bicim/sinir eksik, rol karisikligi, olcut yok, bitis kosulu yok, dongu); koordinasyon (cakisan brif, paralel celisen kararlar, ayni dosya, devirde kayip baglam, soru sormama, raydan cikma, bilgi saklama, aktarilan "onay"); dogrulama (erken bitti, test silme, ucten uca kontrol yok, inceleyici = yazar, hakem onyargisi, kapi hook yerine duz yazi); ekonomi (basit ise cok ajan, sirali/paralel yanlisligi, butcesiz kosu, bos isci, her seyi tek oturuma yigma, 2'den fazla duzeltme); yonetisim (cift yonluye agir kapi, tek yonluye kapi yok, kayitsiz karar, bagimsiz denetim yok, sisirilmis CLAUDE.md).
