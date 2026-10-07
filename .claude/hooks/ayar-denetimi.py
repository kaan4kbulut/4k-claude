#!/usr/bin/env python3
"""Ayar denetimi hook'u — ConfigChange | SessionStart | PermissionDenied.

"Kural ile engel ayrıdır" ilkesini ayarların kendisine uygular (Anayasa Madde 3.6, IMZA-MATRISI):
  ConfigChange      project_settings / local_settings / user_settings: değişmezleri (DEGISMEZLER) denetler.
                    İhlal varsa ve imzası yoksa decision: block — yeni ayar bu oturuma YÜKLENMEZ (dosya diskte değişmiş
                    kalır; geri alınmaz, sahibine bildirilir). Her durumda anahtar düzeyinde fark GUNLUK'e yazılır.
                    skills: yalnız kayıt. policy_settings: engellenemez (Claude Code belgesi), yalnız kayıt.
  SessionStart      Diskteki ayarı denetler; ihlal varsa bağlama uyarı basar (SessionStart engelleyemez) ve GUNLUK'e
                    [hata] yazar. Fark tabanı için ayarların izini 00-sistem/.kosu/ayar-izi.json'a alır.
  PermissionDenied  Auto kipte reddedilen araç çağrısını GUNLUK'e yazar (retry verilmez).
Eklenti ve mod (T-039, K-006): onaylı taban .claude/eklenti-tabani.json; taban dışı enabledPlugins (true),
  extraKnownMarketplaces, pluginConfigs, prependPlugins ConfigChange'de değişmez ihlalidir; .claude/workflows/ altındaki
  taban dışı dosya ve managed settings eksikliği (allowManagedModsOnly) SessionStart'ta uyarıdır. Yol: FOURK_MANAGED.

İmzalı istisna: sahibi bir değişmezi bilerek gevşetmek isterse 30-devlet/kapilar/ altına sonuc: go olan bir kapı
kaydı açar ve .claude/ayar-imzasi.json'a yazar: {"istisnalar": [{"degismez": "<kimlik>", "kapi": "<KP yolu>"}]}.
.claude/ sandbox'taki Bash'ten yazılamaz ve Write aracıyla yazımı sahibine sorulur; ajan kendine imza atamaz.
Hiçbir zaman çökme ile engellemez: kendi hatasında GUNLUK'e yazar ve geçer (yalnız değişmez ihlali engeller).
"""
import json
import os
import re
import stat
import sys
from datetime import datetime

KOK = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
PROJE = os.path.join(KOK, ".claude", "settings.json")
YEREL = os.path.join(KOK, ".claude", "settings.local.json")
KULLANICI = os.path.join(os.path.expanduser("~"), ".claude", "settings.json")
IMZA = os.path.join(KOK, ".claude", "ayar-imzasi.json")
IZ = os.path.join(KOK, "00-sistem", ".kosu", "ayar-izi.json")
TABAN = os.path.join(KOK, ".claude", "eklenti-tabani.json")
WORKFLOWS = os.path.join(KOK, ".claude", "workflows")
YONETILEN = os.environ.get("FOURK_MANAGED") or "/etc/claude-code/managed-settings.json"
EKLENTI_ALANLARI = ("enabledPlugins", "extraKnownMarketplaces", "pluginConfigs", "prependPlugins")

ZORUNLU_DENY = [
    "Edit(30-devlet/normlar/ANAYASA.md)", "Write(30-devlet/normlar/ANAYASA.md)",
    "Bash(rm -rf *)", "Bash(git push --force*)", "Bash(git reset --hard*)",
    "Read(./.env*)", "Bash(graphify install*)",
]
ZORUNLU_HOOKLAR = {
    "PreToolUse": "yikici-koruma.py", "Stop": "durus-kapisi.py", "SessionStart": "oturum-basi.py",
    "ConfigChange": "ayar-denetimi.py", "PreModelSwitch": "model-bekcisi.py",
}
GENIS_ALLOW = re.compile(r"^(Bash|Bash\(\*\)|Edit|Write|Edit\(\*\*\)|Write\(\*\*\)|"
                         r"(Edit|Write)\((\./)?(\.claude|30-devlet)(/.*)?\)|(Edit|Write)\(.*ANAYASA.*\))$")


