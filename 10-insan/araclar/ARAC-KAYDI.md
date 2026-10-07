---
id: 20261006-2251-arac-kaydi
ad: arac-kaydi
tur: referans
kat: 1
surum: 0.8
durum: aktif
amac: Sistemin dunyaya dijital dokunma yollarini (yetenek, arac/API, olgunluk, insan noktasi, yedek yol) ve kurulu MCP/CLI araclarini tek kayitta tutar; kayitsiz arac kullanilmaz.
olusturma: 2026-10-06
guncelleme: 2026-10-07
yazar: claude
talimat: T-000
dayandigi: [00-sistem/arastirma/05-eller-ve-alan-paketi-3d.md, 00-sistem/arastirma/04-guvenilirlik-ve-kalite-teknikleri.md, 00-sistem/arastirma/09-github-taramasi.md, 00-sistem/arastirma/10-yenilikci-teknolojiler.md]
besledigi: []
kaynaklar: ["https://claude.com/docs/connectors/overview", "https://github.com/stripe/agent-toolkit", "https://apidocs.parasut.com/", "https://code.claude.com/docs/en/routines"]
alindi: 2026-10-06
guven: orta
etiketler: [arac]
---

# Araç kaydı — eller yetenek matrisi

Yeni araç eklemek bir karardır (IMZA A10 dış erişim verenler için; diğerleri B7). Tercih sırası: yerel CLI > uzak MCP > tarayıcı otomasyonu. Her satır tarihli; 90 günde yeniden kontrol.

## Amaç
Sistemin dünyaya dijital dokunma yollarını (yetenek, araç/API, olgunluk, insan noktası, yedek yol) ve kurulu MCP/CLI araçlarını tek kayıtta tutar; kayıtsız araç kullanılmaz.

## İçerik
### A. Yetenek matrisi (araştırma 05, 2026-10-06)
| Yetenek | Araç / API | Olgunluk | İnsan noktası | Yedek yol |
| --- | --- | --- | --- | --- |
| Kod ve sandbox | Claude Code shell; API code-execution (Python 3.11, internet yok) | Yüksek | yok | — |
| Belge üretimi (docx/xlsx/pdf) | python-docx, openpyxl, reportlab; Claude Code skills | Yüksek | imza, hukuki onay | LibreOffice headless |
| Tarayıcı otomasyonu | Playwright MCP; Claude in Chrome (GA 2026) | Orta-Yüksek | satın alma/yayınlama/PII tıkı, 2FA, CAPTCHA | elle |
| API / MCP entegrasyonu | REST betikleri; uzak MCP; konektör dizini | Yüksek | OAuth onayı, anahtar | CLI |
| E-posta / takvim / mesaj | Gmail, Google Calendar, Slack konektörleri | Yüksek okuma / Orta gönderim | ilk müşteri yanıtı, ihtilaf (A6) | taslak → insan gönderir |
| Ödeme | Stripe MCP (kısıtlı anahtar); ACP/AP2/MPP protokolleri; TR: iyzico/PayTR UNCONFIRMED | Orta | ödeme yetkisi, limit üstü iade (A6) | ödeme linki hazırla, insan onaylar |
| E-ticaret | Shopify /api/mcp, UCP; Etsy API | Orta-Yüksek | fiyat ve liste onayı (A9) | — |
| Tedarik | Amazon Business PunchOut; Alibaba Accio (UI) | Düşük-Orta | ödeme, tedarikçi şartları | sepet hazırla, insan öder |
| Muhasebe / fatura | Paraşüt API v4 (e-fatura, e-arşiv, stok); Odoo MCP | Orta | e-imza/mali mühür, SMMM, beyan (A6) | taslak fatura |
| Stok | SimplyPrint / Printago / Odoo / kendi SQLite | Orta | fiziksel sayım, teslim alma | CSV defteri |
| Zamanlama | Bulut Rutinler (1 saat, onay yok); Masaüstü zamanlı görev (1 dk, yerel); GitHub Actions; calistir.sh | Yüksek | hazırla→onayla→uygula bölünmesi | /loop |
| IoT | Home Assistant MCP Server; MQTT | Orta | cihaz yerleşimi, güç, güvenlik | — |
| CAD üretimi | OpenSCAD CLI; build123d-mcp; agentcad; FreeCADCmd | Orta-Yüksek | tasarım kabulü | — |
| YZ 3D üretimi | Meshy/Tripo API; TRELLIS.2; Hunyuan3D | Düşük-Orta (fonksiyonel parça) | estetik/uyum onayı | kod-CAD |
| Mesh kontrol/onarım | trimesh, pymeshlab | Yüksek | yok | — |
| Dilimleme | OrcaSlicer / PrusaSlicer CLI | Yüksek | yeni malzeme profili onayı | — |
| Yazıcı kontrolü | Moonraker, OctoPrint REST; mcp-3D-printer-server | Yüksek | yatak boş, filament yüklü (fiziksel) | — |
| Yazıcı (Bambu) | Developer Mode MQTT / Bambu Connect / Printago | Orta | firmware/mod kararı | — |
| Hata tespiti (baskı) | Obico (self-host), yerleşik | Orta-Yüksek | fiziksel müdahale | — |
| Kargo | Shippo/EasyPost; TR kargo API'leri UNCONFIRMED | Orta/Düşük | paketleme, teslim | tarayıcı otomasyonu |
| Vergi / mevzuat | GİB e-arşiv (Paraşüt), ETBİS, mesafeli satış metinleri | Orta | kayıt, imza, SMMM | — |
| Ses → not | Claude Code /voice (kısa; Türkçe); yerel whisper.cpp/faster-whisper + BuzzASR/turkish (uzun) | Orta | — | Deepgram Nova-3 tr |

