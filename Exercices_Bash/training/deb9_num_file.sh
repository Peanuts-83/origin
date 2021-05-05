#! /bin/bash

# for loop / echo filenames with num id
# i=1
# for file in *
# do
#   echo "$i) $file"
#   i=$((i+1))
# done

# while loop / echo cmd line 5 times, sleep 1 each
# i=0
# while [ $i -lt 5 ]
# do
#   echo "$1"
#   i=$((i+1))
#   sleep 1
# done
# execute 3 times in the same time
# ./deb9_num_file.sh AAA & ./deb9_num_file.sh BBB & ./deb9_num_file.sh CCC

# file tester / needs to pass filenam in param
echo PID: $$
echo "******** FILE TESTER ***********"
echo "$(readlink -f $1)"
echo "        *************           "
if [ -f $1 ]
then
  echo "$1 is a valid file"
  [ -b $1 ] && echo "$1 is a block file"
  [ -c $1 ] && echo "$1 is a character special file"
  [ -L $1 ] && echo "$1 is a symbolic link"
  [ -p $1 ] && echo "$1 is a named pipe"
  [ -r $1 ] && echo "$1 has read permission granted"
  [ -w $1 ] && echo "$1 has write permission granted"
  [ -x $1 ] && echo "$1 has execute permission granted"
  [ -O $1 ] && echo "$1 is owned by effective UID"
  [ -G $1 ] && echo "$1 is owned by effective GID"  
  echo "*******************************"
  cat $1
elif [ -d $1 ] ; then echo "$1 is a directory name..."
else
  echo "$1 is an invalid filename!"
fi