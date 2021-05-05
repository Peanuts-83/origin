#! /bin/bash

# For to iterate in a list
# Enumerate parameters of the function
for i in "$@"; do echo $i ; done


# renaming file function
# first use 'echo' to try test
# for i in *.tgz; do echo mv $i ${i%%.tgz}.tar.gz ; done

# then do it without 'echo' / "" protection if white spaces in filenames!
# for i in *.tgz; do mv "$i" "${i%%.tgz}.tar.gz" ; done
