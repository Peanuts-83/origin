#! /bin/bash

# entries and issues redirection in file
echo "*** Debut ***" > sub1/test_file3.txt # > for creating file or erasing old data
ls -la >> sub1/test_file3.txt # >> for appending data
echo "*** Fin ***" >> sub1/test_file3.txt

