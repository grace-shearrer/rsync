import sys
import os
import fnmatch
import subprocess

def rmv_zeros(basedir,sub,ons_type):
  os.chdir(basedir+sub+ons_type)
  print "start process"
  for file in os.listdir('.'):   
    if fnmatch.fnmatch(file,'*.txt'):
      out_file=open('./clean/'+file,'w')
      subsed=subprocess.call(['sed','/0$/d',file], stdout=out_file)
      out_file.close()

def mv_orig_ons():
  submv=subprocess.call('mv *.txt orig_ons', shell=True)
  print 'end process'

def main():
  check_args=1
  if len(sys.argv)<2:
    print('usage error: must specify subject id')
    sys.exit()
  elif check_args==1:
    sub=sys.argv[1]
  basedir='/corral-repl/utexas/poldracklab/data/sugar_brain/onset_logs/'
  ons_type='/taste'
  
  #functions to be called
  rmv_zeros(basedir,sub,ons_type)
  mv_orig_ons()
main()
