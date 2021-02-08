#! /bin/bash

# Eval correspondance between 2 args in a function
function corresp {
  case "$1" in
    $2) return 0 ;;
    *)  return 1 ;;
  esac
}

# | for 'or', '?' to replace a charact, '*' to replace multi charact
if corresp "azer" "azer" ; then echo Oui ; else echo Non ; fi
if corresp "azer" "a?er" ; then echo Oui ; else echo Non ; fi
if corresp "azer" "a*r" ; then echo Oui ; else echo Non ; fi
if corresp "azer" "a*b" ; then echo Oui ; else echo Non ; fi
if corresp "azer" "azur" ; then echo Oui ; else echo Non ; fi
if corresp "azer" "azur" | corresp "azer" "a?er" ; then echo Oui ; else echo Non ; fi