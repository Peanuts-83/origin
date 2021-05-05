#! /bin/bash

NOTE=0
MOY=0
I=0

while [ $NOTE -ge 0 ]
do
    read -p "Saisissez une note /20 (q pour quitter): " NOTE
    if [ $NOTE = "q" ]
    then
        let NOTE=-1
        echo "Au revoir."
    elif [ $NOTE -ge 16 ]
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
    ((I++))
    let MOY=$MOY+$NOTE
done

if [ $I -eq 0 ]
then
    $I=1
elif [ $I -gt 0 ]
then
    let I=$I-1
fi

if [ $I -gt 0 ]
then
    if [ $NOTE -lt 0 ]
    then    
        let MOY=($MOY-$NOTE)/$I
        echo "La moyenne des notes est $MOY ($I notes)."
    else
        let MOY=$MOY/$I
        echo "La moyenne des notes est $MOY ($I notes)."
    fi
fi