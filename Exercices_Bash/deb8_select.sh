#! /bin/bash

# Select : menu selection usefull for user interface
# Function that takes a filename in arg, and gives choice of all possible actions on it

# function action_file() first
action_file () {
  # localize vars in case existing vars with same name 
  local answer
  local entry

  echo "***********************************************"
  # initialise PS3 
  PS3="Action sur $1 : "

  select answer in Info Copy Move Remove Back
  do
    case $answer in 
      Info )
        echo
        ls -l "$1"
        echo ;;
      Copy )
        echo -n "Copy $1 to wich path? "
        if ! read entry ; then continue ; fi  # tempo waiting for user
        cp "$1" "$entry" ;;
      Move )
        echo -n "Move $1 to which path? "
        if ! read entry ; then continue ; fi  # tempo waiting for user
        mv "$1" "$entry"
        break ;;                              # break because file is gone / go out of loop
      Remove )
        if rm -i "$1" ; then break ; fi            # rm -i for prompt before removal / then break (no more file)
        ;;
      Back )
        break
        ;;
      * )
        if [ "$REPLY" = "0" ] ; then break ; fi     # entry stays empty, but value goes in special var '$REPLY'
        echo "$REPLY n'est pas une entrée valide."
        echo ;;
    esac
  done
}

# function list_files() which calls action_file()
list_files () {
  echo "***********************************************"
  # [ -z $rep ] && echo "Sélectionnez un répertoire de travail: " ; read rep
  # echo "rep: $rep"
  echo "==> Entrez '0' pour Quitter <=="
  PS3="Sélectionnez un fichier : "
  select file in *
  do
    if [ ! -z "$file" ] ; then action_file "$file" ; return 0 ; fi
    if [ "$REPLY" = "0" ] ; then return 1 ; fi
    echo
  done
}

# loop till function is ok
# ':' after 'do' means wait
while list_files ; do : ; done
