import sys
import glob
import os
import shutil

def create_regdir(basedir,sub,regdir):
#
  outputdir= basedir + sub + '/model'
  for name in glob.glob(outputdir): 
    if os.path.exists(regdir + 'reg_check_results.html'):
      shutil.rmtree(regdir)
    os.makedirs(regdir)


def main ():
#input subject id to be run; this will generate an error message if no subject id is given
  check_args=1
  if len(sys.argv)<2:
    print('usage error: must specify subject for which to create registration plots')
    sys.exit()
  elif check_args==1:
    sub=sys.argv[1]

#Global variables
  basedir='/corral-repl/utexas/poldracklab/data/sugar_brain/'
  regdir='reg_check_results'
  #templatesdir='scripts/fsf_templates/level2/'
  repl_dict={'SUBNUM':sub}

#Function to be called 
  create_regdir(basedir,sub,regdir) 
main()
