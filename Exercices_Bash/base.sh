#!/bin/bash
# script bash non fonctionnel >> dos2unix nom.sh

# if then else // -n chaine non vide
echo '$0 cript name /$1 1rst arg /$# numb of args /$@ all args /-n not empty'
if [[ -n $1 ]]; then LOGIN=$1 ; else LOGIN=$USER ; fi
echo "Bonjour $LOGIN"

# $0 cmd name / $# param numb / $@ params
echo "La commande $0 a $# parametres qui sont : $@"

# tr
echo -e "\ntr //upper to lower case"
string="ARMISTICE FACOS MILITANT DAGES"
echo $string | tr '[:upper:]' '[:lower:]' 