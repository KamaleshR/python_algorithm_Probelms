#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fibci_sum_lastdigit(n):
    a=0
    b=1
    s=1
    if(n<=1):
        return n
    else:
        for i in range(n-1):
            a,b=b%10,(a+b)%10
            s+=b
        return s%10
    


n = int(input())
print(fibci_sum_lastdigit(n))


# In[ ]:




