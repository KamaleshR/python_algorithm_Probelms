#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys


def compute_min_refills(distance, tank, stops):
    current=0
    numrefill=0
    ns=len(stops)-2 #number of stops. I have included start point and end point stops in array so have to reduce by 2 to get just number of fuel stops
    while(current<=ns):
        last=current
        while(current<=ns and stops[current+1]-stops[last]<=tank):
            current+=1
        if(current==last):
            return -1
        if(current<=ns):
            numrefill+=1
        

    return numrefill

if __name__ == '__main__':
    d=int(input())
    m=int(input())
    n=int(input())
    stops=[0]*(n+2)
    stops[0]=0
    stops[n+1]=d
    inpt=input()
    li=inpt.split()
    for i in range(1,n+1):
        stops[i]=int(li[i-1])     
    assert(len(stops)==n+2),"Invalid Input"
    print(compute_min_refills(d,m,stops))

