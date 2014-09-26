import os
import fnmatch
import sys

def find_template(basedir,sub, fsfdir):
  os.chdir(basedir + sub + fsfdir)
  print os.getcwd()
  templatedir=os.getcwd()
  
def create_template(basedir,sub,fsfdir,targetfile):
  for file in os.listdir('.'):
    if fnmatch.fnmatch(file,targetfile):
      filename=[targetfile]
      with open(basedir + sub + fsfdir + targetfile,'r') as infile:
        text=infile.read()  
	with open(basedir + '/scripts/fsf_templates/level1/design_wtp_lev1template.fsf','w') as outfile:
	  outfile.write(text)
	  #for line in infile:
	  os.chdir(basedir + '/scripts')

def main ():
  
  check_args=1
  if len(sys.argv)<2:
    print('usage: need to specify subject on which to run analysis')
    sys.exit()
  elif check_args==1:
    sub=sys.argv[1]

#Global variables
  basedir='/corral-repl/utexas/poldracklab/data/sugar_brain/'
  fsfdir='/model/run001.feat/'
  targetfile='design.fsf'

#Functions to be called
  find_template(basedir,sub,fsfdir)
  create_template(basedir,sub,fsfdir,targetfile)

main()