def oku(yol):
    """(dict | None, hata | None) — dosya yoksa ({}, None)."""
    if not os.path.exists(yol):
        return {}, None
    if stat.S_ISCHR(os.stat(yol).st_mode):
        return {}, None  # sandbox yer tutucusu (/dev/null bağı) "ayar yok" demektir (T-039)
    if not os.path.isfile(yol):
        return None, "sıradan dosya değil (dizin/FIFO)"
    try:
        with open(yol, encoding="utf-8") as f:
            metin = f.read()
        if not metin.strip():
            # Sandbox, komut çalışırken var olmayan korunan ayar dosyasının yerine 0 baytlık salt-okunur bir yer tutucu
            # koyar (Claude Code belgesi); boş dosya "ayar yok" demektir, hata değildir.
            return {}, None
        d = json.loads(metin)
        return (d if isinstance(d, dict) else {}), (None if isinstance(d, dict) else "kök nesne değil")
    except Exception as e:  # noqa: BLE001
        return None, f"geçersiz JSON: {e}"


def degismezleri_denetle(proje, yerel, kullanici):
    """[(kimlik, açıklama)] — ihlaller. Öncelik: yerel > proje > kullanıcı (aynı anahtar için)."""
    ihlal = []

    def etkin(yol):
        for d in (yerel, proje, kullanici):
            v = d
            for p in yol:
                v = v.get(p) if isinstance(v, dict) else None
            if v is not None:
                return v
        return None

    if etkin(["sandbox", "enabled"]) is not True:
        ihlal.append(("sandbox.enabled", "Bash sandbox kapalı ya da tanımsız"))
    if etkin(["sandbox", "failIfUnavailable"]) is not True:
        ihlal.append(("sandbox.failIfUnavailable", "sandbox kurulamazsa sandbox'sız çalışılır"))
    if etkin(["sandbox", "allowUnsandboxedCommands"]) not in (False, "false"):
        ihlal.append(("sandbox.allowUnsandboxedCommands", "sandbox dışına yeniden deneme açık"))
    for ad, d in (("proje", proje), ("yerel", yerel), ("kullanıcı", kullanici)):
        if d.get("disableAllHooks") is True:
            ihlal.append(("disableAllHooks", f"tüm hook'lar kapalı ({ad} ayarı)"))
        for anahtar in (d.get("env") or {}) if isinstance(d.get("env"), dict) else []:
            if str(anahtar).startswith("FOURK_"):
                # hook'ların test/yol değişkenleri (FOURK_MANAGED, FOURK_KASA…) ayardan verilirse denetim başka
                # dosyaya yönlendirilebilir (T-039 denetci)
                ihlal.append((f"env:{anahtar}", f"ayar env'i hook yol değişkeni veriyor ({ad} ayarı): {anahtar}"))
        kip = (d.get("permissions") or {}).get("defaultMode")
        if kip in ("bypassPermissions",):
            ihlal.append(("permissions.defaultMode", f"izin kipi {kip} ({ad} ayarı)"))
        for kural in (d.get("permissions") or {}).get("allow") or []:
            if isinstance(kural, str) and GENIS_ALLOW.match(kural.strip()):
                ihlal.append((f"allow:{kural}", f"geniş/korunan yol için allow kuralı ({ad} ayarı): {kural}"))
    deny = set((proje.get("permissions") or {}).get("deny") or [])
    for kural in ZORUNLU_DENY:
        if kural not in deny:
            ihlal.append((f"deny:{kural}", f"zorunlu deny kuralı eksik: {kural}"))
    hooks = proje.get("hooks") or {}
    for olay, betik in ZORUNLU_HOOKLAR.items():
        komutlar = [h.get("command", "") for grup in hooks.get(olay) or [] for h in grup.get("hooks") or []]
        if not any(betik in k for k in komutlar):
            ihlal.append((f"hook:{olay}", f"{olay} hook'u eksik: {betik}"))
    return ihlal


def eklentileri_denetle(*ayarlar):
    """[(kimlik, açıklama)] — onaylı tabanın (.claude/eklenti-tabani.json) dışındaki eklenti alanları (T-039, K-006).
    Mod/eklenti yolu managed olmayan PreToolUse hook'larını aşabilir; bu yüzden yeni eklenti imzasız yüklenmez."""
    taban, hata = oku(TABAN)
    if hata:
        return [("eklenti:taban", f"eklenti-tabani.json okunamadı: {hata}")]
    ihlal = []
    for d in ayarlar:
        for alan in EKLENTI_ALANLARI:
            v = d.get(alan)
            if not v:
                continue
            if isinstance(v, dict):
                adlar = [k for k, x in v.items() if alan != "enabledPlugins" or x]  # kapatmak (false) gevşetme değil
            elif isinstance(v, list):
                adlar = [x if isinstance(x, str) else json.dumps(x, sort_keys=True) for x in v]
            else:
                adlar = [str(v)]
            for ad in adlar:
                if ad not in (taban.get(alan) or []):
                    ihlal.append((f"eklenti:{alan}:{ad}", f"onaysız eklenti ayarı {alan}: {ad} (taban: .claude/eklenti-tabani.json)"))
    return ihlal


def workflowlari_denetle():
    """[(kimlik, açıklama)] — .claude/workflows/ altında tabanda olmayan dosya (sandbox yer tutucusu dizin değildir)."""
    if not os.path.isdir(WORKFLOWS):
        return []
    taban = (oku(TABAN)[0] or {}).get("workflows") or []
    ihlal = []
    for dizin, _, dosyalar in os.walk(WORKFLOWS):
        for f in dosyalar:
            g = os.path.relpath(os.path.join(dizin, f), WORKFLOWS)
            if g not in taban:
                ihlal.append((f"workflow:{g}", f"onaysız workflow dosyası: .claude/workflows/{g}"))
    return ihlal


def yonetileni_denetle():
    """[(kimlik, açıklama)] — K-006: yalnız yönetilen mod'lar makine düzeyinde açık mı."""
    if not os.path.exists(YONETILEN):
        return [("managed:yok", f"managed settings yok ({YONETILEN}): kullanıcı/Claude yazımı mod'lar koruma hook'larını aşabilir (K-006)")]
    d, hata = oku(YONETILEN)
    if hata:
        return [("managed:okunamadi", f"managed settings okunamadı: {hata}")]
    secenek = (((d.get("pluginConfigs") or {}).get("cc-plugin-sec-default@builtin") or {}).get("options") or {})
    ihlal = []
    if secenek.get("allowManagedModsOnly") is not True:
        ihlal.append(("managed:allowManagedModsOnly", "managed settings'te allowManagedModsOnly true değil (K-006)"))
    if secenek.get("allowModsToOverrideDenyRules") is True:
        ihlal.append(("managed:allowModsToOverrideDenyRules", "managed settings mod'ların deny kuralını aşmasına izin veriyor (K-006)"))
    return ihlal


def imzali_istisnalar():
    d, hata = oku(IMZA)
    if not d or hata:
        return set(), ([f"ayar-imzasi.json okunamadı: {hata}"] if hata else [])
    gecerli, notlar = set(), []
    for i in d.get("istisnalar") or []:
        kimlik, kapi = (i or {}).get("degismez"), (i or {}).get("kapi")
        yol = os.path.join(KOK, kapi or "")
        if not (kimlik and kapi and os.path.isfile(yol)):
            notlar.append(f"imza geçersiz (kapı kaydı yok): {kimlik} → {kapi}")
            continue
        with open(yol, encoding="utf-8") as f:
            if not re.search(r"^sonuc:\s*go\s*$", f.read(), re.M):
                notlar.append(f"imza geçersiz (kapı sonucu go değil): {kimlik} → {kapi}")
                continue
        gecerli.add(kimlik)
    return gecerli, notlar


