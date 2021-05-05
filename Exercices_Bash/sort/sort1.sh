#!/bin/bash

head -2 file1.txt               # cat 2 first lines
tail +3 file1.txt | sort -k2n    # sort data by 2nd value // n for numeric