# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:12:39 2024

@author: LENOVO
"""
#thường, hoa
def question_3 (s: str)->(int, int):
    return len([i for i in s if i.isupper()]), len([i for i in s if i.islower()])
print(question_3("Hello World"))