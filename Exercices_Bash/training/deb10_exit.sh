#! /bin/bash

# exit shuts shell and gives back arg (0/1 etc...)
check_file ()
{
  if [ ! -f $1 ]
  then 
    echo "$1 doesn't exist"
    exit 1
  fi
}

if [ $# -ne 1 ]
then
  echo "Correct syntax is: $0 file"
  exit 1
fi


check_file $1
file $1       # gives the type of file given in arg $1
exit 0

# check with cmd below:
# if ./deb10_exit.sh ; then echo vrai ; else echo faux ; fi 
# if ./deb10_exit.sh /etc/passwords ; then echo vrai ; else echo faux ; fi 
# if ./deb10_exit.sh /etc/passwd ; then echo vrai ; else echo faux ; fi 

