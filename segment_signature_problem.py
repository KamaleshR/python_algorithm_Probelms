#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def signature_alot(mainlist):
    cord=[]
    pos=0
    n=len(mainlist)
    mainlist.sort(key=lambda x:x[1]) #sort elements based on [][1]th values in them
    while(pos<n-1):  #to loop and prevent list index out of range
        curr=mainlist[pos] #store current vaue in variable
        while( pos<n-1 and curr[1] >= mainlist[pos+1][0]): 
            '''Since sorted by last element value, we compare last element of 1 segment and 1st value of next element
            So when we see that curr >= next elem[0] it means it lies within rangeof that "Next segment" coordinate
            Becz as per input format of co-ordinate [][0]always > [0][].
            So if x>[0][] and since we are at 1st elem and we know that next elem has x<[][1] since we sorted that way
            we can be sure that x exists within the segment'''
            pos+=1
        cord.append(curr[1])
        pos+=1
    
    
    
    return cord


n=int(input())
mainlist=[]
for i in range(n):
    a,b=map(int,input().split())
    mainlist.append([a,b]) 

opt=signature_alot(mainlist) #storing in variable isntead of direct call ,becz we also need len of cord[].
print(len(opt))
print(' '.join([str(i) for i in opt]))

