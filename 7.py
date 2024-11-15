# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:54:26 2024

@author: LENOVO
"""
import random
def question_7(n:int)->(float, float):
    ds=[]
    for i in range(n):
        x=random.uniform(0,1)
        ds.append(x)
    lonnhat=max(ds)
    nhonhat=min(ds)
    return (lonnhat, nhonhat)
print (question_7(5))