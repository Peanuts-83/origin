#! /bin/sh

numero=1

for fic in *
do
	echo "$numero) $fic"
	numero=$((numero + 1))
done
