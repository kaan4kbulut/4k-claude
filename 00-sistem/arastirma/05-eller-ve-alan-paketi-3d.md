---
id: 20261006-1904-arastirma-05
ad: eller-ve-alan-paketi-3d
tur: kaynak
kat: 0
surum: 1.0
durum: aktif
amac: Bir ajanin dunyaya dijital olarak dokunma yollarini (eller yetenek matrisi) ve bir alanin sisteme nasil ogretilecegini gosteren Alan Paketi sablonunu, 3D baski mikro-fabrikasi test alani uzerinden belirlemek.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-000
dayandigi: []
besledigi: [10-insan/araclar/ARAC-KAYDI.md, 20-sirket/alan-paketleri/3d-uretim.md]
kaynaklar: ["https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool", "https://github.com/stripe/agent-toolkit", "https://apidocs.parasut.com/", "https://www.orcaslicer.com/wiki/cli/cli_mode", "https://moonraker.readthedocs.io/", "https://wiki.bambulab.com/en/software/third-party-integration", "https://makers101.com/commercial-license-to-sell-3d-prints/"]
alindi: 2026-10-06
guven: orta
kaynak_turu: literatur-ve-urun-taramasi
saklama: K
---

# Eller (yurutme) kati ve 3D uretim test alani

## 1. Genel "eller" yetenekleri
| Yetenek | Arac/API | Olgunluk | Insan noktasi |
|---|---|---|---|
| Kod/sandbox | Claude Code shell; API code-execution (Python 3.11, internet yok, 5 GiB) | Yuksek | yok |
| Belge uretimi | python-docx/openpyxl/reportlab, skills | Yuksek | imza, hukuki onay |
| Tarayici otomasyonu | Playwright; Claude in Chrome (GA Agu 2026; satin alma/yayinlama/PII oncesi onay sorar) | Orta-Yuksek | satin alma tiki, 2FA, CAPTCHA |
| API/MCP | REST, uzak MCP, konektor dizini | Yuksek | OAuth onayi, anahtar |
| E-posta/takvim/mesaj | Gmail/GCal/Slack konektorleri | Yuksek okuma / Orta gonderim | ilk musteri yaniti, ihtilaf |
| Odeme | Stripe MCP (kisitli anahtar; payment link, invoice, refund); ACP (OpenAI+Stripe), AP2 (Google), x402, MPP; Visa/Mastercard ajan tokenlari (TR: UNCONFIRMED) | Orta | odeme yetkisi, limit ustu iade |
| E-ticaret | Shopify `/api/mcp`, UCP (Mar 2026), Etsy | Orta-Yuksek | fiyat onayi |
| Tedarik | Amazon Business PunchOut; Alibaba Accio (yalniz UI) | Dusuk-Orta | odeme, tedarikci sartlari |
| Muhasebe | Parasut API v4 (e-fatura, e-arsiv, stok), Odoo MCP | Orta | e-imza/mali muhur, SMMM |
| Stok | SimplyPrint/Printago, Odoo, kendi veritabani | Orta | fiziksel sayim |
| Zamanlama | Bulut Rutinler (1 saat, onay yok), Masaustu zamanli gorev (1 dk, yerel), GitHub Actions | Yuksek | hazirla/onayla/uygula bolunmesi |
| IoT | Home Assistant MCP Server (2025.2), MQTT | Orta | cihaz yerlesimi, guvenlik |
| CAD uretimi | OpenSCAD CLI, build123d-mcp, agentcad, FreeCADCmd | Orta-Yuksek | tasarim kabulu |
| YZ 3D uretimi | Meshy/Tripo API, TRELLIS.2 (MIT), Hunyuan3D | Dusuk-Orta (fonksiyonel) | estetik/uyum onayi |
| Mesh kontrol | trimesh (`is_watertight`, repair), pymeshlab | Yuksek | yok |
| Dilimleme | OrcaSlicer/PrusaSlicer CLI | Yuksek | yeni malzeme profili onayi |
| Yazici kontrolu | Moonraker, OctoPrint REST | Yuksek | yatak bos, filament yuklu |
| Yazici (Bambu) | Developer Mode MQTT / Bambu Connect / Printago | Orta | firmware/mod karari |
| Hata tespiti | Obico (AGPL, self-host), yerlesik | Orta-Yuksek | fiziksel mudahale |
| Kargo | Shippo/EasyPost; TR kargo API'leri UNCONFIRMED | Orta/Dusuk | paketleme |
| Vergi | GIB e-arsiv (Parasut), ETBIS, mesafeli satis | Orta | kayit, imza |

