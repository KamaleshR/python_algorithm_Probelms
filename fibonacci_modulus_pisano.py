#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fibci(n): #fuction to calculate nth fib number.
    a,b=0,1
    if(n==1 or n==0):
        return n
    else:
        for i in range(2,n+1):
            a,b=b,a+b
    return b


def piso_len(m): #function to determine length of pisano period, that is second occurence of ..-0-1.
    i=2
    while(fibci(i)%m!=0): #Increment i till we find a 0.
        i+=1
    if(fibci(i+1)%m!=1): #check if next elem is 1 or not. If 1 then yo, we found period, else crement till we find 1
        while(fibci(i+1)%m!=1): #increment i till we reach value which resuts in 1 when mod by m, and after which we check prev element for 0 
            i+=i #i increases till we find 1 at its next point i.e., (i+1)
    print("Length of pisano sequence of ",m," is::",i)
    return i #return the period where ith element is 0 and (i+1)th elem = 1 when mod(m)


n,m=map(int,input().split())
#it takes time to compute mod of bigger fib number, so I broke it. f(n)%f(m) if and only if n%m (pisano period concept)
r=n%piso_len(m)# break nth fiboncacci number to small number by using pisano concept. Instead of finding mod of big number, just find repeat period and use the remainder to find mod,which will give same result as  big number mod m.
print(fibci(r)%m)


# In[ ]:





# In[ ]:




