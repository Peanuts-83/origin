#! /bin/bash

# & execution en parallele
i=0
while [ $i -lt 5 ]; do
  echo $i
  i=$((i+1))
  sleep 1
done
