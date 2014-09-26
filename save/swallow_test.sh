#!/bin/sh

cd /corral-repl/utexas/poldracklab/data/sugar_brain/onset_logs/sb_0012


arr=($(find . -name 'swallow*'))
echo ${arr[@]}

for x in ${arr[@]}
do 
    cd /corral-repl/utexas/poldracklab/data/sugar_brain/onset_logs/sb_0012
    sed '1d' $x > $x.tmp
    mv $x.tmp $x
    echo "swallow line removed from $x"
done
