# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:49:08 2024

@author: LENOVO
"""
#tính giai thừa
def question_6 (n:int)-> int:
    if n==0 or n==1:
        return 1
    else:
        kq=n
        for i in range(2,n):
            kq*=i
    return kq
print(question_6(5))