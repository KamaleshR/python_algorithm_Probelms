#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def getchange(m):
    t,f,o=0,0,0 # variables to store values of number of coins of ten,five,one denomination
    temp=m
    while(temp>0):
        if(temp>=10):
            temp-=10
            t+=1
        elif(temp>=5):
            temp-=5
            f+=1
        elif(temp>1):
            temp-=1
            o+=1
        else:
            temp-=1
            o+=1
    return t+f+o
    
m=int(input())
print(getchange(m))

