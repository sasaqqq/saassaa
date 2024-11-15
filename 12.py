# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:57:25 2024

@author: LENOVO
"""

import random
def question_12()->bool:
    n=random.randint(1,1000)
    print(f"số ngẫu nhiên là: {n}")
    if n < 2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(question_12())
        
    