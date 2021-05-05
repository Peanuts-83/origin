#! /bin/bash

# Rename files with 'content' in place of 'file'
v1=${1}
v2=${2}
path_1=${v1:-"sub1/"}
path_2=${v2:-"sub2/"}

for file_name in $(ls $path_2); do {
  echo ${file_name/file/content}
  mv $path_2/$file_name $path_2/${file_name/file/content}
} done

# for file in $(ls $path_2); do {
#   tr [:upper:] [:lower:] < $path_2/$file > "$path_1/lower_${file#"upper_"}"
# } done
