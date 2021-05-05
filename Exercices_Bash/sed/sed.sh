#!/bin/bash
# sed.sh
# sed -e --> commande uniligne
# sed -f fichier --> passage de commande par un script
# sed -i --> modifie directement le fichier source au lieu de rediriger vers la sortie standard

# sed d delete
echo "sed \"1d;4d\" test.txt //delete line n° sep ;"
sed "1d;4d" test.txt
echo -e "\n\nsed \"2,4d\" test.txt //delete line n° interval ,"
sed "2,4d" test.txt
echo -e "\n\nsed \"/^#/d\" test.txt //delete with regexp"
sed "/^#/d" test.txt
echo -e "\n\nsed \"/^#/,/_/d\" test.txt // del regexp interval ,"
sed "/^#/,/_/d" test.txt 

# sed -n filter/mask all // p print
echo -e "\n\nsed -n 1p test.txt //-n filter, print line n°"
sed -n 1p test.txt
echo -e "\nsed -n \"/^#/p\" test.txt //-n filter, print with regexp"
sed -n "/^#/p" test.txt

# sed s/ / / Substitution
echo -e "\nsed \"s/Voilà/Voicicici/\" test.txt //s Subst orig/new"
sed "s/Voilà/Voicicici/" test.txt | sed -n 1p

# sed y/ / / Transliteration
echo -e "\nsed \"y/éèëê/eeee/\" test.txt //y Transliterate éèëê to e"
sed "y/éèëê/eeee/" test.txt | sed -n 1p

# Group cmd {}
echo -e "\nsed \"1,2 {y/éèëê/eeee/;s/ceci/celalala/}\" test.txt //Concerned line n°, then group cmd {}"
sed "1,2 {y/éèëê/eeee/;s/ceci/celalala/}" test.txt | sed -n 1,3p

echo -e "\nRenaming files"
for file in man min mon mun; do fn="$(echo $file | sed s/m/yoda_/)"; echo "$fn"; done
echo -e "\nV2 //\"\${string//old/new}\" for replacement!"
for file in man min mon mun; do fn="${file//m/yoda_}"; echo "$fn"; done

echo -e "\nReplacing txt in files /-i interract in file /.bak backup copy"
$ for f in *.php; do sed -i.bak -e 's/ancienne-adresse/nouvelle-adresse/' "$f"; done
