import sys
import glob
import os
from subprocess import check_output

def create_fsf(basedir,sub,templatesdir,targetfile,repl_dict):
#Find the functional run directories and create variable to use as name for output file and add variable to dictionary
  for name in glob.glob(basedir + sub + '/BOLD/liquid_run*'):
    funcrun=name
    #print funcrun
    funcrun=funcrun.lstrip(basedir + sub)
    funcrun=funcrun.lstrip('BOLD/')
    #print funcrun
    repl_dict.update({'FUNCRUN':funcrun})
    #print repl_dict

#Find the number of timepoints for each functional run (need to change to that directory to find bold file) and set as variable to add to dictionary
    os.chdir(name)
    ntmpts=check_output(['fslnvols','bold.nii.gz'])
    #print ntmpts
    repl_dict.update({'NTIMEPOINTS':ntmpts})

#Opens the template files, reads in, changes dictionary variables, writes out as design.fsf file 
    with open(basedir + templatesdir + targetfile,'r') as infile:
      tempfsf=infile.read()
      for key in repl_dict:
        tempfsf = tempfsf.replace(key, repl_dict[key])
	with open(basedir + sub + '/model/liquid_design_' + funcrun + '.fsf','w') as outfile:
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
  targetfile='design_liquid_lev1template.fsf'
  templatesdir='scripts/fsf_templates/level1/'
  repl_dict={'SUBNUM':sub}

#Function to be called 
  create_fsf(basedir,sub,templatesdir,targetfile,repl_dict) 
main()
