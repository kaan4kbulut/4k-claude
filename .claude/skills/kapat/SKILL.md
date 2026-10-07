---
name: kapat
description: Oturumu ve aktif talimatı kanıtla kapatır. Yalnız sahibi çağırır. Kanıt bloğu, denetci incelemesi, ILERLEME.md, nerede-kaldik.md, commit ve BLUF brifing üretir.
disable-model-invocation: true
argument-hint: [T-xxx]
---

# /kapat — kanıtla kapanış

Bu komut yan etkilidir (commit atar); yalnız sahibi çağırır. Stop hook'u (durus-kapisi) kanıt ya da ASK.md olmadan oturumu kapatmaz; /kapat bu kanıtı üretir.

Aktif talimat: `$0` (boşsa ILERLEME.md'deki `aktif_talimat`).

Ön kontrol:
!`python3 00-sistem/scripts/kontrol.py --kisa 2>&1 | tail -8`
!`git status --short | head -20`

## 1. Kanıt topla
- Bu oturumda değişen dosyalar: `git status --short`, `git diff --stat`.
- Çalıştırılan kontroller: kontrol.py çıkışı; görev kartı varsa `kabul_olcutleri`ndeki kanıt komutlarını tek tek çalıştır ve çıkış kodlarını yaz.
- Görev kartı varsa `kanit` listesini doldur (komut, çıkış kodu, çıktı özeti ≤ 5 satır). Boş `kanit` ile `durum: tamam` yazma.

## 2. Bağımsız inceleme
- Değişiklik koda ya da kabul ölçütlü bir karta dokunuyorsa `denetci` alt ajanını çağır: yalnız `git diff` ve ilgili görev kartını ver; "doğruluk ve gereksinim boşluklarını raporla, stil değil" de.
- Engelleyici bulgu varsa kapatma: düzelt, yeniden çalıştır. İki turda çözülmezse `[durdu]` kaydı ve ASK.md.
- Yalnız wiki metni değiştiyse (gözlem, fikir, not) denetci atlanabilir; kontrol.py yeter.

## 3. Kayıtları güncelle
- `TALIMATLAR.md`: T-xxx `Durum: kapali`, `Doğurduğu dosyalar`, `Kapanış notu` (bir cümle: ne bitti, ne açık kaldı).
- `00-sistem/ILERLEME.md`: `aktif_talimat` (sıradaki ya da "yok"), `kapi`, `acik_soru`, `degisen_dosyalar`, `siradaki`.
- `40-ic-ses/nerede-kaldik.md`: konuşulan (≤3 madde), açık (≤3), sonraki (1).
- `GUNLUK.md`: `[oturum] T-xxx kapandı — özet`.
- İlgili MOC'ta durum satırı.
- Bu adım elle kapanışta da zorunludur: kontrol.py 16. denetim, son kapanan talimat GUNLUK `[oturum]`, ILERLEME ve nerede-kaldik'te yoksa hata verir (T-025).

## 4. Commit
- `git add -A && git commit -m "T-xxx: <kısa başlık>"`. Gövdede: değişen dosyalar, kanıt özeti. Push yapma (izin sistemi sorar; sahibi ister).

## 5. BLUF brifing (sahibine)
`/brifing` biçiminde, ≤ 1 sayfa:
- **Etiket**: INFO (bitti) / DECISION (karar bekliyor) / ACTION (sahibi bir şey yapacak)
- **BLUF**: tek cümle sonuç + sahibinden istenen.
- **Kanıt**: komutlar, çıkış kodları, değişen dosyalar.
- **Değerlendirme**: riskler, sapmalar, örtülü aldığım kararlar.
- **Açık sorular / sıradaki**.
Kötü haber ilk satırda.

## Çıktı
Mesajın `## Kanıt` başlığı içermeli (Stop hook'u bunu arar). Örnek:

## Kanıt
- `python3 00-sistem/scripts/kontrol.py --kisa` → 0 (Bütünlük tam: N sayfa, M bağ)
- `git commit` → abc1234 "T-003: araştırma görevi kartı"
- değişen: 20-sirket/gorevler/G-001-...md, 00-sistem/HARITA.md, 00-sistem/GUNLUK.md