Insan noktasi sozdizimi: `insan_noktasi: {id: HP-PAY-01, tur: odeme_onayi, kosul: tutar > 2000 TL, kanit: payment_link_paid webhook, bekleyen_adim: 6}`.

Kaynaklar: https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool ; https://claude.com/docs/connectors/overview ; https://github.com/stripe/agent-toolkit ; https://crossmint.com/learn/agentic-payments-protocols-compared ; https://ecommercefastlane.com/shopify-mcp-model-context-protocol/ ; https://apidocs.parasut.com/ ; https://code.claude.com/docs/en/routines ; https://home-assistant.io/integrations/mcp_server/

## 2. 3D baski mikro-fabrikasi (dijital taraf)
- **CAD**: OpenSCAD `openscad -o out.stl -D var=val file.scad`; build123d-mcp (olcum, render, STEP/STL; CADGenBench 0.457 geri bildirimle); FreeCADCmd; Blender `-b --python`. YZ 3D: TRELLIS.2 (Ara 2025, MIT, 24 GB VRAM), Hunyuan3D 2.1/3.1, Meshy 7 (API: text-to-3D 20 kredi, printability ucretsiz), Tripo, Rodin; sattilabilir fonksiyonel parcalar icin DUSUK-ORTA. https://pypi.org/project/build123d-mcp/ https://docs.meshy.ai/api/pricing
- **Mesh onarim**: trimesh `is_watertight`, `fix_normals`, `fill_holes`; kontroller: watertight, manifold, min duvar vs nozzle, cikinti %, yatak sigdirma, hacim -> gram. https://trimesh.org/trimesh.repair.html
- **Dilimleme CLI**: PrusaSlicer `--export-gcode --load ... -o`; OrcaSlicer `--slice 1 --load-settings "machine.json;process.json" --load-filaments f.json --export-3mf out.gcode.3mf` (`--arrange`, `--orient`, `--pipe` JSON ilerleme); Docker headless. https://www.orcaslicer.com/wiki/cli/cli_mode
- **Filo kontrolu**: OctoPrint REST (`X-Api-Key`; /api/files, /api/job); Moonraker HTTP+WS JSON-RPC (upload, print/start, job_queue). Bambu: Oca 2025 Authorization Control; Developer Mode (LAN, MQTT acik, bulut yok) veya Bambu Connect. Prusa: PrusaLink yerel REST; Prusa Connect'in acik otomasyon API'si yok. Farm yazilimi: SimplyPrint (API Pro+), Printago (REST, SKU, Etsy/Shopify), 3DPrinterOS, Repetier-Server, FDM Monster (acik kaynak). MCP: DMontgomery40/mcp-3D-printer-server (OctoPrint/Moonraker/Duet/Bambu/Prusa, GPL-2). https://docs.octoprint.org/en/main/api/general.html https://moonraker.readthedocs.io/ https://wiki.bambulab.com/en/software/third-party-integration
- **Fiyatlama**: Fiyat = (malzeme + makine saati + iscilik + genel gider) / (1 - marj); makine $5-10/sa; amortisman; %5-15 hata tamponu; platform komisyonu %5-15. Acik kaynak fiyat araci yok -> dilimleyici ciktisindan (gram, dakika) kendi betigi. https://siraya.tech/blogs/news/how-to-price-3d-prints
- **Lisans**: CC BY/BY-SA/BY-ND satisa izin verir (atifla); NC -> satis yok. MakerWorld standart lisans satisi yasaklar; Commercial License Membership (Sub 2025). Cults3D ticari anlasma gerektirir. Printables CC + no-commercial bayragi. Thingiverse cogu NC. Marka/fan-art ayri risk. Ajan: lisans alanini ayristir, ekran goruntusu + URL + tarih kaydet, NC/bilinmeyeni engelle. https://makers101.com/commercial-license-to-sell-3d-prints/
- **Fiyat referanslari (2026, USD)**: A1 Mini $299, A1 $399, P1S $399-699, X1C ~$1.199, H2D $1.899; PLA 1 kg $9.79-26.99 (medyan $14.72), PETG $20-23, ASA ~$28, PA6-CF ~$40. TL fiyatlari UNCONFIRMED. https://stacksheriff.com/3d-printing/bambu-lab-pricing/
- **Operasyon**: bakim kullanim tetikli (saat, kg, hata); hata tespiti Obico (otomatik duraklatma); QC toleranslari FDM +-0.2-0.5 mm; guvenlik: UFP/VOC havalandirma, recine PPE; Turkiye: esnaf vergi muafiyeti (GVK 9/10; 2026 tavan ~1.9-1.98 M TL UNCONFIRMED; "sinai makine" sorusu UNCONFIRMED), e-arsiv 2026 tum e-ticaret, e-fatura 500.000 TL e-ticaret esigi, ETBIS, mesafeli satis 14 gun cayma (kisiye ozel uretim istisnasi on bildirimle), KDV. https://www.parasut.com/blog/internet-satislarinda-fatura-nasil-kesilir
- **Ucten uca akis (A=ajan, P=ajan hazirlar, H=insan)**: 1 talep (A) -> 2 model temini/lisans (A; H lisans odemesi) -> 3 basilabilirlik (A) -> 4 teklif (A hazirlar, P gonderir; H limit ustu) -> 5 odeme (H musteri; A webhook) -> 6 filoya planla (A; H yatak/filament) -> 7 izle (A; H fiziksel) -> 8 son islem listesi (P; H yapar) -> 9 QC (P liste; H olcer; A karar) -> 10 fatura + kargo etiketi (A; H paketler) -> 11 geri bildirim, bakim sayaci, stok dusumu, yeniden siparis sepeti (A; H oder).