def ozet(d):
    """Fark için düzleştirilmiş görünüm: anahtar yolları ve izin kuralları."""
    duz = {}

    def gez(v, on=""):
        if isinstance(v, dict) and on.count(".") < 2 and on not in ("hooks",):
            for k, x in v.items():
                gez(x, f"{on}.{k}" if on else k)
        else:
            duz[on] = json.dumps(v, ensure_ascii=False, sort_keys=True)[:200]
    gez({k: v for k, v in d.items() if k != "permissions"})
    for tur in ("allow", "ask", "deny"):
        for kural in (d.get("permissions") or {}).get(tur) or []:
            duz[f"permissions.{tur}:{kural}"] = "1"
    return duz


def fark(eski, yeni):
    eklenen = sorted(k for k in yeni if k not in eski)
    cikan = sorted(k for k in eski if k not in yeni)
    degisen = sorted(k for k in yeni if k in eski and eski[k] != yeni[k])
    p = [f"+{k}" for k in eklenen] + [f"-{k}" for k in cikan] + [f"~{k}" for k in degisen]
    return ", ".join(p[:8]) + (f" (+{len(p) - 8})" if len(p) > 8 else "") if p else "anlamlı fark yok"


def iz_oku():
    try:
        with open(IZ, encoding="utf-8") as f:
            return json.load(f)
    except Exception:  # noqa: BLE001
        return {}


def iz_yaz(izler):
    os.makedirs(os.path.dirname(IZ), exist_ok=True)
    with open(IZ, "w", encoding="utf-8") as f:
        json.dump(izler, f, ensure_ascii=False)


def gunluk(tur, yol, not_):
    satir = f"{datetime.now().strftime('%Y-%m-%d %H:%M')} [{tur}] {yol} — {' '.join(str(not_).split())[:400]}"
    try:
        with open(os.path.join(KOK, "00-sistem", "GUNLUK.md"), "a", encoding="utf-8") as f:
            f.write(satir + "\n")
    except Exception:  # noqa: BLE001
        pass


def goreli(yol):
    try:
        return os.path.relpath(yol, KOK) if os.path.abspath(yol).startswith(KOK) else yol.replace(os.path.expanduser("~"), "~")
    except Exception:  # noqa: BLE001
        return yol


def config_change(girdi):
    kaynak = girdi.get("source", "?")
    dosya = girdi.get("file_path") or ""
    if kaynak == "skills":
        gunluk("ayar", goreli(dosya) or "skills", "skill dosyası değişti (denetim izi)")
        return None
    if kaynak not in ("project_settings", "local_settings", "user_settings"):
        yon = [a for _, a in yonetileni_denetle()] if kaynak == "policy_settings" else []
        gunluk("hata" if yon else "ayar", goreli(dosya) or kaynak,
               f"{kaynak} değişti (engellenemez; denetim izi)" + ("; " + "; ".join(yon) if yon else ""))
        return None
    dosyalar = {"project_settings": PROJE, "local_settings": YEREL, "user_settings": KULLANICI}
    okunan = {k: oku(v) for k, v in dosyalar.items()}
    hatali = [f"{goreli(dosyalar[k])}: {h}" for k, (d, h) in okunan.items() if h]
    izler = iz_oku()
    yeni_ozet = ozet(okunan[kaynak][0] or {})
    degisim = fark(izler.get(kaynak, {}), yeni_ozet)
    if hatali:
        gunluk("hata", goreli(dosya), "ayar değişikliği ENGELLENDİ — " + "; ".join(hatali))
        return "Ayar dosyası okunamıyor, değişiklik bu oturuma yüklenmedi: " + "; ".join(hatali)
    ayarlar = [okunan[k][0] for k in ("project_settings", "local_settings", "user_settings")]
    ihlal = degismezleri_denetle(*ayarlar) + eklentileri_denetle(*ayarlar)
    imzali, notlar = imzali_istisnalar()
    kalan = [(k, a) for k, a in ihlal if k not in imzali]
    if kalan:
        gunluk("hata", goreli(dosya), f"ayar değişikliği ENGELLENDİ ({degisim}) — "
               + "; ".join(a for _, a in kalan) + ("; " + "; ".join(notlar) if notlar else ""))
        return ("4k-claude ayar denetimi: bu değişiklik güvenlik değişmezlerini bozuyor ve bu oturuma YÜKLENMEDİ "
                "(dosya diskte değişmiş durumda; bir sonraki oturum uyarı verir):\n- " + "\n- ".join(a for _, a in kalan)
                + "\nSahibi bilerek yapıyorsa: 30-devlet/kapilar/ altına sonuc: go kapı kaydı ve .claude/ayar-imzasi.json "
                  "istisnası gerekir (IMZA-MATRISI). Değilse dosyayı eski haline getir (git diff .claude/).")
    izler[kaynak] = yeni_ozet
    iz_yaz(izler)
    if degisim == "anlamlı fark yok":
        return None  # sandbox yer tutucusu ya da biçim değişikliği: kayıt gürültüsü yapma
    gunluk("ayar", goreli(dosya), f"{kaynak} değişti: {degisim}; değişmezler tamam"
           + (f" (imzalı istisna: {', '.join(sorted(imzali & {k for k, _ in ihlal}))})" if imzali & {k for k, _ in ihlal} else ""))
    return None


