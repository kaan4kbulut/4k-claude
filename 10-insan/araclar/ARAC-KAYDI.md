---
id: 20261006-2251-arac-kaydi
ad: arac-kaydi
tur: referans
kat: 1
surum: 0.1
durum: aktif
amac: Sistemin dunyaya dijital dokunma yollarini (yetenek, arac/API, olgunluk, insan noktasi, yedek yol) ve kurulu MCP/CLI araclarini tek kayitta tutar; kayitsiz arac kullanilmaz.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: [00-sistem/arastirma/05-eller-ve-alan-paketi-3d.md, 00-sistem/arastirma/04-guvenilirlik-ve-kalite-teknikleri.md, 00-sistem/arastirma/09-github-taramasi.md]
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
### Beslediği
### Gelen
- ← [[10-insan/MOC-insan]] — araç kaydı

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 0.1 | 2026-10-06 | T-000 | Oluşturuldu |
