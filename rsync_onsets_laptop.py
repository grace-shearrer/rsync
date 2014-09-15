import os

def rsync_onsets(src_path, user, ID, date):
    os.chdir(src_path)
    os.system('rsync -rtvx'+' '+ID+'_'+date+'*.log '+user+'@poldrack.lonestar.tacc.utexas.edu:/corral-repl/utexas/poldracklab/data/sugar_brain/onset_logs/'+ID)


def main():
    #defines TACC login by prompting user input
    user = raw_input('Please enter you TACC login ID: ')

    #defines subject ID by prompting user input
    ID = raw_input ('Please enter the subjet\'s ID: ')

    #defines date attached to file name by prompting user input
    date = raw_input ('Please enter the date the subject was run, format: yyyy-mm-dd: ')

    #defines source path of files to be copied
    src_path = 'CHANGE PATH'

    #functions to be called
    rsync_onsets(src_path, user, ID, date)
main()
