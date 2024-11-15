# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:25:13 2024

@author: LENOVO
"""

import random 
def question_17(n: int) -> list:
    danh_sách = []
    for i in range(n):
        x = random.randint(1, 100)
        danh_sách.append(x)
    danh_sách.sort(reverse= True)
    return danh_sách
print(question_17(5))
   