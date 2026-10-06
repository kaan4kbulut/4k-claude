# Talimatlar — istek defteri

Her istek numaralı bir talimattır. Biçim `00-sistem/sablonlar/talimat.md`. Durumlar: `acik`, `bekliyor` (ASK.md var), `kapali`. En yeni en altta. Numara boşluk bırakmadan artar, yeniden kullanılmaz.

---

## T-000 — Yeni Sistem klasörünün ilk kurulumu
- Tarih: 2026-10-06
- Niyet: Şema v2'ye göre tüm sistem dosyalarını (CLAUDE.md, .claude katmanı, 00-sistem omurgası, şablonlar, betikler, kat dosyaları, araştırma raporları) tam içerikle oluşturmak; işleyiş Claude Code'da denenebilir olsun.
- Başarı ölçütü: `python3 00-sistem/scripts/kontrol.py` sıfır hata; HARITA'da tüm frontmatter'lı sayfalar; her sayfa SEMA'ya uygun.
- Sınırlar: Rol (kadro) dosyası yazılmaz; gerçek proje işi yapılmaz; sandbox açılmaz.
- Kat: 0
- Kapı: cift-yonlu (dosyalar geri alınabilir; git ile)
- Durum: kapali
- Doğurduğu dosyalar: tüm klasör (HARITA.md listeler)
- Kapanış notu: Kurulum tamamlandı; kontrol.py sıfır hata. Danışman ve kadro kararları açık (K-002).

## T-001 — Yazıcı işi fikrini kat 4'e not olarak kaydet
- Tarih: 2026-10-06
- Niyet: Deneme 1/4. Sahibinin "yazıcı alıp bir işe başlamak istiyorum" fikrini zihin katına fikir sayfası olarak kaydetmek; altı adımın tamamını işletmek.
- Başarı ölçütü: `40-ic-ses/fikirler/F-0001-yazici-isi-fikri.md` var; merdiven 1; Cynefin tipi atanmış; HARITA ve GUNLUK satırı; kontrol.py sıfır hata.
- Sınırlar: Fikir değerlendirilmez (ZORLA modu çalıştırılmaz); yalnız kayıt.
- Kat: 4
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: 40-ic-ses/fikirler/F-0001-yazici-isi-fikri.md
- Kapanış notu: F-0001 merdiven 1, cynefin kompleks (Claude ataması, sahibi onayı bekliyor) olarak kaydedildi; HARITA, MOC, GUNLUK satırları düştü; kontrol.py 0. Açık: yazıcı türü sorusu; şablon/şema uyumsuzluğu (kapi, son_dokunus) için kök neden talimatı önerildi.

## T-002 — "Önce pazar araştırması yapılacak" kararını kat 3'e kaydet
- Tarih: 2026-10-06
- Niyet: Deneme 2/4. F-0001'e dayanan bir karar kaydı (K-004) açmak; MADR-mini alanları dolu; F-0001 ile iki yönlü bağ.
- Başarı ölçütü: `30-devlet/kararlar/K-004-yazici-pazar-arastirmasi.md` var; durum onerildi; KARARLAR.md satırı; F-0001.besledigi içinde K-004; kontrol.py sıfır hata.
- Sınırlar: Karar sahibi onaylamadan `kabul` olmaz.
- Kat: 3
- Kapı: cift-yonlu
- Durum: acik
- Doğurduğu dosyalar:
- Kapanış notu:

## T-003 — Pazar araştırması görev kartını kat 2'ye aç
- Tarih: 2026-10-06
- Niyet: Deneme 3/4. K-004'e dayanan görev kartı (G-001); 12 alan dolu; insan noktaları beyan edilmiş; kanıt boş olduğu için kanban `bekliyor`.
- Başarı ölçütü: `20-sirket/gorevler/G-001-yazici-pazar-arastirmasi.md` var; K-004.besledigi içinde G-001; kontrol.py sıfır hata; kanıtsız `tamam` denemesi kontrol.py tarafından reddedilir (bunu bilerek dene ve raporla).
- Sınırlar: Araştırma yapılmaz; yalnız kart.
- Kat: 2
- Kapı: cift-yonlu
- Durum: acik
- Doğurduğu dosyalar:
- Kapanış notu:

## T-004 — F-0001'e bir cümle ekle (değiştirme kuralı denemesi)
- Tarih: 2026-10-06
- Niyet: Deneme 4/4. `/degistir` ile F-0001'e bir cümle eklemek; sürüm 0.2; sayfa günlüğünde ve GUNLUK'te satır.
- Başarı ölçütü: F-0001 `surum: 0.2`; günlük tablosunda ikinci satır; GUNLUK `[degisti]`; kontrol.py sıfır hata.
- Sınırlar: Başka alan değişmez.
- Kat: 4
- Kapı: cift-yonlu
- Durum: acik
- Doğurduğu dosyalar:
- Kapanış notu:

## T-005 — Analizde bulunan eksiklerin kök neden düzeltmesi
- Tarih: 2026-10-06
- Niyet: 2026-10-06 analizinde bulunan eksikleri kapatmak: calistir.sh'ta hook'ları kapatan --bare; git deposu yok; durus-kapisi'nin metne dayalı (sahte kanıtla geçilebilen) kontrolü ve İç Ses sohbetiyle çatışması; yikici-koruma'nın yanlış pozitifleri ve açıkları; MALIYET.csv'nin hep 0 yazması; şablon/şema uyumsuzluğu (belirlenmedi enum dışı, tarih alanları); GUNLUK'te elle yazılan zaman damgaları.
- Başarı ölçütü: her düzeltme için çalıştırılmış test (komut + çıkış kodu); kontrol.py sıfır hata; hook'lar örnek girdilerle beklenen kararı veriyor; git'te temel commit (e39a086) ve düzeltme commit'i.
- Sınırlar: Anayasa, imza matrisi ve "altı adım" kuralı değiştirilmez (sahibinin kararı; öneri olarak sunulur). F-0001 içeriğine dokunulmaz (T-004 denemesi için korunur). T-002..T-004 açık kalır.
- Kat: 0
- Kapı: cift-yonlu (git ile geri alınabilir)
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/scripts/gunluk.py (yeni); değişen: calistir.sh, durus-kapisi.py, oturum-basi.py, yikici-koruma.py, kapanis-kaydi.py, settings.json, yscommon.py, kontrol.py, sayfa.schema.json, SEMA.md, MALIYET.csv, CLAUDE.md, rules/00-sistem.md, DEGISIKLIKLER.md
- Kapanış notu: Yedi eksik kök nedenden düzeltildi ve testlerle doğrulandı. Açık kalanlar: hafif yol önerisi (sahibinin kararı); sandbox hâlâ kapalı (bubblewrap + socat kurulumu sahibinde); omitClaudeMd alanı belgelerde doğrulanamadı.

## T-006 — Sistemin adını "Yeni Sistem"den "4k-claude"a değiştir
- Tarih: 2026-10-06
- Niyet: Sahibinin isteğiyle sistemin adı 4k-claude olur. Canlı dosyalardaki ad (kurallar, hook iletileri, şema, README, SISTEM, ANAYASA) ve klasör adı değişir; tarihî kayıtlar (GUNLUK satırları, 00-sistem/arastirma raporları, kapanmış talimat başlıkları) olduğu gibi kalır.
- Başarı ölçütü: canlı dosyalarda "Yeni Sistem" geçmiyor (grep); ANAYASA 1.1 ve sayfa günlüğünde çerçeve ifade; K-003 karar kaydı ve KARARLAR satırı; kontrol.py sıfır hata; klasör ~/Downloads/4k-claude.
- Sınırlar: Anlam değişmez, yalnız ad. Arşiv niteliğindeki metin yeniden yazılmaz. T-002/T-003'ün planladığı karar numarası K-003'ten K-004'e kayar (numara sırası kuralı).
- Kat: 0
- Kapı: cift-yonlu (git ile geri alınabilir)
- Durum: kapali
- Doğurduğu dosyalar: 30-devlet/kararlar/K-003-ad-degisikligi-4k-claude.md (yeni); değişen: ANAYASA (1.1), SISTEM (0.2), KARARLAR, MOC-devlet, HARITA, README, CLAUDE.md, AGENTS.md, hook iletileri, şemalar, ajanlar, skill açıklamaları; klasör ~/Downloads/yeni-sistem → ~/Downloads/4k-claude
- Kapanış notu: Ad değişti; canlı dosyalarda eski ad yok, tarihî kayıtlar korundu. Açık: eski Claude Code oturum geçmişi eski yola bağlı; ~/Downloads/yeni-sistem.zip ve "Yeni Sistem Şeması.md" klasör dışı, dokunulmadı.

