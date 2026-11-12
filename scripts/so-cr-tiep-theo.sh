#!/usr/bin/env bash
# Tìm thư mục CR của tháng và mã CR tiếp theo.
# Cách dùng: bash so-cr-tiep-theo.sh "<thư mục gốc CR>" [YYMM]
# YYMM bỏ trống thì lấy tháng hiện tại.

root="$1"
yymm="${2:-$(date +%y%m)}"
if [ -z "$root" ] || [ ! -d "$root" ]; then
  echo "LOI=Không tìm thấy thư mục gốc CR: $root" >&2
  exit 1
fi

dir="$root/CR-$yymm"
last=$(ls "$dir" 2>/dev/null | grep -oE "^CR-$yymm-[0-9]{3}" | sort -u | tail -1)
if [ -n "$last" ]; then
  n=$((10#${last##*-} + 1))
else
  n=1
fi

echo "THU_MUC=$dir"
[ -d "$dir" ] && echo "THU_MUC_DA_CO=co" || echo "THU_MUC_DA_CO=chua"
printf 'MA_CR=CR-%s-%03d\n' "$yymm" "$n"
echo "CR_DA_CO:"
ls "$dir" 2>/dev/null | grep -E "^CR-$yymm-[0-9]{3}.*\.md$" | grep -vE "\.(note|test|auto)\.md$" | sed 's/^/  /'
