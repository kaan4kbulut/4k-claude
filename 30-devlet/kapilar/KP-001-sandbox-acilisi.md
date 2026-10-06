---
id: 20261006-2353-kp-001-sandbox-acilisi
ad: kp-001-sandbox-acilisi
tur: kapi
kat: 3
surum: 1.0
durum: aktif
amac: Bu kapi kaydi, Claude Code Bash sandbox'inin bu projede acilmasi karari icin sahibinin onayini, kriterleri ve sonucu tutmak icin var.
olusturma: 2026-10-06
guncelleme: 2026-10-06
yazar: claude
talimat: T-008
dayandigi: [00-sistem/arastirma/10-yenilikci-teknolojiler.md]
besledigi: []
ust: 30-devlet/MOC-devlet.md
kapi_turu: adhoc
kapi: cift-yonlu
karar_veren: kaan
bekci: kaan
sonuc: go
saklama: S
etiketler: [kapi/guvenlik]
---

# Kapı KP-001: Bash sandbox'ının açılışı

## Amaç
Bu kapı kaydı, Claude Code Bash sandbox'ının bu projede açılması kararı için sahibinin onayını, kriterleri ve sonucu tutmak için var.

## İçerik
### Gerekli teslimatlar
- [[00-sistem/arastirma/10-yenilikci-teknolojiler]] — öncelik 1 gerekçesi ve riskler: hazır
- `.claude/settings.json` sandbox bloğu: T-008'de yazılır

### Kriterler
- Zorunlu: bubblewrap ve socat kurulu (`/usr/bin/bwrap`, `/usr/bin/socat`).
- Zorunlu: sandbox kurulamazsa oturum açılmaz (`failIfUnavailable`), sandbox dışına yeniden deneme kapalı (`allowUnsandboxedCommands: false`).
- Zorunlu: beş yoklama gerçek oturumda beklenen sonucu verir (T-008 kanıtı).
- İstenen: sistem betikleri (kontrol.py, gunluk.py, git commit) sandbox içinde çalışmaya devam eder.

### İmza
Sahibinin onayı, 2026-10-06 sohbet: "tamam önerdiğin sırayla başla, önce sandbox". Karar çift yönlüdür: ayar silinerek geri alınır.

### Sonuç
go — bekçi: kaan.

## Bağlar
### Dayandığı
- [[00-sistem/arastirma/10-yenilikci-teknolojiler]] — öncelik 1 ve sandbox'ın kapsam sınırları (yalnız Bash)
### Beslediği
### Gelen
- ← [[30-devlet/MOC-devlet]] — kapılar listesi

## Günlük
| Sürüm | Tarih | Talimat | Değişiklik |
| --- | --- | --- | --- |
| 1.0 | 2026-10-06 | T-008 | Sahibinin onayıyla go |
