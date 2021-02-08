#! /bin/bash

# While do cmd while condition is true / Until do cmd until condition becomes true
# factorial script

n=${1:-1}
i=1
f=1

while [ $i -le $n ] ; do
  f=$((f * i))
  i=$((i + 1))
done

echo "$n! = $f"