#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fibci_lastdigit(n):
    a=0
    b=1
    if(n<=1):
        return n
    else:
        for i in range(n-1):
            a,b=b%10,(a+b)%10
        return b%10


n = int(input())
print(fibci_lastdigit(n))


# In[ ]:




