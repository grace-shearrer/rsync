#!/usr/bin/env python
"""
process data for sugar_brain study

USAGE: process_data.py subcode

"""

import os,sys
#from run_shell_cmd import *
from subprocess import call

subcode=sys.argv[1]
if len(sys.argv)>3:
    username=sys.argv[2]
    password=sys.argv[3]
else:
    username=None
    password=None


subdir=int(subcode.split('_')[-1])
#subdir='sugar_brain'

tmpdir='/corral-repl/utexas/poldracklab/data/selftracking/tmpscripts/'

#cd /corral-repl/utexas/poldracklab/data/${STUDYNAM

SETUP_SUBJECT='/corral-repl/utexas/poldracklab/software_lonestar/setu p-subject/setup_subject.py'
SETUP_SUBJECT='/corral-repl/utexas/poldracklab/software_lonestar/local/bin/setup_subject.py'

if username==None or password==None:
    cmd='%s --getdata --studyname sugar_brain -s %s --subdir sb_%003d'%(SETUP_SUBJECT,subcode,subdir)
else:
    cmd='%s --getdata --studyname sugar_brain -s %s --subdir sb_%003d --xnat_username %s --xnat_password %s'%(SETUP_SUBJECT,subcode,subdir,username,password)

    
print cmd
call(cmd.split(' '))

scriptfile=os.path.join(tmpdir,'setup_%d.sh'%subdir)
f=open(scriptfile,'w')
f.write('%s -o --dcm2nii --motcorr --qa  --betfunc --fm --fsrecon --keepdata --studyname sugar_brain --subcode %s --subdir sb_%03d\n'%(SETUP_SUBJECT,subcode,subdir))
f.close()

cmd='launch -s %s -p 24 -q largemem -r 10:00:00 -n stsetup_%d'%(scriptfile,subdir)
print cmd
call(cmd.split(' '))
