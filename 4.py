# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:21:27 2024

@author: LENOVO
"""
#tìm chẵn lẻ
def question_4(n:int)->bool:
    if n%2==0:
        return True
    elif n%2!=0:
        return False
print(question_4(4))