
import numpy


f=open('test_2014-06-12-08_57_52_subdata.log')

onsets=[]
conds=[]
#onsets are the times
#condvals are the pics
#juice is onsets and juice in general

for l in f.readlines():
    if l.find('Level Condition')>-1:
        l_s=l.strip().split()
        onsets.append(float(l_s[0]))
        conds.append(int(l_s[3]))
    if l.find('Key pressed: 5')>-1:
        l_s=l.strip().split()
        start_time=float(l_s[0])

f_task=open('ons_task857.txt','w')
f_swallow=open('ons_swallow857.txt','w')
f_rinse=open('ons_rinse857.txt','w')
f_waterwater=open('ons_waterwater857.txt','w')
f_juicejuice=open('ons_juicejuice857.txt','w')
f_juicewater=open('ons_juicewater857.txt','w')
f_waterjuice=open('ons_waterjuice857.txt','w')

onsets=numpy.array(onsets)-start_time


#swallows
swallow=onsets-9



#rinse
rinse=onsets-7


condvals=numpy.array(conds)/2

#juice=numpy.zeros(len(conds))
#juice[numpy.array(conds)==1]=1
#juice[numpy.array(conds)==2]=1
#juice[numpy.array(conds)==3]=0
#juice[numpy.array(conds)==0]=0

#see water get water
water_water=numpy.zeros(len(conds))
water_water[numpy.array(conds)==0]=1
                         

#see juice and get juice
juice_juice=numpy.zeros(len(conds))
juice_juice[numpy.array(conds)==2]=1
                          


#see juice get water
juice_water=numpy.zeros(len(conds))
juice_water[numpy.array(conds)==3]=1


#see water get juice
water_juice=numpy.zeros(len(conds))
water_juice[numpy.array(conds)==1]=1




#change the 3 here
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





   
       
