#!/bin/bash
# join.sh

echo 'join tele noms' > NDT
join tele noms >> NDT            # only common entries
echo -e '\njoin -a1 -a2 tele noms' >> NDT
join -a1 -a2 tele noms >> NDT   # any entries even uncommon from file 1 & 2
echo -e '\njoin -a1 -a2 -o 2.3,0,1.2 tele noms ' >> NDT
join -a1 -a2 -o 2.3,0,1.2 tele noms >> NDT   # any entries -o format with a2/col3 0 common a1/col2 

cat NDT