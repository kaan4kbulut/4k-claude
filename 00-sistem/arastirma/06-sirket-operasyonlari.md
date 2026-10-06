---
id: 20261006-1905-arastirma-06
ad: sirket-operasyonlari
tur: kaynak
kat: 0
surum: 1.0
durum: aktif
amac: Gercek sirket operasyon bilgisini (SOP, surec haritalari, roller, kalite, tedarik, finans, ritim, KPI, eskalasyon) sirket katina kodlanabilir hale getirmek.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: []
besledigi: [20-sirket/SCORECARD.md, 20-sirket/RITIM.md, 20-sirket/alan-paketleri/3d-uretim.md]
kaynaklar: ["https://www.epa.gov/sites/default/files/2015-06/documents/g6-final.pdf", "https://www.eosworldwide.com/faq", "https://handbook.gitlab.com/handbook/company/culture/all-remote/handbook-first/", "https://kanbanguides.org/the-kanban-guide/2025.5/", "https://www.lrqa.com/en-gb/latest-news/iso-9001-publication-date-confirmed/", "https://www.parasut.com/blog/e-arsiv-fatura-limitleri", "https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai"]
alindi: 2026-10-06
guven: orta
kaynak_turu: literatur-taramasi
saklama: K
---

# Sirket operasyonlari bilgisi

## 1. Isletim modelleri ve SOP
- SOP bicimi (EPA QA/G-6): baslik/kimlik/tarih/imza, kapsam, yontem ozeti, tanimlar, guvenlik, personel sorumluluklari, ekipman, adim adim prosedur (sorun giderme dahil), kayit yonetimi, QA/QC, referanslar; 1-2 yilda bir gozden gecirme. https://www.epa.gov/sites/default/files/2015-06/documents/g6-final.pdf
- BPMN: akis nesneleri (olay, aktivite, gateway XOR/AND/OR), yuzme kulvarlari (havuz = kurum, kulvar = rol), artefaktlar. Kulvar = rol; gateway = "tek basina / eskale" noktasi. https://www.heflo.com/guides/bpmn
- RACI: tek Accountable. EOS/Traction: V/TO, Accountability Chart (koltuk basina 5 rol, koltuk basina tek kisi), Scorecard (5-15 haftalik sayi, sahip ve hedefli), Rocks (90 gun, 3-7), Level 10 toplanti (90 dk: segue 5 / scorecard 5 / rocks 5 / basliklar 5 / to-do 5 / IDS 60 / kapanis 5). https://www.eosworldwide.com/faq
- Scaling Up (Rockefeller Habits): gunluk huddle, haftalik, aylik, ceyreklik, yillik ritim; tek sayfa stratejik plan. https://scalingup.com/growth-tools
- GitLab handbook-first: "once el kitabini degistir, sonra duyur"; el kitabinda olmayan karar yoktur. Yeni Sistem'in dosya kati = el kitabi. https://handbook.gitlab.com/handbook/company/culture/all-remote/handbook-first/
- Kontrol listeleri (Gawande): DO-CONFIRM vs READ-DO; duraklama noktasi basina 5-9 madde; yalniz kritik maddeler; tek sayfa. https://www.ycn.org/resources/all/a-checklist-for-checklists-five-things-to-tick-off-when-developing-a-checklist
- Lean: standart is (takt, sira, standart WIP) kaizen'in tabani; 5S; PDCA; kanban cekme sinyali. https://www.lean.org/the-lean-post/articles/what-you-need-to-know-about-standardized-work/
- DMAIC: Define-Measure-Analyze-Improve-Control. https://asq.org/quality-resources/dmaic
- Kisitlar teorisi: kisiti bul -> somur -> her seyi ona tabi kil -> yukselt -> tekrar. Tek kisilik ureticide kisit = sahibin fiziksel saatleri; YZ kati her seyi buna tabi kilar. https://www.tocinstitute.org/five-focusing-steps.html

