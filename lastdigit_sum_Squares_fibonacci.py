#!/usr/bin/env python
# coding: utf-8

# In[19]:





def fibci_lastdigit(n):
    if(n<1):
        return n
    a=0
    b=1

    for _ in range(n - 1):
        a,b=b%10,(a+b)%10  #here I do fibonacci with just considering last digits.This makes program faster

    return b%10

def fibci_sumsqrs(n):
    #Making use of fact that when modulo 11 ,pisano period is 10
    vertical_side = fibci_lastdigit(n % 10)
    horizontal_side = fibci_lastdigit((n + 1) % 10)
    return (vertical_side * horizontal_side) % 11


n = int(input())
print(fibci_sumsqrs(n))


# In[ ]:





# In[ ]:




