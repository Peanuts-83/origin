#! /bin/bash

# Put upper copy in new file, then lower in an other
v1=${1}
v2=${2}
path_1=${v1:-"sub1/"}
path_2=${v2:-"sub2/"}

for file in $(ls $path_1); do {
  # cat $path_1/$file
  # echo $path_1 $path_2
  tr [:lower:] [:upper:] < $path_1/$file > "$path_2/upper_${file##"upper_"}"
} done

for file in $(ls $path_2); do {
  tr [:upper:] [:lower:] < $path_2/$file > "$path_1/lower_${file##"upper_"}"
} done
