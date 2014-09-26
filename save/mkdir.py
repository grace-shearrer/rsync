import os
import glob

def make_dir_taste(basedir, subdir, tastedir):
  os.chdir(basedir)
  for name in glob.glob(basedir+subdir+tastedir):
    if not os.path.exists(name+'/ica'):
      os.mkdir(name+'/ica', 0775)

def make_dir_wtp(basedir, subdir, wtpdir):
  os.chdir(basedir)
  for name in glob.glob(basedir+subdir+wtpdir):
    if not os.path.exists(name+'/ica'):
      os.mkdir(name+'/ica', 0775)

def main():
  basedir='/corral-repl/utexas/poldracklab/data/sugar_brain/'
  subdir='/sb_00[0-5]*'
  tastedir='/model'
  wtpdir='/model'
  make_dir_taste(basedir, subdir, tastedir)
  make_dir_wtp(basedir, subdir, wtpdir)
main()
