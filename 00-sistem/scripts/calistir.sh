#!/usr/bin/env bash
# calistir.sh — gözetimsiz Claude Code koşusu (zamanlı görevler, rutinler, CI).
# Kullanım: 00-sistem/scripts/calistir.sh "<T-xxx>" "<istem>" [max_turns] [max_usd]
# Örnek:    00-sistem/scripts/calistir.sh T-007 "/uyku tam" 30 2
#
# İlkeler (arastirma/04 §2.6):
#  - --bare: repo hook'ları ve MCP yalnız güvenilir klasörde; güven iletişim kutuları -p'de kapalı olduğundan dikkat.
#  - --max-turns ve --max-budget-usd: kaçak koşu yok. Alt ajan harcaması da sayılır.
#  - --fallback-model: model yoksa Sonnet'e düş.
#  - --json-schema: çıktı kapi-raporu şemasına uyar; durum gecti|bekliyor|durdu.
#  - Gözetimsiz koşuda onay sorulamaz: iş "hazırla → (insan onaylar) → uygula" olarak bölünür. Onay gerektiren adıma gelince
#    skill ASK.md yazar ve durum bekliyor döner.
#  - Çıktı ve maliyet GUNLUK.md'ye düşer.
set -euo pipefail
cd "$(dirname "$0")/../.."

T="${1:?talimat numarası (T-xxx) gerekli}"
ISTEM="${2:?istem gerekli}"
MAX_TURNS="${3:-30}"
MAX_USD="${4:-2}"
SEMA="00-sistem/sema/kapi-raporu.schema.json"
ZAMAN="$(date +%Y-%m-%d\ %H:%M)"
CIKTI_DIR="00-sistem/.kosu"
mkdir -p "$CIKTI_DIR"
CIKTI="$CIKTI_DIR/${T}-$(date +%Y%m%d-%H%M%S).json"

echo "$ZAMAN [oturum] $T — gözetimsiz koşu başladı: $ISTEM (turn<=$MAX_TURNS, usd<=$MAX_USD)" >> 00-sistem/GUNLUK.md

set +e
claude -p --bare \
  --max-turns "$MAX_TURNS" \
  --max-budget-usd "$MAX_USD" \
  --fallback-model sonnet \
  --permission-mode auto \
  --permission-prompts none \
  --output-format json \
  --json-schema "$(cat "$SEMA")" \
  --name "$T" \
  "Talimat $T. Önce 00-sistem/ILERLEME.md ve 00-sistem/HARITA.md'yi oku. Gözetimsiz koşudasın: soru soramazsın; onay gereken adımda /kapi ile ASK.md yaz ve durum=bekliyor döndür. İş: $ISTEM. Bitince kanıtla kapat ve kapi-raporu şemasına uygun JSON ver." \
  > "$CIKTI" 2>"$CIKTI_DIR/${T}-hata.log"
KOD=$?
set -e

DURUM="$(python3 -c "import json,sys; d=json.load(open('$CIKTI')); s=d.get('structured_output') or d; print(s.get('durum','?'))" 2>/dev/null || echo '?')"
MALIYET="$(python3 -c "import json; d=json.load(open('$CIKTI')); print(d.get('total_cost_usd','?'))" 2>/dev/null || echo '?')"
echo "$(date +%Y-%m-%d\ %H:%M) [oturum] $T — gözetimsiz koşu bitti: kod=$KOD durum=$DURUM usd=$MALIYET çıktı=$CIKTI" >> 00-sistem/GUNLUK.md

if [ "$KOD" -ne 0 ]; then
  echo "$(date +%Y-%m-%d\ %H:%M) [hata] $T — claude çıkış kodu $KOD; bkz. $CIKTI_DIR/${T}-hata.log" >> 00-sistem/GUNLUK.md
fi
echo "durum=$DURUM kod=$KOD çıktı=$CIKTI"
exit "$KOD"