### B. Kurulu araçlar (bu klasörde)
| Araç | Tür | Kapsam | Eklenme | Karar |
| --- | --- | --- | --- | --- |
| python3 | CLI | hook'lar, betikler | 2026-10-06 | T-000 |
| git | CLI | kayıt, geri alma | 2026-10-06 | T-000 |
| graphifyy 0.9.77 (sabit; `.venv/`) | Python kütüphanesi | `00-sistem/scripts/graf.py`: Leiden topluluk, merkez düğüm, sınır aşan bağ, vis.js HTML. LLM yok, ağ yok (kaynak incelendi, sha256 eşleşti). `graphify install`, git hook'ları ve `--mode deep` YASAK. graf.html açılınca vis-network'ü unpkg.com'dan indirir | 2026-10-06 | T-009 |
| Bash sandbox (bubblewrap + socat) | Claude Code yerleşik | Bash komutları; kimlik bilgisi klasörleri okunamaz, ağ izin listesi boş | 2026-10-06 | T-008, KP-001 |
| qmd 2.8.3 (sabit; `.araclar/qmd`, dizin ve modeller `.araclar/onbellek`; .araclar toplam 3.6 GB, ölçüldü 2026-10-07) | Yerel CLI (node-llama-cpp) | `00-sistem/scripts/ara.py`: wiki'de anlamsal arama (Qwen3-Embedding-0.6B); 01-gelen ve günlükler dizin dışı. Ağ yalnız ilk model indirmede (HuggingFace). MCP eklenmedi. Ölçüm: [[40-ic-ses/arastirma-notlari/qmd-turkce-isabet]] | 2026-10-07 | T-010 |
| markitdown 0.1.8 (`.venv/`) | Python kütüphanesi | `00-sistem/scripts/al.py`: PDF/DOCX/PPTX/XLSX/HTML/URL → 01-gelen ham not. Türkçe metin PDF'inde karakter ve tablo kaybı yok (T-012). Eklentiler ve LLM görsel açıklaması kapalı. **onnxruntime telemetrisi**: `ORT_DISABLE_TELEMETRY=1` zorunlu (al.py ve settings.json env); kapatılmazsa `~/.cache/Microsoft/DeveloperTools/.onnxruntime/` altına cihaz kimliği ve olay kuyruğu yazar | 2026-10-07 | T-012 |
| docling | — | KURULMADI: metin PDF'inde markitdown yeterli; taranmış (görüntü) PDF gelirse OCR için ayrı karar (araştırma 10 önerisinden kanıtla sapma) | 2026-10-07 | T-012 |
| Obsidian Web Clipper (tarayıcı eklentisi) | İnsan noktası | Sahibi kurar: kasa = bu klasör; şablon `00-sistem/sablonlar/web-clipper-gelen.json` içe aktarılır; not 01-gelen'e düşer. İlk kırpıntıdan sonra `kontrol.py --kisa` (şablon gerçek eklentide sınanmadı: UNCONFIRMED) | 2026-10-07 | T-012 |
| Syncthing-Fork (Android) | İnsan noktası | Sahibi kurar: telefondaki not klasörü → `01-gelen/mobil/` (tek yönlü gönderim önerilir) | 2026-10-07 | T-012 |
| lychee 0.24.2 (`.araclar/lychee`, sha256 doğrulandı) | Yerel CLI (Rust) | `00-sistem/scripts/canli.py`: wiki'deki http(s) bağlantıların canlılığı; yalnız 404/410 ölü, 403/429/5xx/ağ belirsiz; 01-gelen denetlenmez. Ağ ister (sandbox'ta alan adı onayı; /haftalik'te sahibi `!` ile) | 2026-10-07 | T-013 |
| ccusage 20.0.26 (`.araclar/ccusage`) | Yerel CLI (node) | `00-sistem/scripts/maliyet.py`: MALIYET.csv ↔ Claude Code oturum kayıtları; `--offline` (ağ yok). Sınır: çevrimdışı fiyat tablosunda olmayan model (claude-sonnet-5-5) 0 USD sayılır, "fiyatsız" işaretlenir | 2026-10-07 | T-013 |
| Snyk agent-scan | — | KURULMADI: skill içeriği, MCP ayarı ve araç açıklamalarını Snyk API'sine gönderir, hesap ve SNYK_TOKEN ister, çevrimdışı kipi yok (resmi README, 2026-10-07). Araştırma 10'daki "yerel" bilgisi yanlıştı. Karar sahibinin (A6/A10) | 2026-10-07 | T-013 |
| Claude Code /voice (dikte) | Yerleşik | Proje ayarı `language: turkish` (T-015). **Veri dışarı:** ses transkripsiyon için Anthropic sunucularına gider, yerelde işlenmez; claude.ai girişi ister; token tüketmez; 15 sn sessizlik ya da 2 dk sınırı. Etkinleştirme (/voice) sahibinde | 2026-10-07 | T-015 |
| FreyaTTS (commit 146d36c; `.araclar/tts`, CPU PyTorch 2.11; deneme ortamı + Whisper large-v3-turbo; toplam 5.1 GB) | Deneme (bağımlılık değil) | Türkçe TTS ölçümü: günlük cümle WER %7, İngilizce terim %60, işlemcide RTF 2.5–12 → canlı sohbete uygun değil. Ağ yalnız HuggingFace indirme. Kaldırmak: `rm -r .araclar/tts` (sahibi) | 2026-10-07 | T-016 |
| (MCP yok) | — | ilk gerçek işte A10 ile | — | — |

