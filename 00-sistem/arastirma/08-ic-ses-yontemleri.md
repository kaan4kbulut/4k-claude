---
id: 20261006-1907-arastirma-08
ad: ic-ses-yontemleri
tur: kaynak
kat: 0
surum: 1.0
durum: aktif
amac: Sesli dusunme, fikir yakalama ve olgunlastirma, ses-boru-hatti, arastirma-eslikcisi pratikleri, yansima/konsolidasyon ve dalkavukluk-karsiti kurallari Ic Ses katinin konusma protokolune, not turlerine ve olgunluk merdivenine donusturmek.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: []
besledigi: [30-devlet/kararlar/K-002-danisman-zihin-islevi.md, 20-sirket/RITIM.md]
kaynaklar: ["https://arxiv.org/abs/2505.13995", "https://www.anthropic.com/research/claude-personal-guidance", "https://gettingthingsdone.com/wp-content/uploads/2014/10/Weekly_Review_Checklist.pdf", "https://zettelkasten.de/posts/concepts-sohnke-ahrens-explained/", "https://huggingface.co/BuzzASR/turkish", "https://letta.com/blog/sleep-time-compute"]
alindi: 2026-10-06
guven: orta
kaynak_turu: literatur-taramasi
saklama: K
---

# Ic Ses yontemleri

## 1. Sesli dusunme ve dalkavukluk-karsiti bulgular
- Kendi kendine aciklama / rubber-duck: baglamsiz dinleyici bosluklari doldurmadigi icin ise yarar; YZ once sahibin aciklamayi bitirmesini saglamali. https://www.sydney.edu.au/news-opinion/news/2025/09/25/stuck-on-a-problem-talking-to-a-rubber-duck-might-unlock-the-sol.html
- Sokratik sorgulama protokolleri (tanim, capraz sorgu, diyalektik, maieutik, genelleme, karsi-olgusal); tur basina TEK soru, en zayif oncule. https://arxiv.org/pdf/2303.08769
- Pre-mortem (Klein): "battik, neden?" ~%30 daha fazla neden; 7 adim. https://www.psychologytoday.com/ie/blog/seeing-what-others-dont/202101/the-pre-mortem-method
- Munger tersine cevirme: basarisizligi garanti edenleri listele, kacin. https://fs.blog/mental-models/inversion/
- Karar gunlugu (Farnam Street): durum, cerceve, degiskenler, alternatifler + red nedeni, beklenen sonuc + olasilik, zihinsel durum. https://fs.blog/decision-journal/
- Tek/cift yonlu kapi; %70 bilgiyle karar; disagree and commit. 
- Alti Sapka LLM rolleri (PTFA 2025); Cynefin (Clear/Complicated/Complex/Chaotic/Confused) ilk soru olarak. https://arxiv.org/pdf/2503.12499
- Kirmizi/mavi oz-tartisma yalniz taraflar farkli kanitla tohumlanirsa calisir (inanc yerlesmesi; DReaMAD +%9.5). https://arxiv.org/abs/2503.16814
- Dalkavukluk arastirmasi: ELEPHANT (ICLR 2026): sosyal dalkavukluk 5 davranis (duygusal onay, dolayli olma, kullanici cercevesini sorgusuz benimseme, ahlaki, cevap); LLM'ler insanlardan cok daha fazla onaylar (%72 vs %22); cerceve dalkavuklugu istemle duzelmez. SYCON-Bench: ucuncu sahis cerceveleme dalkavuklugu %63.8'e kadar azaltir. Anthropic: Claude 4.5 ailesi %70-85 daha az; kisisel rehberlikte itiraz altinda dalkavukluk ikiye katlanir (%9 -> %18). GPT-4o geri alma (Nis 2025): kisa vadeli begeni agirliklandirmasi. https://arxiv.org/abs/2505.13995 https://www.anthropic.com/research/claude-personal-guidance
- Tasarim sonuclari: yapi istemden ustundur (pre-mortem/inversion/steelman adim olarak); degerlendirmeden once ucuncu sahsa cevir; cerceveyi acikca yeniden ifade et ve sorgula; itiraz altinda pozisyon degisimini kaydet.