## T-007 — Yenilikçi YZ araç ve teknoloji araştırmasını kaynak sayfası olarak kaydet
- Tarih: 2026-10-06
- Niyet: Sahibinin "Graphify gibi yapay zeka çözümlerini ve yenilikçi teknolojileri araştır, dahil edebileceklerimizi bul" isteği. Araştırma alt ajanının raporu 00-sistem/arastirma/10 olarak, 09-github-taramasi kararlarını tekrar etmeden, BENİMSE/ÖDÜNÇ AL/İZLE/UNCONFIRMED etiketleriyle sisteme girer.
- Başarı ölçütü: sayfa var, SEMA'ya uygun; dayandığı raporlar ve ARAC-KAYDI ile iki yönlü bağ; HARITA ve GUNLUK satırı; kontrol.py sıfır hata.
- Sınırlar: Hiçbir araç kurulmaz, ayar değiştirilmez; öneriler sahibinin seçimiyle ayrı talimatlara döner (sandbox açmak imza ister).
- Kat: 0
- Kapı: cift-yonlu
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/arastirma/10-yenilikci-teknolojiler.md (yeni); değişen: arastirma 02/04/05/08/09 (besledigi, 1.1), ARAC-KAYDI (0.2), HARITA
- Kapanış notu: 10 öncelikli öneri kayıtlı; hiçbiri kurulmadı. Sahibinin seçimi bekleniyor (öncelik 1 sandbox imza ister). Ara hata: backlink betiği 5 raporu boşalttı, git HEAD'den geri yüklenip yeniden uygulandı.

## T-008 — Bash sandbox'ını aç (öncelik 1)
- Tarih: 2026-10-06
- Niyet: 10-yenilikci-teknolojiler öncelik 1: Claude Code Bash sandbox'ı (bubblewrap + socat) proje ayarında açılır; sandbox kurulamazsa oturum açılmaz, sandbox dışına kaçış kapalıdır, kimlik bilgisi klasörleri okunamaz.
- Başarı ölçütü: settings.json'da sandbox bloğu; gerçek bir Claude Code oturumunda (claude -p) beş yoklama beklenen sonucu verir: ev dizinine yazma reddedilir, proxy dışı ağ çözülemez, ~/.ssh okunamaz, .claude/hooks'a yazma reddedilir, kontrol.py çalışır; kontrol.py sıfır hata.
- Sınırlar: Ağ izin listesi boş başlar (alan adı eklemek ayrı karar). Kullanıcı ayarına (~/.claude/settings.json) dokunulmaz; yalnız bu proje.
- Kat: 0
- Kapı: cift-yonlu (ayar geri alınabilir) · imza: sahibi (KP-001)
- Durum: kapali
- Doğurduğu dosyalar: 30-devlet/kapilar/KP-001-sandbox-acilisi.md (yeni); değişen: .claude/settings.json, SISTEM (0.3), MOC-devlet, arastirma/10 (1.1), HARITA, DEGISIKLIKLER
- Kapanış notu: Sandbox açık ve gerçek oturumda doğrulandı (ev dizinine yazma, proxy dışı ağ, .claude/hooks yazma reddedildi; ~/.config/gh ve keyrings boş göründü; kontrol.py çalıştı). Açık: klasör yeni adıyla güvenilir değil (sahibi bir kez etkileşimli claude açıp onaylamalı); maliyet tahmini gerçek faturadan ~%30 düşük (1 saatlik önbellek yazımı 2× fiyatlanıyor) → ccusage mutabakatı (öncelik 7).