### C. İnsan noktası türleri (kartlarda HP-xxx)
`fiziksel` (kur, tak, paketle), `odeme` (ödeme/iade yetkisi), `imza` (sözleşme, beyan), `oauth` (hesap bağlama), `2fa` (doğrulama kodu), `ilk-musteri-yaniti`, `yayin` (kamuya açık çıktı), `silme` (fiziksel silme), `diger`.

### D. Kurallar
1. Kayıtsız araç kullanılmaz; yeni araç `/karar` ile (dış erişim veriyorsa A10, tek yönlü).
2. Dış içerik yalnız okuyucu ile okunur (Dual-LLM); ölümcül üçlü kuralı.
3. Her satır 90 günde yeniden kontrol (TAZELIK); fiyat/erişilebilirlik değişimi `/degistir`.
4. Gözetimsiz koşuda onay gerektiren araç adımı ASK.md yazar ve durur.

## Bağlar
### Dayandığı
- [[00-sistem/arastirma/05-eller-ve-alan-paketi-3d]] — yetenek matrisi
- [[00-sistem/arastirma/04-guvenilirlik-ve-kalite-teknikleri]] — MCP/CLI tercih sırası, güvenlik
- [[00-sistem/arastirma/09-github-taramasi]] — benimsenecek araçlar
- [[00-sistem/arastirma/10-yenilikci-teknolojiler]] — Ekim 2026 yenilikçi araç taraması; öncelikli 10 öneri buradan kayda aday
### Beslediği
### Gelen
- ← [[10-insan/MOC-insan]] — araç kaydı

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-06 | T-000 | Oluşturuldu |
| 0.2 | 2026-10-06 | T-007 | dayandigi += 00-sistem/arastirma/10-yenilikci-teknolojiler.md |
| 0.3 | 2026-10-06 | T-009 | B tablosuna graphifyy (graf.py) ve Bash sandbox satırları |
| 0.4 | 2026-10-07 | T-010 | B tablosuna qmd (ara.py) |
| 0.5 | 2026-10-07 | T-012 | B tablosuna markitdown (telemetri kapalı), docling kararı, Web Clipper ve Syncthing insan noktaları |
| 0.6 | 2026-10-07 | T-013 | B tablosuna lychee, ccusage; agent-scan kurulmadı (veri dışarı gider) |
| 0.7 | 2026-10-07 | T-015 | B tablosuna /voice (Türkçe; ses Anthropic'e gider) |
| 0.8 | 2026-10-07 | T-016 | B tablosuna FreyaTTS deneme ortamı |
