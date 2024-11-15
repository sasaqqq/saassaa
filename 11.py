# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:44:57 2024

@author: LENOVO
"""

def question_11(n:int)-> int:
    a,b = 0,1
    for i in range(n):
        a,b=b,a+b
    return a
print(question_11(10))

    