## 2. Proje ve is yonetimi
- PMBOK 7 (12 ilke, 8 alan) ve PMBOK 8 (Kas 2025: 6 ilke, 7 alan, surec gruplari geri geldi, YZ egilimi). https://pmstudycircle.com/pmbok-guide-7th-vs-8th-edition/
- Kanban Guide 2025.5: is akisi tanimi (deger birimi, baslangic/bitis, durumlar, WIP kontrolu, acik politikalar, SLE); dort olcum: WIP, verim, is yasi, cevrim suresi; cekme kurali. https://kanbanguides.org/the-kanban-guide/2025.5/
- Scrum DoD; OKR (hedef + 3-5 KR, 0-1.0; 0.7 basari) vs KPI (haftalik scorecard). 

## 3. Roller (girdi / cikti / tek basina vs eskale)
- Operasyon/planlama (MRP): girdiler ana uretim programi, BOM, stok durumu, tedarik sureleri; cikti planli siparisler/is emirleri. https://www.ifm.eng.cam.ac.uk/research/dstools/mrp/
- Kalite: ISO 9001:2015 10 madde; **ISO 9001:2026 16 Eyl 2026'da yayimlandi** (iklim, kalite kulturu/etik, risk ve firsat ayrimi, degisiklik yonetimi, bilgi paylasimi, kabul kriterleri ayrimi, denetim basina hedef); gecis ~3 yil (UNCONFIRMED). CAPA/8D. https://www.lrqa.com/en-gb/latest-news/iso-9001-publication-date-confirmed/
- Satis: Lead -> Qualified -> Teklif -> Muzakere -> Won/Lost -> Onboarding. Destek: ticket yasam dongusu, SLA (ilk yanit, cozum, yeniden acma). https://www.getmacha.com/glossary/ticket-lifecycle
- Finans: Tekduzen Hesap Plani (1 donen varliklar ... 7 maliyet; 100 Kasa, 120 Alicilar, 150 Ilk madde, 152 Mamuller, 320 Saticilar, 600 Satislar, 620 SMM, 710/720/730). Fiyatlama: cost-plus taban, deger bazli hedef. https://alomaliye.com/2000/12/26/1-seri-no-lu-muhasebe-sistemi-uygulama-genel-tebligi/

## 4. Kalite ve guvenilirlik sistemleri
- Operasyon DoD = is emri basina cikis kontrol listesi (olcu/gorsel/fonksiyon/paket/etiket/kayit); ISO 8.6 serbest birakma kaniti.
- Kontrol grafikleri (Shewhart X-bar/R; Western Electric kurallari). https://itl.nist.gov/div898/handbook/pmc/section3/pmc321.htm
- Suclamasiz postmortem (Google SRE): tetikleyiciler, eylem maddeleri izlenir. https://sre.google/sre-book/postmortem-culture/
- FMEA (AIAG-VDA 2019, 7 adim, Action Priority). https://blog.aiag.org/new-aiag-vda-fmea-handbook-and-trainings-available

## 5. Tedarik zinciri
- Dongu: ihtiyac -> spesifikasyon -> RFQ (>=3 teklif) -> secim -> PO -> teyit -> takip -> teslim alma/muayene -> 3 yonlu eslestirme -> odeme -> performans. https://qntrl.com/blog/procurement-life-cyle.html
- Tedarikci niteleme (belgeler, numune, onayli liste, periyodik degerlendirme); Incoterms 2020 (FCA vs DAP/DDP); ROP = gunluk talep x teslim suresi + emniyet stogu; emniyet = Z x sigma x sqrt(LT); EOQ = sqrt(2DS/H); tedarikci puan karti (zamaninda teslim, kalite PPM, fiyat sapmasi). https://ecosire.com/tr/blog/eoq-safety-stock-reorder-point-guide

