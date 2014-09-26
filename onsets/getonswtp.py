
import numpy

f=open('/corral-repl/utexas/poldracklab/data/sugar_brain/scripts/onsets/Onsetsbmock2_BDM2_09-May-2014_19h27m.txt')


legend=f.readline()
lines=f.readlines()
f.close()

bids=[]
onsets=[]
rt=[]

for l in lines:
    l_s=l.strip().split()
    bids.append(float(l_s[5]))
    onsets.append(float(l_s[3]))
    rt.append(float(l_s[6]))



meanrt=numpy.mean(rt)
meanbids=numpy.mean(bids)
#miss=onset[onset[:,2]==999.9999]

##indicate run###
f_task=open('ons_task_0.txt', 'w')
f_bids=open('ons_bids_0.txt', 'w')
f_rt=open('ons_rt_0.txt', 'w')
#f_miss=open('miss_wtp_0.txt', 'w')



for t in range(len(bids)):
    f_task.write('%f\t4\t1\n' %onsets[t])
    f_bids.write('%f\t4\t%f\n' %(onsets[t], bids[t]))
    f_rt.write('%f\t4\t%f\n' %(onsets[t], rt[t]))
    #f_miss.write('%f\t4\t%f\n' %(miss[t])

f_task.close()
f_bids.close()
f_rt.close()
#f_miss.close()


