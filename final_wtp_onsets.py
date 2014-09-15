#!/usr/bin/python
#get onsets food photos


import numpy
import glob
import os

os.chdir('/Users/everyonelovesacatholicgirl/Desktop/onsets/')

f=glob.glob('*.txt')

handles=[]
bids=[]
onsets=[]
rt=[]

for l in f:
    handles.append(open(l))  

path='/Users/everyonelovesacatholicgirl/Desktop/onsets/output'
if not os.path.exists(path):
    os.makedirs(path, 0755)

os.chdir(path)
    
for logfile_handle in handles:
    bids=[]
    onsets=[]
    rt=[]    
    
    for x in logfile_handle.readlines()[1:]:
        l_s=x.strip().split()
        bids.append(float(l_s[5]))
        onsets.append(float(l_s[3]))
        rt.append(float(l_s[6]))    
        
    base_filename=logfile_handle.name.split('.')[0]    
    onsets=numpy.array(onsets)    
   
    
    meanrt=numpy.mean(rt)
    meanbids=numpy.mean(bids)
    #miss=onsets[onsets==float(999)]   
    
    f_task=open('ons_task_'+base_filename+'.txt', 'w')
    f_bids=open('ons_bids_'+base_filename+'.txt', 'w')
    f_rt=open('ons_rt_.'+base_filename+'.txt', 'w')
    #f_miss=open('ons_miss_'+base_filename+'.txt', 'w')   
    
    for t in range(len(bids)):
        f_task.write('%f\t4\t1\n' %onsets[t])
        f_bids.write('%f\t4\t%f\n' %(onsets[t], bids[t]))
        f_rt.write('%f\t4\t%f\n' %(onsets[t], rt[t]))
        #f_miss.write('%f\t4\t%f\n' %(miss[t]))  

    f_task.close()    
    f_bids.close()
    f_rt.close()
    #f_miss.close()
    
     
    







