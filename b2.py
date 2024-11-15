# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:09:27 2024

@author: LENOVO
"""
#ngẫu nhiên, tổng, tb
import random
def question_2 (n:int)->(int, float):
    ds=[]
    for i in range(n):
        x=random.randint(1,100)
        ds.append(x)
    tong=sum(ds)
    tb=tong/n
    return (tong, tb)
print(question_2(5))