#!/bin/sh
#cleaning onsets
cd /corral-repl/utexas/poldracklab/data/sugar_brain/onset_logs/sb_0012/

FILES=/corral-repl/utexas/poldracklab/data/sugar_brain/onset_logs/sb_0012/*

for x in $FILES
do
	echo "start process"
        cd /corral-repl/utexas/poldracklab/data/sugar_brain/onset_logs/sb_0012/
        echo 'run' $x
	test -f "$x" || continue
	echo "Replacing on : $x"
	sed '/0$/d' $x > $x.tmp
	mv $x.tmp $x
	echo "Replacement done on : $x"
	echo "process done"
done 

arr=($(find . -name 'swallow*'))
echo ${arr[@]}

for x in ${arr[@]}
do 
    cd /corral-repl/utexas/poldracklab/data/sugar_brain/onset_logs/sb_0012
    sed '1d' $x > $x.tmp
    mv $x.tmp $x
    echo "swallow line removed from $x"
done

arr=($(find . -name 'rinse*'))
echo ${arr[@]}

for x in ${arr[@]}
do 
    cd /corral-repl/utexas/poldracklab/data/sugar_brain/onset_logs/sb_0012
    sed '1d' $x > $x.tmp
    mv $x.tmp $x
    echo "rinse line removed from $x"
done