def session_start(girdi):
    okunan = {"project_settings": oku(PROJE), "local_settings": oku(YEREL), "user_settings": oku(KULLANICI)}
    iz_yaz({k: ozet(d or {}) for k, (d, h) in okunan.items()})
    hatali = [f"{k}: {h}" for k, (d, h) in okunan.items() if h]
    ayarlar = [(okunan[k][0] or {}) for k in ("project_settings", "local_settings", "user_settings")]
    ihlal = degismezleri_denetle(*ayarlar) + eklentileri_denetle(*ayarlar) + workflowlari_denetle() + yonetileni_denetle()
    imzali, notlar = imzali_istisnalar()
    kalan = [a for k, a in ihlal if k not in imzali] + hatali + notlar
    if not kalan:
        return None
    gunluk("hata", ".claude/settings.json", "oturum açılışında ayar ihlali: " + "; ".join(kalan))
    return ("## AYAR İHLALİ (ayar-denetimi) — önce bunu sahibine sor\n"
            "Diskteki ayarlar güvenlik değişmezlerini bozuyor; bu oturum gevşetilmiş ayarla çalışıyor olabilir:\n- "
            + "\n- ".join(kalan)
            + "\nBu düzelmeden (git diff .claude/) ya da imzalı istisna olmadan iş yapma; /kapi ile ASK.md yaz.")


def permission_denied(girdi):
    arac = girdi.get("tool_name", "?")
    ti = girdi.get("tool_input") or {}
    hedef = ti.get("command") or ti.get("file_path") or ti.get("url") or ""
    gunluk("hata", f"izin-reddi {arac}", f"{str(girdi.get('denial_reason', ''))[:160]} — {str(hedef)[:160]}"
           + ("" if girdi.get("has_classifier_verdict") else " (sınıflandırıcısız)"))


def main():
    try:
        girdi = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    olay = girdi.get("hook_event_name", "")
    try:
        if olay == "ConfigChange":
            neden = config_change(girdi)
            if neden:
                print(json.dumps({"decision": "block", "reason": neden}, ensure_ascii=False))
        elif olay == "SessionStart":
            uyari = session_start(girdi)
            if uyari:
                print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": uyari}},
                                 ensure_ascii=False))
        elif olay == "PermissionDenied":
            permission_denied(girdi)
    except Exception as e:  # noqa: BLE001
        gunluk("hata", ".claude/hooks/ayar-denetimi.py", f"hook hatası ({olay}): {e}")
    sys.exit(0)


if __name__ == "__main__":
    main()
