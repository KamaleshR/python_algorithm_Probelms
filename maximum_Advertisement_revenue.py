#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort()
ans = sum([a[i]*b[i] for i in range(n)])
print(ans)
