#! /bin/bash

# ./ftpauto.sh ftp.lip6.fr pub/linux/french/docs man-fr*
# paramétrage du transfert désiré
MACHINE=${1:?Pas de machine indiquée}
CHEMIN=${2:?Pas de chemin indiqué}
FICHIERS=${3:?Pas de fichiers indiqués}

LOGIN=${4:-anonymous}
PASSWORD=${5:-$USER@$HOSTNAME}

# sauvegarde de l'éventuel fichier ~/.netrc
if [ -f ~/.netrc ] ; then
  mv ~/.netrc ~/.netrc.back
fi

#création d'un nouveau .netrc avec les infos pour la connexion voulue
ANCIEN_UMASK=$(umask)
umask 0177
echo machine $MACHINE > ~/.netrc
echo login $LOGIN >> ~/.netrc
echo password $PASSWORD >> ~/.netrc
umask $ANCIEN_UMASK

# lancer la connexion
ftp <<- FIN
  open $MACHINE
  bin
  prompt
  cd $CHEMIN
  mget $FICHIERS
  quit
FIN

# effacer .netrc et récupérer l'ancien
rm - ~/.netrc
if [ -f ~/.netrc.back ] ; then
  mv ~/.netrc.back ~/.netrc
fi
