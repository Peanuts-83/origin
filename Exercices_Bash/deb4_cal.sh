#! /bin/bash

# Shows next year calendar
var=$(date)
var=$((${var#*CET}+1))
cal $var