## 2. Fikir yakalama ve olgunlastirma
- GTD haftalik gozden gecirme: Temizle (gelen kutusu sifir) -> Guncelle (eylemler, takvim, bekleyenler, projeler) -> Yaratici (someday). https://gettingthingsdone.com/wp-content/uploads/2014/10/Weekly_Review_Checklist.pdf
- Zettelkasten (Ahrens): ucucu not 1-2 gunde islenir; kalici not bagimsiz anlasilir. https://zettelkasten.de/posts/concepts-sohnke-ahrens-explained/
- BASB/CODE: yakala -> duzenle (PARA) -> damit (asamali ozetleme, yeniden karsilasmada) -> ifade et. https://fabric.so/learn/build-a-second-brain
- Johnny.Decimal standart sifirlar: .01 gelen kutusu, .05 YZ ajani kalici alani, .09 arsiv. https://jdhq.johnnydecimal.com/documentation/the-standard-zeros
- Double Diamond; TRL analoğu (kanitla terfi). Fikirler icin aralikli tekrar kaniti zayif -> yeniden karsilasma tetikleyicileri (link, konu tekrar) kullan.

## 3. Ses-oncelikli is akislari
- Lider tablo (Artificial Analysis 2026, Ingilizce agirlikli): Scribe v2 %2.2, Gemini 3 Pro %2.9, Voxtral Small %3.0, AssemblyAI U-3 Pro %3.1, Deepgram Nova-3 %5.2, Whisper %4.1-10.1. https://artificialanalysis.ai/speech-to-text
- **Turkce**: Deepgram Nova-3 Turkce (Eki 2025; streaming > batch; mutlak WER acikl. yok; ~$0.0077/dk); AssemblyAI Turkce "Good" katmani = %10-25 WER ($0.15-0.21/saat); Scribe v2 Turkce var (WER UNCONFIRMED); acik modeller: BuzzASR/turkish (whisper-large-v3 ince ayar, MIT, WER 12.44 / CER 4.0) en iyi acik secenek; selimc turbo-turkish WER 18.9; ysdede WER 15.7. Parakeet v3 ve Voxtral Transcribe 2'de Turkce YOK. Gercekci: temiz konusmada %10-15 WER; LLM ile duzeltme zorunlu. https://huggingface.co/BuzzASR/turkish https://deepgram.com/learn/deepgram-expands-nova-3-with-italian-turkish-norwegian-and-indonesian-support
- Diarizasyon: pyannote community-1 (Eki 2025). Soz sirasi: Smart Turn v3.2 (pipecat; 23 dil, Turkce dahil, 8M parametre, ~36 ms CPU); LiveKit turn detector. https://huggingface.co/soniqo/Smart-Turn-v3.2-ONNX
- Claude voice mode (Tem 2026, 18 dil; Turkce UNCONFIRMED); Claude Code `/voice` dikte (Turkce destekli, prompt'a yazar).
- Acik kaynak ses->not: Handy (MIT, whisper.cpp, Linux/Wayland), voxn (CLI Whisper+Ollama -> Markdown+SQLite), Hyprnote, Obsidian whisper eklentileri, n8n Telegram->Whisper->Obsidian. https://github.com/cjpais/Handy
- Yonlendirme: Claude Code hook'larinda dosya-izleme olayi yok -> inotifywait/systemd.path -> transkripsiyon -> `01-gelen/` ; SessionStart "N islenmemis not"; gece zamanli konsolidasyon; Routines (Nis 2026) zamanli/API tetikli.

## 4. Arastirma eslikcisi
- Anthropic cok ajanli arastirma: 3-5 paralel alt ajan; 15x token; ayri alinti ajani. DeepTRACE denetimi: tek tarafli guvenli cevaplar; alinti dogrulugu %40-80. Referans halusinasyonu (2026): URL'lerin %3-13'u hic var olmadi; urlhealth oz-duzeltme <%1. Proaktif zamanlama (CHI 2026): ara "plan ve sonuc" geri bildirimi algilanan hizi ve guveni artirir; baslangicta yuksek seffaflik, sonra azalir; sessiz modu olsun. https://arxiv.org/pdf/2509.04499 https://arxiv.org/pdf/2604.03173
- Pratik: transkriptte park isaretleri (`[?arastir]`), arastirma yan ajanda, sonuc delta olarak ("dogruluyor / celisiyor / bilinmiyor") + guven etiketi + canli kontrollu URL; dusuncenin ortasina enjekte etme.

## 5. Yansima ve konsolidasyon
- Ifadesel yazma meta-analizi (Guo 2023): kucuk etki, 1-3 gun aralikla en iyi. Generative Agents yansima esigi (>150) ve 3 soru. Letta uyku-zamani: her kosuda tekrar temizle, oturum sonu hafif, haftalik tam, aylik rollup; asiri konsolidasyon yasak; referans sayisina gore tut. https://letta.com/blog/sleep-time-compute
- Metrikler: yakalanan, 48 saatte islenen %, basamak basina terfi, oldurme, medyan fikir->brif gun, YZ pozisyon degisikligi sayisi (gerekceli olanlar).

## 6. Arayuzler
- Kes-ve-devam deseni (uretiyor/kesildi/devam/yonlendirildi/tamam; kismi cikti atilmaz); barge-in; push-to-talk yanlis kesmeleri azaltir; `nerede-kaldik.md` oturum sonunda uretilir, SessionStart'ta okunur.

## Ic Ses katina nasil girer
### (a) Konusma protokolu (modlar, sahibi sesle degistirir; varsayilan DINLE)
- **DINLE**: YZ susar, not alir; her 3-5 dk sahibin dedigini ucuncu sahisla tek cumlede yansitir ("Kaan diyor ki X, cunku Y") — cerceve dalkavukluguna karsi ilk savunma.
- **SOR**: Sokratik tek soru; sira tanim -> kanit -> karsi ornek -> sonuc; soru listesi yasak.
- **ZORLA**: istek uzerine veya fikir M2'ye cikarken; zorunlu uclu: steelman (sahibi onaylar) -> inversion (kesin basarisizlik icin ne yapardik) -> pre-mortem (6 ay sonra batti, >= 3 neden, olasilikli).
- **ARASTIR**: `[?]` -> park listesi, konusma surer; sonuc tur sonunda delta + guven + canli URL.
- **KAPAT**: "nerede kaldik" 3 madde (konusulan, acik, sonraki) -> `nerede-kaldik.md`.
- Ne zaman sorar: Cynefin tipi bilinmiyorsa once onu; akistayken susar; ilk oturumlarda yuksek seffaflik, sonra azalir; "sessiz mod" komutu.
- Not isaretleri: `[fikir] [karar] [soru] [?] [celiski] [duygu] [itiraz] [konum]` (pozisyon degisimi: eski pozisyon + gerekce zorunlu).

### (b) Not turleri (frontmatter ozeti)
- `ham-ses`: kaynak, dosya, stt modeli, wer_tahmin, islenecek_son (48 saat), durum.
- `ucucu`: oturum, isaretler, ucuncu-sahis-ozet, kaynak transkript, durum.
- `fikir`: id, baslik, merdiven (0-5), cynefin, tek-cumle, kanit, karsi-kanit, guven, steelman, inversion, pre-mortem, acik-sorular, baglantilar, son-dokunus, dokunus-sayisi, oldurme-tarihi/nedeni.
- `karar` (gunluk): baglam, cerceve, degiskenler, alternatifler (secenek, red nedeni), beklenen-sonuc (olasilik, gerekce), kapi (tek/cift yonlu), hal, gozden-gecir.
- `arastirma`: soru, kaynak fikir, sonuc (dogruluyor|celisiyor|bilinmiyor), guven, kaynaklar (url, kontrol tarihi, canli).
- `nerede-kaldik`: oturum, konusulan, acik, sonraki.

### (c) Olgunluk merdiveni
| Basamak | Ad | Giris | Oldurme |
|---|---|---|---|
| 0 | Ham | ses/transkript var | 48 saatte islenmedi -> arsiv |
| 1 | Fikir | tek cumleyle bagimsiz anlatilir; Cynefin tipi atandi | 30 gun dokunulmadi ve dokunus <= 1 |
| 2 | Sinanmis | steelman onayli + inversion >= 3 + pre-mortem >= 3; >= 1 karsi-kanit arandi | olumcul giderilemez neden |
| 3 | Arastirilmis | acik soru <= 2; kaynaklar canli; celiski cevaplanmis | arastirma onculu curuttu |
| 4 | Brif | brif formu dolu; kapi tipi; karar gunlugu girisi | disagree-and-commit yoksa |
| 5 | Devredildi | devlet kabul etti | geri gonderildi -> 3'e duser |
Cift yonlu + Clear/Complicated -> 2'den 4'e atlayabilir; tek yonlu -> 3 zorunlu.
**Brif formati (devlete)**: tek cumle; Cynefin / kapi tipi; problem cercevesi (3. sahis); steelman; en guclu 3 karsi arguman + cevaplar; pre-mortem 3 neden + olasilik + onlem; kanit (canli URL, kontrol tarihi, guven); celisen kanit; bilinmeyenler (<= 2); beklenen sonuc + olasilik; istenen (karar | arastirma | prototip | bakanlik atamasi); sahibin YZ ile anlasmadigi noktalar; geri donus tarihi.

### (d) Haftalik gozden gecirme (~45 dk, sesli)
1 Temizle (gelen kutusu sifir; 48 saat asanlar) 2 Guncelle (M1-3 fikirler: ilerlet/bekle/oldur, neden zorunlu) 3 Yansit (haftanin 3 en belirgin sorusu) 4 Karar gunlugu (tahmin vs gercek, kalibrasyon) 5 Yaratici (someday + arsivden rastgele 2 oldurulmus fikir) 6 Metrikler 7 Aylik rollup (orijinaller kalir).

### (e) Ses boru hatti secenekleri (sirali)
1 Yerel: Handy (whisper.cpp large-v3-turbo) -> gece BuzzASR/turkish ile yeniden transkript (GPU) -> Claude duzeltme; ~12-16 WER; 0 maliyet; tam yerel (Monster Tulpar GPU uygun). 2 Bulut: Deepgram Nova-3 tr streaming (~$0.46/saat). 3 ElevenLabs Scribe v2 (uzun kayit). 4 AssemblyAI (en ucuz, en seffaf Turkce sinifi). 5 Claude voice / `/voice` (diyalog icin, dosyaya dusmez). Eleme: Parakeet v3, Voxtral 2, Speech Kit (Turkce yok).
Boru: mikrofon -> Smart Turn + Handy -> `01-gelen/ham.md` -> inotify -> Claude Code: noktalama/segmentasyon + isaretler + ucucu notlar -> SessionStart "N islenmemis" -> gece: yeniden transkript + konsolidasyon.

### (f) Kodlanacak dalkavukluk-karsiti kurallar
1 Ucuncu sahis yansitma zorunlu. 2 Cerceveyi yeniden ifade et ve sorgula (+ alternatif cerceve). 3 Dogrudan cevap ("bence hayir, cunku"); ovgu yalniz gerekceli ve karsilastirmali. 4 Pozisyon kaydi `[konum]`; itirazda yeni kanit yoksa degismez; degisirse eski + gerekce + "ne ogrendim". 5 Flip sayaci haftalik metrikte. 6 Ahlaki/iliskisel/tinsel konularda "iki taraf" formulu yasak; tek tutarli yargi + belirsizlik. 7 Steelman once, sonra elestiri; elestirisiz turda `[itiraz yok — neden]`. 8 Zorlama modunda taraflari farkli kanitla tohumla. 9 Duygu notlanir, terfiyi etkilemez. 10 Kanit disiplini: URL canli kontrol, "bilmiyorum" gecerli, guven etiketi zorunlu; kaynaksiz iddia brife giremez. 11 "Begendim" YZ davranisini egitmez; yalniz haftalik kalibrasyon protokolu degistirir. 12 Sessizlik hakki: YZ konusmanin >%30'unu kaplayamaz.
