# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:50:49 2020

@author: Ahsan Rahim
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:27:05 2020

@author: Ahsan Rahim
"""


import numpy as np
import pandas as pd
from math import floor
from queue import Queue 
  

q1 = list()
q2 = list()
q3 = list()
  

class Job:
    def __init__(self, iat, st):
        self.iat=iat
        self.at=0
        self.wt=0
        self.tas=0
        self.server=0;
        self.st=st
        self.dt=0
        self.QL=0
        self.RavgWT=0;
        self.RavgDT=0;
        self.RavgQL=0;

j1=Job(0,floor(np.random.random()*10))

#servers=[Job , Job , Job]

servers=[[] , [] , []]



jobList =[j1]
for i in range(20):
    #Change input parameters to increase/change iat and st of jobs
    jobList.append(Job(floor(np.random.random()*10),floor(np.random.random()*50)))



jobList[0].at = jobList[0].tas = 1
jobList[0].wt = jobList[0].QL = 0
jobList[0].dt = jobList[0].st
jobList[0].RavgWT= jobList[0].wt;11
jobList[0].RavgDT= jobList[0].dt;
jobList[0].RavgQL= jobList[0].QL;
jobList[0].server=1;
servers[0].append(jobList[0]);


def RavgWT(x):
    sum=0;
    for i in range(0 , x+1):
       sum=sum+jobList[i].wt; 
     
    return sum/(x+1); 


def RavgDT(x):
    sum=0;
    for i in range(0 , x+1):
       sum=sum+jobList[i].dt; 
     
    return sum/(x+1); 


def RavgQL(x):
    sum=0;
    for i in range(0 , x+1):
       sum=sum+jobList[i].QL; 
     
    return sum/(x+1); 






def emptyServe( j ,  i):
    j.at=jobList[i-1].at + j.iat;
    j.tas=j.at;
    j.dt=j.tas+j.st
    j.QL=0;
    j.server=i+1;
    j.RavgWT=RavgWT(i);
    j.RavgDT=RavgDT(i);
    j.RavgQL=RavgQL(i);



def releaseQueue(at):
    for i in range(3):
        for j in servers[i]:
            if j.dt<=at:
                servers[i].remove(j)
                            
                    
    

def secondServer(j , i , minimum):
    j.at=jobList[i-1].at + j.iat;
    releaseQueue(j.at)
    j.QL= len(servers[minimum])
    
    if(len(servers[minimum])==0):
        j.tas=j.at;
    else:
        j.tas= max(j.at, servers[minimum][len(servers[minimum])-1].dt);
    j.server=minimum+1;
    j.wt=j.tas-j.at;
    j.dt=j.tas +j.st;
    j.RavgWT=RavgWT(i);
    j.RavgDT=RavgDT(i);
    j.RavgQL=RavgQL(i);
    servers[minimum].append(j)
    
def minServer():
    x=0
    for i in range(1,3):
        
        if servers[i][len(servers[i])-1].dt < servers[x][len(servers[x])-1].dt:
            x=i;
    return x;

def checkEmptyServer():
    
    for i in range(len(servers)):
        if len(servers[i])==0:
            return True;
    return False;

def emptyServerIndex():
    for i in range(len(servers)):
        if len(servers[i])==0:
            return i;
    return -1;



for i in range(1,len(jobList)):
        
        if checkEmptyServer()==True:
            
            servers[emptyServerIndex()].append(jobList[i])
            emptyServe(jobList[i],i)
               
        else:    
            x=minServer();
            secondServer(jobList[i], i ,x);
        
        
        

df = pd.DataFrame( columns=['iat', 'at', 'wt', 'tas' , 'server' , 'st' , 'dt' ,'QL', 'RavgWT', 'RavgDT', 'RavgQL'])

for i in range(len(jobList)):
    df=df.append(vars(jobList[i]), ignore_index=True)

print("Three Server Model by Ahsan Rahim")
print(df)










 
