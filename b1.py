# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:46:45 2024

@author: LENOVO
"""
#tìm số nguyên tố
def question_1 (n: int) -> bool:
    if n<2:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True
print (question_1 (2))