## 3. Alan Paketi sablonu (herhangi bir alani sisteme ogretmek icin)
1. Kimlik: alan adi, surum, sahip, kapsam cumlesi
2. Kavramlar ve sozluk (her biri kanonik belgeye bagli)
3. Roller (sahip + ajan rolleri; hangi piramit katinda)
4. Surecler (A/P/H etiketli adimlar; hata dallari)
5. Araclar ve API'ler (uc nokta/CLI, kimlik dogrulama, olgunluk, surum, yedek yol)
6. Tedarikciler ve pazar yerleri (fiyat bandi + tarih; lisans rejimi; ajanin erisim yolu)
7. Mevzuat ve vergi (tarihli, VERIFIED/UNCONFIRMED, kaynak)
8. Riskler ve guvenlik (azaltma + sahip)
9. Maliyet modeli (BOM, birim maliyet formulu, parametre dosyasi)
10. Insan noktalari katalogu (id, tetik, insan ne yapar, kanit, SLA, eskalasyon)
11. Metrikler (teslim suresi, ilk gecis verimi, hata orani, marj...)
12. Bakim ve operasyon takvimi
13. Veri semasi (siparis, model+lisans kaniti, is, yazici, filament lotu, QC, fatura)
14. Test senaryolari (kuru kosu, NC lisans reddi, limit ustu odeme)
15. Bilinmeyenler / UNCONFIRMED listesi
16. Degisiklik gunlugu (kaynak yeniden kontrol kadansi)

Kalan UNCONFIRMED: TR kargo API'leri; iyzico/PayTR ajan araclari; TL fiyatlar; Cura CLI ayrintisi; FreeCAD headless ayrintisi; masaustu yazicinin esnaf muafiyetine etkisi; Visa/MC ajan odemeleri TR.
