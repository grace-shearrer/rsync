#!/bin/sh

cd /corral-repl/utexas/poldracklab/data/sugar_brain/onset_logs/sb_0012


arr=($(find . -name 'rinse*'))
echo ${arr[@]}

for x in ${arr[@]}
do 
    cd /corral-repl/utexas/poldracklab/data/sugar_brain/onset_logs/sb_0012
    sed '1d' $x > $x.tmp
    mv $x.tmp $x
    echo "rinse line removed from $x"
done
