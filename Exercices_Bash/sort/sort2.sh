#!/bin/bash
head -2 file2.txt               # cat 2 first lines
tail +3 file2.txt | tr : ' ' | sort -k2n -k3n -k4n -k1     # sort data by 2nd 3rd 4th 1st value // n for numeric
echo -e "\nSort by 3rd letter of name"
tail +3 file2.txt | sort -b -k 1.3 # -b ignore blanks // field 1 / 3rd letter