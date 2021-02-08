#! /bin/bash


appreciation ()
{
if [ $NOTE -ge 16 ]
then
    echo "très bien!"
elif [ $NOTE -ge 14 ]
then
    echo "bien."
elif [ $NOTE -ge 12 ]
then
    echo "passable..."
elif [ $NOTE -ge 10 ]
then
    echo "bof."
else
    echo "c'est nul!"
fi 
}

# clear
if [ $# -ne 0 ]
then
    NOTE=$1
else
    read -p "Entrez une note /20: " NOTE
fi

appreciation
