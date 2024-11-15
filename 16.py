# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:22:47 2024

@author: LENOVO
"""

def question_16(*arg) -> float:
    if not arg:
        return None
    return sum(arg)/len(arg)
print(question_16(1,2,3,4,5))