## T-009 — graf.py: Graphify'ı LLM'siz kütüphane olarak bağla (öncelik 2)
- Tarih: 2026-10-06
- Niyet: 10-yenilikci-teknolojiler öncelik 2: frontmatter bağlarından (dayandigi, ust) ve gövde wikilink'lerinden sayfa grafı kurmak; Graphify ile topluluk, merkez düğüm, sınır aşan bağ ve HTML görünümü üretmek; kopuk küme ve yetim sayfayı raporlamak.
- Başarı ölçütü: graf.py çalışır (çıkış 0), graphify yokken çıkış 2; çıktılar 00-sistem/.kosu/graf/ (git dışı); kurulu paket incelenen 0.9.77 ile birebir (sha256); ARAC-KAYDI satırı; kontrol.py sıfır hata.
- Sınırlar: graphify install, git hook'ları, --mode deep yok; LLM çağrısı yok. Bulunan yapısal sorunlar düzeltilmez, raporlanır.
- Kat: 0
- Kapı: cift-yonlu · araç kaydı A10 değil (dış erişim vermez; B7, sahibinin sıra onayı 2026-10-06)
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/scripts/graf.py (yeni), .venv/ (git dışı); değişen: yscommon.py, sikistirma-oncesi.py, settings.json, CLAUDE.md, uyku SKILL.md, ARAC-KAYDI (0.3), .gitignore, DEGISIKLIKLER
- Kapanış notu: graf.py çalışıyor (doğrudan ve sandbox içinde çıkış 0; graphify yokken 2). İlk bulgu: 40-ic-ses katı (MOC-ic-ses, F-0001, nerede-kaldik) sistemin geri kalanından kopuk; düzeltme sahibinin içerik kararı (öneri: MOC-ic-ses dayandigi += arastirma/08, ya da SISTEM besledigi += MOC-ic-ses).

## T-010 — qmd: yerel anlamsal arama (öncelik 3)
- Tarih: 2026-10-06
- Niyet: 10-yenilikci-teknolojiler öncelik 3: wiki için yerel hibrit arama (BM25 + vektör + yeniden sıralama). Proje içine sabit sürümle kurulur (`.araclar/`, git dışı); dizin ve modeller proje içinde tutulur ki sandbox içinden güncellenebilsin. Türkçe isabet ölçülür.
- Başarı ölçütü: `ara.py` sarmalayıcısı çalışır; 20 Türkçe sorguda isabet@3 ölçülür ve BM25 ile karşılaştırılır; sonuç 40-ic-ses/arastirma-notlari'na yazılır; 01-gelen dizine girmez; kontrol.py sıfır hata.
- Sınırlar: Global kurulum yok. MCP sunucusu (.mcp.json) yalnız ölçüm tatmin ediciyse eklenir. Modeller yalnız ilk kurulumda HuggingFace'ten iner (sonra ağ yok).
- Kat: 0
- Kapı: cift-yonlu · yerel araç, dış erişim vermez (B7); sahibinin sıra onayı 2026-10-06
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/scripts/ara.py, 00-sistem/scripts/ara-olcum.py, 40-ic-ses/arastirma-notlari/qmd-turkce-isabet.md (yeni), .araclar/ (git dışı); değişen: şema + SEMA (0.3) + kontrol.py (sonuc türleri), ARAC-KAYDI (0.4), MOC-ic-ses (0.2), arastirma/10 (1.2), settings.json, CLAUDE.md, HARITA, DEGISIKLIKLER
- Kapanış notu: Vektör arama Türkçe çalışıyor (%75@1, %90@3, 4.5 sn); kelime araması Türkçe cümlede %0; hibrit daha kötü. MCP eklenmedi (30 sayfada gereksiz; 100 sayfada yeniden ölç). Yan etki: not araştırma 10'a dayandığı için 40-ic-ses kopuk kümesi bağlandı (graf: 1 bileşen). T-005 kalıntısı sonuc şema uyumsuzluğu düzeltildi.

