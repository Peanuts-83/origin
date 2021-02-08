#! /bin/bash

# Motifs extraction / dissociates path and file/dir name
v1=${1}
path_1=${v1:-"sub1/"}

for file in $(ls $path_1)
do
  if [ $path_1 != "." ]
  then
    full_path=$(readlink -f $path_1$file)
    echo "path is: ${full_path%/*}/"
    echo "file is: ${full_path##*/}"
  else
    full_path=$(readlink -f $file)
    echo "path is: ${full_path%/*}/"
    echo "file is: ${full_path##*/}"
  fi
done