## 6. Finans
- Sabit/degisken, katki marji, basabas; 13 haftalik dogrudan nakit akisi tahmini. https://www.numeric.io/template/13-week-cash-flow-template
- Turkiye e-fatura/e-arsiv (2026-10-06 kontrol): VUK 509/535/589; e-fatura brut satis >= 3.000.000 TL (onceki yil) -> 1 Temmuz; e-ticaret/gayrimenkul 500.000 TL; e-arsiv 1 Oca 2026'dan itibaren tutar esigi yok (basit usul/isletme hesabi 3.000 TL altina 31 Ara 2026'ya kadar kagit); 1 Oca 2027 herkes icin sifir esik; e-defter bilanco esasi; DBS digerleri. Ceza 17.000 TL (UNCONFIRMED). https://www.parasut.com/blog/e-arsiv-fatura-limitleri
- Sahis isletmesi 2026: KDV aylik; gecici vergi 3 donem %15; yillik gelir vergisi Mart (%15-40); Bag-Kur ~11.791 TL/ay (UNCONFIRMED); genc girisimci istisnasi 400.000 TL; SMMM fiilen zorunlu. https://www.parasut.com/blog/gecici-vergi

## 7. YZ ajanlarinin operasyonda kullanimi (2025-2026)
- McKinsey State of AI 2026: %88 en az bir fonksiyonda; ajanlar buyuk firmalarin %40'inda, kucuklerde %22; yuksek performanslilar is akisini yeniden tasarlar. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- Gartner: ajanik projelerin >%40'i 2027'ye kadar iptal. Anthropic Economic Index: API kullaniminin ~%77'si otomasyon; Claude Code'da otonomi daha yuksek. https://www.anthropic.com/research/economic-index-june-2026-report
- Karar basina otonomi (INFORM): Otomatiklestir / Onayla / Insan karar. https://www.inform-software.com/en/blog/artificial-intelligence/ai-agents-in-practice-how-much-autonomy-makes-sense
- Tek kisilik sirket + ajan kadro: kurucunun dikkati darbogaz olur; iliskiler devredilemez. https://aibusiness.vc/solo/one-person-company-ai-agents-limits-2026
- OWASP Agentic Top 10 (2026): hedef kacirma, arac kotuye kullanimi, kimlik/yetki, tedarik zinciri (MCP), beklenmeyen kod, hafiza zehirleme, ajanlar arasi iletisim, zincirleme hata, guven istismari, haydut ajan. https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## 8. Buyume icin orgut tasarimi
- Rol ekleme: is yasi/cevrim suresi 2+ hafta SLE'yi asarsa ve kisit somurulemiyorsa; tek kisi >5-7 koltuk tutuyorsa. Gallup 2026 kontrol araligi medyan 5-6. Tek iplikli sahip; iki pizza; Team Topologies (sahip = akis-hizali; YZ finans/kalite/tedarik = platform). Greiner tek insan + YZ kadro: liderlik krizi = sahip her ciktiyi inceleyemez -> yazili yon (SOP, DoD, KPI) -> sinirli karar haklari -> scorecard/denetim/postmortem. https://www.gallup.com/workplace/700718/span-control-optimal-team-size-managers.aspx

