import sys
import glob
import os
from subprocess import check_output

#Opens the template files, reads in, changes dictionary variables, writes out as design.fsf file
def create_fsf(basedir,sub,templatesdir,targetfile,repl_dict): 
  with open(basedir + templatesdir + targetfile,'r') as infile:
    tempfsf=infile.read()
    for key in repl_dict:
      tempfsf = tempfsf.replace(key, repl_dict[key])
      with open(basedir + sub + '/model/Lev2/wtp_design_lev2.fsf','w') as outfile:
	outfile.write(tempfsf)
	os.chdir(basedir + templatesdir)

def main ():
#input subject id to be run; this will generate an error message if no subject id is given
  check_args=1
  if len(sys.argv)<2:
    print('usage error: must specify subject on which to run analysis')
    sys.exit()
  elif check_args==1:
    sub=sys.argv[1]

#Global variables
  basedir='/corral-repl/utexas/poldracklab/data/sugar_brain/'
  targetfile='design_wtp_lev2template.fsf'
  templatesdir='scripts/fsf_templates/level2/'
  repl_dict={'SUBNUM':sub}

#Function to be called 
  create_fsf(basedir,sub,templatesdir,targetfile,repl_dict) 
main()
