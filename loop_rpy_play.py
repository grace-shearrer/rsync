# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 17:35:06 2014

@author: everyonelovesacatholicgirl
"""

#!/usr/bin/python
#mean groups based on participant ID

import pandas as pd
import numpy as np
import os
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
import glob

stats = importr('stats')
base = importr('base')

os.chdir('/Users/everyonelovesacatholicgirl/Desktop/testtest/data_w_headers')

allFiles=glob.glob("*.txt")

for files in allFiles:
    df=pd.read_table(files)
    df.reset_index()
    daya4=df.groupby(['Participant ID'])
    data5=daya4.aggregate(np.sum)
    data5.to_csv(files+'.csv', sep=",")
    print(files+'.csv')




print(ro.r('fame <-read.table("totals_foods.txt.csv", sep=",", header=T)'))

print(ro.r('nutrient<-read.table("totals_nutrients.txt.csv", sep=",", header=T)'))

ro.r('fame<-transform(fame, fruit=FRU0100+FRU0300+FRU0400+FRU0500)')##fruit

ro.r('fame<-transform(fame, veggeies=VEG0100+VEG0200+VEG0300+VEG0600)')##veggies

ro.r('fame <- transform(fame, starchveggies = VEG0400 + VEG0450)')##starch veg

ro.r('fame <- transform(fame, fries = VEG0800)')##fried

ro.r('fame <- transform(fame, wholegrain = GRW0100+GRW0200+GRW0300+GRW0400+GRW0500+GRW0600+GRW0900)')#NO SWEET CEREAL OR COOKIES AND CAKES whole grain

ro.r('fame<-transform(fame, somewholegrain=GRS0100+GRS0200+GRS0300+GRS0400+GRS0500+GRS0600+GRS0900)')#no cereal, cookies, cakes some whole grain

ro.r('fame<-transform(fame, refinedgrain=GRR0100+GRR0200+GRR0300+GRR0400+GRR0500+GRR0600+GRR0900)')##refined, no cereal, cookies, cakes

ro.r('fame<-transform(fame, sweetcereal=GRW0700+GRS0700+GRR0700)') ##sweet cereal

ro.r('fame<-transform(fame, sweetbakedgoods=GRW0800+GRS0800+GRR0800)')## sweet baked goods

ro.r('fame<-transform(fame, snackbars=GRW1000+GRS1000+GRR1000)') ##snack bars

ro.r('fame<-transform(fame, popcorn=GRW1100+GRW1200)')##popcorn

ro.r('fame<-transform(fame, meat=MRF0100+MRF0200+MRF0300+MRL0300+MRF0400+MRL0400+MCF0200+MCL0200+MRF0500+MPF0100+MFF0100+MFL0100+MSL0100+MCF0100+MCL0100+MOF0100+FMC0200+MOF0300)')##normal meat

ro.r('fame<-transform(fame, friedmeat=MFF0200+MSF0100+MPF0200)')##fried meat

ro.r('fame<-transform(fame, nuts=MOF0500+MOF0600)') ##nuts

ro.r('fame<-transform(fame, fakemeat=MOF0700)')## fake meat

ro.r('fame<-transform(fame, milk=DMF0100+DMR0100+DML0100+DMN0100)') #white milk

ro.r('fame<-transform(fame, flavoredmilk=DMF0200+DMR0200+DML0200+DML0300)') #sweet milk

ro.r('fame<-transform(fame, cheese=DCF0100+DCR0100+DCL0100+DCN0100)')## cheese

ro.r('fame<-transform(fame, sweetyogurt=DYF0100+DYR0100+DYL0100)')## sweetyogurt

ro.r('fame<-transform(fame, yogurt=DYF0200+DYR0200+DYL0200+DYN0100)')##plain yogurt

ro.r('fame<-transform(fame, deserts=DOT0100+DOT0200+DOT0300+SWT0400+SWT0500+SWT0700+SWT0800+SWT0200+SWT0300+MSC0600)')## deserts

ro.r('fame<-transform(fame,cream=FCF0100+FCR0100+FCN0100)')## cream

ro.r('fame<-transform(fame, fats=FMF0100+FMR0100+FOF0100+FAF0100+FSF0100+FAR0100+FDF0100+FDR0100)') ##fats

ro.r('fame<-transform(fame, SSB=BVS0400+BVS0300+BVS0500+BVS0100+BVS0200+BVS0600)') ##SSB

ro.r('fame<-transform(fame, artSSB=BVA0400+BVU0300+BVA0300+BVA0500+BVU0400+BVA0100+BVA0200+BVU0200+BVA0600+BVU0500)') ##artifical SSB

ro.r('fame<-transform(fame, condiments=MSC0200+MSC0300+MSC0400)') ##condiments


###SSB categories one####
ro.r('fame$ssbcat[fame$SSB<1]<-0') #low
ro.r('fame$ssbcat[fame$SSB>=1 & fame$SSB<2]<-1') #med
ro.r('fame$ssbcat[fame$SSB>=2]<-2') #high

####alternate SSB cats#####
ro.r('fame$ssbcat2[fame$SSB==0]<-0')
ro.r('fame$ssbcat2[fame$SSB>0 & fame$SSB<=1]<-1')
ro.r('fame$ssbcat2[fame$SSB>1 & fame$SSB<=2]<-2')
ro.r('fame$ssbcat2[fame$SSB>2  & fame$SSB<=3]<-3')
ro.r('fame$ssbcat2[fame$SSB>3]<-4')


print(ro.r('(fame$ssbcat)'))

ro.r('write.table(fame, "calculated_foods.csv", sep=",", row.names=FALSE)')
ro.r('write.table(nutrient, "calc_nut.csv", sep=",", row.names=FALSE)')


df1=pd.read_table("calculated_foods.csv", sep=",")
df2=pd.read_table("calc_nut.csv", sep=",")
s1 = pd.merge(df1, df2, how='left', on=['Participant.ID'])
s1.to_csv("total_calc.csv")




