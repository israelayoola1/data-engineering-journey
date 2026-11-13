#!/bin/zsh
# Count how many title files have a given status
# usage: ./count_status.sh "Shipped"

if [ -z "$1" ]; then
  echo "usage: ./count_status.sh \"<status>\""
  exit 1
fi

file_status="$1"
count=$(grep -c "'$file_status'" ~/practice/data/transactions_500.sql)
echo "$file_status: $count files"