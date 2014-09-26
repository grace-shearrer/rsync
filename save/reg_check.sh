outputdir='/corral-repl/utexas/poldracklab/data/sugar_brain/sb_mock_02/model/reg_check_results'
#delete if there is an old version
mkdir $outputdir
rm  $outputdir/reg_check_results.html

for subnum in sb_mock_02
do

for i in food001+.feat food002.feat taste001.feat 

do

dirpth=/corral-repl/utexas/poldracklab/data/sugar_brain/$subnum/model/${i}/

echo '<p>============================================
<p> Registration for analysis in '$dirpth'

<p>Summary registration, FMRI to standard space<br><IMG BORDER=0 SRC='$dirpth'reg/example_func2standard1.png WIDTH=100%>
</BODY></HTML>' >> $outputdir/reg_check_results.html


done
done
