#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_optimal_value(capacity, weights, values):
    value = 0
    unitweight=[0]*len(values)
    for i in range(len(values)):
        unitweight[i]=values[i]/weights[i]
    while(capacity>0):
        maxuw=max(unitweight)
        posmax1=unitweight.index(maxuw)
        
        if(weights[posmax1]>capacity):
            ratio=capacity/weights[posmax1]
            weights[posmax1]=ratio*weights[posmax1]
            values[posmax1]=ratio*values[posmax1]
           
        if(weights[posmax1]<capacity and len(weights)<=1):
            value+=values[posmax1]
            return value
    
        value+=values[posmax1]        
        capacity-=weights[posmax1]
        
        unitweight.remove(unitweight[posmax1])
        values.remove(values[posmax1])
        weights.remove(weights[posmax1])
    

    return value


if __name__ == "__main__":
    data = list(map(int,input().split()))
    n, capacity = data[0:2]
    values = [0]*n
    weights = [0]*n
    for i in range(n):
        values[i], weights[i] = map(int, input().split())

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

