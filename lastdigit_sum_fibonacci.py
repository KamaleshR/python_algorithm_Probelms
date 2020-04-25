#!/usr/bin/env python
# coding: utf-8

# In[16]:


def fibci(n):
    a=0
    b=1
    s=1
    if n<=1:
        return n
    for i in range(n-1):
        a,b=b,a+b
        s+=b
    return s

def digi(n):
    k=fibci(n)
    return k%10
    

n=int(input())
print(digi(n))


# In[ ]:





# In[ ]:




