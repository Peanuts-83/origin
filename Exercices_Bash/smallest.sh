#!/bin/bash
# smallest.sh returns the smallest file in the list provided
# It executes 'wc -l $@ | sort -n | head -1'
# Written by James Grant, r.j.grant@bath.ac.uk


if [[ "$1" == "--help" ]]
    then
    echo "smallest.sh returns the smallest file in the list provided"
    echo "It executes 'wc -l $@ | sort -n | head -1'"
    echo "Written by James Grant, r.j.grant@bath.ac.uk"
    exit 0
fi

wc -l $@ | sort -n | head -1
