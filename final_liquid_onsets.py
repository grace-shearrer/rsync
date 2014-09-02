#!/usr/bin/python
#get onsets


import numpy
import glob
import os

os.chdir('/Users/everyonelovesacatholicgirl/Desktop/onsets/')

f=glob.glob('*.log')


onsets=[]
conds=[]
handles=[]
#onsets are the times
#condvals are the pics
#juice is onsets and juice in general
#f is a list of log files

for l in f:
    handles.append(open(l))  
  #l is a log file in f  
#handles is a list of the logfiles  \
debug_flag = False
path='/Users/everyonelovesacatholicgirl/Desktop/onsets/output'

if not os.path.exists(path):
    os.makedirs(path, 0755)

os.chdir(path)

for logfile_handle in handles:
    onsets = []
    conds = []
    start_time = None
    for x in logfile_handle.readlines():
        
        if x.find('Level Condition:')>-1:
            l_s=x.strip().split()
            onsets.append(float(l_s[0]))
            conds.append(int(l_s[3]))
            
        if x.find('Key pressed: 5')>-1:
            l_s=x.strip().split()
            start_time=float(l_s[0])
            

    base_filename=logfile_handle.name.split('.')[0]
    
    onsets=numpy.array(onsets)-start_time
    
    print 'onsets is '+str(onsets)
    print 'start time is ' + str(start_time)
    print 'onsets changed to ' +str(onsets)
    
   
    rinse=onsets-7
    condvals=numpy.array(conds)/2
    water_water=numpy.zeros(len(conds))
    water_water[numpy.array(conds)==0]=1
    juice_juice=numpy.zeros(len(conds))
    juice_juice[numpy.array(conds)==2]=1
    juice_water=numpy.zeros(len(conds))
    juice_water[numpy.array(conds)==3]=1
    water_juice=numpy.zeros(len(conds))
    water_juice[numpy.array(conds)==1]=1
    swallow=onsets-9 
    
    f_waterwater = open('water_water_' + base_filename+'.txt', 'w')
    f_juicejuice =open('juice_juice_'+base_filename+'.txt', 'w')
    f_waterjuice=open('water_juice'+base_filename+'.txt', 'w')
    f_juicewater=open('juice_water'+base_filename+'.txt', 'w')
    f_task=open('task'+base_filename+'.txt', 'w')
    f_swallow=open('swallow'+base_filename+'.txt', 'w')
    f_rinse=open('rinse'+base_filename+'.txt', 'w')
    
    for t in range(len(onsets)):
        f_task.write('%f\t2\t1\n' %onsets[t])
        f_swallow.write('%f\t2\t1\n' %swallow[t])
        f_rinse.write('%f\t2\t1\n' %rinse[t])
        f_juicejuice.write('%f\t2\t%d\n' %(onsets[t], juice_juice[t]))    
        f_waterwater.write('%f\t2\t%d\n' %(onsets[t], water_water[t]))
        f_juicewater.write('%f\t2\t%d\n' %(onsets[t], juice_water[t]))
        f_waterjuice.write('%f\t2\t%d\n' %(onsets[t], water_juice[t]))
    f_task.close()
    f_swallow.close()
    f_rinse.close()
    f_juicejuice.close()
    f_waterwater.close()
    f_juicewater.close()
    f_waterjuice.close()
    
    
    
            
     
 
 
 #proper syntax is string.format(stuff)
            #eg '{0} will replace {1}'.format(arg0, arg1)