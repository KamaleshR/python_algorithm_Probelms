#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fibci(m,n):
    a=0
    b=1
    if n<=1:
        return n
    for i in range(m-1):
        a,b=b,a+b
    if(n==m):
        return b
    c=a+b
    s=c+b
    for i in range(m+1,n):
        b,c=c,b+c 
        s+=c
    return s


def digi(m,n):
    k=fibci(m,n)
    return k%10
    

m,n=map(int,input().split())
print(digi(m,n))


# In[ ]:





# In[ ]:




