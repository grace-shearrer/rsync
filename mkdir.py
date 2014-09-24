import os
import glob

def make_tastedir(basedir, subdir, tastedir):
    os.chdir(basedir)
    for name in glob.glob(basedir+subdir):
        if not os.path.exists(name+tastedir):
            os.mkdir(name+tastedir, 0775)
def make_wtpdir(basedir, subdir, wtpdir):
    os.chdir(basedir)
    for name in glob.glob(basedir+subdir):
        if not os.path.exists(name+wtpdir):
            os.mkdir(name+wtpdir, 0775)

def main():
    basedir='/Users/liquid/Desktop/test'
    subdir='/sb_00[0-5]*'
    tastedir='/taste'
    wtpdir='/wtp'
    make_tastedir(basedir, subdir, tastedir)
    make_wtpdir(basedir, subdir, wtpdir)
main()