## T-011 — Ayar denetimi hook'u (öncelik 4)
- Tarih: 2026-10-07
- Niyet: 10-yenilikci-teknolojiler öncelik 4: `.claude` ayarlarının kendisine "kural ile engel ayrıdır" ilkesini uygulamak. Güvenlik değişmezlerini (sandbox, deny kuralları, koruma hook'ları, izin kipi) bozan ayar değişikliği oturum içinde engellenir; oturum açılışında diskteki ihlal uyarılır; her geçerli değişiklik anahtar düzeyinde GUNLUK'e yazılır; auto kipte izin reddi kaydedilir.
- Başarı ölçütü: değişmez listesi tek yerde; örnek girdilerle (geçerli, ihlal, imzalı istisna, geçersiz JSON, skills, izin reddi, açılış uyarısı) beklenen karar; gerçek oturumda dışarıdan yapılan sandbox kapatma girişimi engellenir ve kaydedilir; kontrol.py sıfır hata.
- Sınırlar: Değişen dosya geri alınmaz (yalnız oturuma yüklenmesi engellenir, sahibine bildirilir). policy_settings engellenemez (belge). Kullanıcı ayarına yazılmaz.
- Kat: 0
- Kapı: cift-yonlu · sahibinin sıra onayı 2026-10-07
- Durum: kapali
- Doğurduğu dosyalar: .claude/hooks/ayar-denetimi.py (yeni); değişen: settings.json (ConfigChange, PermissionDenied, SessionStart), kapanis-kaydi.py, SISTEM (0.4), CLAUDE.md, DEGISIKLIKLER
- Kapanış notu: 17 durumluk izole test doğru; gerçek oturumda dışarıdan diske yazılan sandbox kapatma ayarı yüklenmedi, ev dizinine yazma reddedildi, engelleme GUNLUK'te. İlk gerçek testte sandbox'ın 0 baytlık yer tutucusu "geçersiz JSON" diye engellenip 2 gürültü satırı yazdı (GUNLUK 00:48); boş dosya artık "ayar yok" sayılıyor, farksız değişiklik yazılmıyor. Açık: IMZA-MATRISI'ne imzalı istisna satırı eklemek sahibinin işi (norm).

## T-012 — Gelen kutusu besleme: belge ve web → 01-gelen (öncelik 5)
- Tarih: 2026-10-07
- Niyet: 10-yenilikci-teknolojiler öncelik 5: PDF/DOCX/PPTX/XLSX/HTML ve URL'yi yerelde markdown'a çevirip şablona uygun ham not olarak 01-gelen'e koyan `al.py`; Obsidian Web Clipper şablonu. Dönüştürücü kanıtla seçilir (önce hafif markitdown; Türkçe PDF'te yetmezse docling).
- Başarı ölçütü: gerçek bir Türkçe PDF ve bir DOCX/HTML örneği dönüşür, Türkçe karakter ve tablo korunur (örnek satırlar kanıt); üretilen not kontrol.py'den geçer; kötü niyetli meta veri (başlıkta YAML kırıcı karakter) frontmatter'ı bozmaz; içerik ara.py dizinine girmez.
- Sınırlar: Dönüşen içerik okunmaz/özetlenmez (okuyucu işi). Web Clipper kurulumu ve telefon eşlemesi (Syncthing) sahibinin insan noktası; yalnız şablon ve talimat hazırlanır. URL alma ağ ister: sandbox içinde alan adı onayı gerekir.
- Kat: 0
- Kapı: cift-yonlu · yerel araç (B7); sahibinin sıra onayı 2026-10-07
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/scripts/al.py, 00-sistem/sablonlar/web-clipper-gelen.json (yeni); değişen: kontrol.py, graf.py, settings.json (env + allow), ARAC-KAYDI (0.5), SISTEM (0.5), CLAUDE.md, DEGISIKLIKLER
- Kapanış notu: markitdown Türkçe PDF'te kayıpsız (73 bin karakter, 0 bozuk, tablolar korunur); kötü niyetli başlık ve dosya adı frontmatter'ı bozmadı; sahte wikilink kontrolü kırmadı; sandbox içinde çalışıyor. docling kurulmadı (kanıtla). Beklenmeyen bulgu: onnxruntime 1.30 Microsoft telemetrisi (cihaz kimliği + 24 olaylık kuyruk ~/.cache/Microsoft/DeveloperTools/.onnxruntime/, sandbox'ta proje köküne ":memory:.ses"); ORT_DISABLE_TELEMETRY=1 ile durduruldu, resmi disable_telemetry_events() etkisiz. Kayıt betiği tırnak hatasıyla çalışmadan commit atıldı (215e41d); kayıtlar ayrı commit'le tamamlandı. Açık: kuyruğun silinmesi sahibinin kararı (proje dışı); Web Clipper şablonu gerçek eklentide sınanmadı.

## T-013 — Bağlantı canlılığı (lychee) ve maliyet mutabakatı (ccusage) (öncelik 6)
- Tarih: 2026-10-07
- Niyet: 10-yenilikci-teknolojiler öncelik 6'nın yerel parçaları: kaynak sayfalarındaki URL'lerin canlılığını denetleyen `canli.py` (lychee) ve MALIYET.csv tahminini Claude Code oturum kayıtlarıyla karşılaştıran `maliyet.py` (ccusage). agent-scan bu talimatta YOK: içerik Snyk API'sine gider ve hesap ister (araştırma 10'daki "yerel" bilgisi yanlıştı); sahibinin kararı bekleniyor.
- Başarı ölçütü: iki betik çalışır (çıkış kodu anlamlı); ilk canlılık raporu ve ilk mutabakat sonucu kanıt olarak; 01-gelen URL'leri denetlenmez (güvenilmeyen); kontrol.py sıfır hata.
- Sınırlar: Ölü bağlantı otomatik düzeltilmez (rapor; düzeltme /degistir ile). MALIYET.csv satırları yeniden yazılmaz. Sürüm sabit, proje içine kurulum (.araclar).
- Kat: 0
- Kapı: cift-yonlu · yerel araçlar (B7); sahibinin sıra onayı 2026-10-07
- Durum: kapali
- Doğurduğu dosyalar: 00-sistem/scripts/canli.py, 00-sistem/scripts/maliyet.py (yeni), .araclar/lychee, .araclar/ccusage (git dışı); değişen: kapanis-kaydi.py, settings.json, CLAUDE.md, haftalik SKILL.md, ARAC-KAYDI (0.6), arastirma/10 (1.3), DEGISIKLIKLER
- Kapanış notu: canli.py ilk rapor: 414 bağlantı, 401 canlı, 3 kesin ölü (404: arastirma/03 ADP 6-0 PDF; arastirma/07 enerji.gov.tr imza yönergesi ve anayasa.gov.tr norm kararı PDF'leri), 6 belirsiz. maliyet.py: T-013 öncesi 9 satır ccusage'in %27-34 altında (kök neden: önbellek yazımı tek tip 1.25×); kapanis-kaydi TTL ayrımıyla düzeltildi, yeni satır %0.0 fark. Sandbox içinde maliyet.py çalışıyor; canli.py ağ istediği için sahibi çalıştırır. agent-scan kurulmadı (veri Snyk'e gider). Ara hata: geçici sunucuları kapatan pkill kendi kabuğunu da öldürdü; kayıt ikinci denemede yazıldı. Açık: 3 ölü bağlantının sayfaları (kaynak) /degistir ile güncellenmeli ya da UNCONFIRMED işaretlenmeli — sahibinin onayıyla.
