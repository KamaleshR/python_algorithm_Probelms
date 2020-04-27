#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def max_prize(m):
    
    arr=[] #initial array to store the pairs
    i=1    #iter variable

    while(m>0): #loop till we reduce given number to zero by taking value of pairs from it
        m-=i     # reduce value , so that we can focus next value of m to build pairs on
        if(m!=0): 
            arr.append(i) #append pairs to array
        i+=1 #increment iter var here , becz funct may end in next if conditional
        if(m-(i+i)<=0): #to prevent over valuing. If m-(i+i)<0 means we have no choice to get value of m hereafter.
            arr.append(m) #so we just append the value of m itself and end the process
            break

    return arr

n=int(input())
if(n>2):
    opt=max_prize(n)
    print(len(opt))
    print(*max_prize(n)) # used * to print all elem. Else it will display in list format
elif(n==1 or n==2): # No need to compute and waste time for known basic result. This helped to remove a block of while loop , which would otherwise will be needed
    print(1)
    print(n)
else:
    print(0)
        

