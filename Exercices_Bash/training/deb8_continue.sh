#! /bin/bash

# $0: deb8_continue.sh / $1: dir or subdir name / $2: i(depth with space x4)
# Explore dir and sub-dirs
explore ()
{
  local f
  local i

  i=0
  while [ $i -lt $2 ] ; do
    echo -n " "
    i=$((i + 1))
  done
  echo "$1"

  if ! cd "$1" ; then return ; fi

  for f in *
  do
    if [ -L "$f" ] ; then
      continue
    fi
    if [ -d "$f" ] ; then
      explore "$f" $(($2 + 4))  # recursive call of explore(), second param +4
    fi
  done

  cd ..
}

explore "$1" 0