#! /bin/bash

# read file line by line
i=0
cat "test_file.txt" | while read line; do {
    echo "$i : $line"
    # echo $line;
    i=$((i+=1))
}
done