## Sirket katina nasil girer
### (a) Rol katalogu
| Rol | Sahip oldugu | Tek basina karar | Eskalasyon | Ajan/Insan |
|---|---|---|---|---|
| Sahip | vizyon, fiyat/urun, musteri iliskisi, fiziksel uretim | her sey | - | Insan |
| Operasyon/Planlama | haftalik plan, is emirleri, MRP | siralama, is emri acma, SLE ici teslim tarihi | SLE disi soz, kapasite asimi | Ajan |
| Tedarik | onayli tedarikci listesi, RFQ, PO, stok politikasi | ROP tetikli tekrar siparis (onayli, butce ici, limit alti) | yeni tedarikci, limit ustu PO, fiyat sapmasi, ithalat | Ajan (onay esikli) |
| Kalite | DoD, NC, CAPA, FMEA, ic denetim | kayit acma, kok neden taslagi | urun serbest birakma, iade, spesifikasyon degisikligi | Ajan (serbest birakma insan) |
| Satis/CRM | pipeline, teklif taslaklari | standart liste ile teklif taslagi | indirim, ozel sart, sozlesme | Ajan (gonderim insan) |
| Musteri destegi | ticket, SLA | bilgi bankasi sorulari | sikayet, iade, SLA ihlali | Ajan |
| Finans | hesap plani, fatura taslagi, 13 haftalik nakit, butce | hesaplama, taslak, hatirlatma | fatura kesme/gonderme, odeme, vergi beyani | Ajan (odeme/beyan insan) |
| IK/Rol yonetimi | rol tanimlari, SOP sahipligi | dokuman bakimi | yeni insan, rol acma/kapatma | Ajan |
| Surekli iyilestirme | postmortem, kaizen, SOP revizyonu | oneri | yururluk | Ajan (onay insan) |

### (b) SOP sablon alanlari
ID, baslik, surum/tarih, sahip (A), R/C/I, amac, kapsam, tanimlar, on kosullar, guvenlik, adimlar (kim ajan/insan, arac, beklenen cikti), karar noktalari (kosul -> yol; tek basina/eskale), durma noktalari ve kontrol listesi (DO-CONFIRM/READ-DO), kayitlar, DoD, KPI, istisnalar/eskalasyon, referanslar, revizyon gecmisi, gozden gecirme tarihi (<=12 ay).

### (c) Operasyon gorev karti ek alanlari
tur (is emri/PO/NC/CAPA/ticket/fatura), musteri/siparis ref, urun + BOM ref, miktar, malzeme hazir mi, tedarikci + PO + teslim, sahibin fiziksel saati, maliyet (tahmin/gercek), fiyat/marj kontrolu, kalite kriterleri, risk (FMEA), karar yetkisi (alone/approval/human), is yasi.

### (d) Ritim
Gunluk (ajan): gelen kutusu triage, SLA, ROP, nakit, bugunun fiziksel is listesi. Gunluk huddle 5-10 dk. Haftalik L10 60-90 dk (ajan scorecard ve Issues'u hazirlar). Haftalik finans (13 hafta). Aylik: butce vs gercek, tedarikci puan karti, NC/CAPA trendi, beyan paketi, SOP gozden gecirme. Ceyreklik: Rocks, OKR, ic denetim, FMEA, gecici vergi. Yillik: strateji, gelir vergisi, esik kontrolu.

### (e) KPI baslangic seti
Teslimat: zamaninda %, cevrim suresi, WIP, geciken. Kalite: ilk seferde dogru %, NC/hafta, sikayet, acik CAPA yasi. Tedarik: tedarikci zamaninda %, stok-out, ROP alti kalem, stok gunu. Satis: pipeline, teklif->siparis %, ortalama siparis. Finans: nakit (13 hafta min), katki marji %, DSO, kesilmemis fatura, butce sapmasi. Sahip: planlanan vs gerceklesen fiziksel saat, darbogaz kullanim %.

### (f) Ajanin asla tek basina karar vermedigi alanlar
1 para cikisi; 2 fiyat ve ticari sartlar; 3 yasal/vergisel (fatura gonderimi, beyan, sozlesme imzasi); 4 urun serbest birakma, iade, tazminat; 5 spesifikasyon/BOM/SOP yururlugu; 6 insanlar (ise alma, muzakere); 7 guvenlik/sorumluluk (fiziksel riskli talimat, kisisel veri, erisim); 8 belirsizlik (SOP'ta karsiligi yok, celiski, guven esigi alti); 9 OWASP tetikleyicileri (dis kaynaktan talimat benzeri icerik, yeni arac, hedef degisikligi). Varsayilan: her sey "onay" seviyesinde baslar; 4-8 hafta sifir hata -> "otomatik".
