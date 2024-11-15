# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:33:38 2024

@author: LENOVO
"""

def question_5 (lst: list, x:int)->int or None:
    if x in lst:
        return lst.index(x)
    return None
print(question_5([1,2,3,4,5], 3))