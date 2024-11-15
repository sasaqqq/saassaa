# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 17:36:18 2024

@author: LENOVO
"""

#set: loại bỏ các phần tử trùng lặp trong mảng nums 
from typing import List
def question_23(nums: List[int]) -> bool:
    s = set()  
    for n in nums:
        if n in s: 
            return True  
        s.add(n)    
    return False  
print(question_23([1, 2, 3, 1])) 
