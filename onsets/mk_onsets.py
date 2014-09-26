import os
import numpy

f=open('/corral-repl/utexas/poldracklab/data/sugar_brain/SB_test1/behav/food/foodons/Onsetsbmock2_BDM1_09-May-2014_19h12m.txt')

legend=f.readline()
lines=f.readlines()
f.close()

bids=[]
onsets=[]
rt=[]

for l in lines:
    l_s=l.strip().split()
    bids.append(int(l_s[5]))
    onsets.append(float(l_s[3]))
    rt.append(float(l_s[6]))

meanrt=numpy.mean(rt)
meanbid=numpy.mean(bids)

f_task=open('ons_task.txt','w')
f_bid=open('ons_bid.txt','w')
f_rt=open('ons_rt.txt','w')

for t in range(len(bids)):
    f_task.write('%f\t3\t1\n'%onsets[t])
    f_bid.write('%f\t3\t%f\n'%(onsets[t],bids[t] - meanbid))
    f_rt.write('%f\t3\t%f\n'%(onsets[t],rt[t] - meanrt))

f_task.close()
f_bid.close()
f_rt.close()

