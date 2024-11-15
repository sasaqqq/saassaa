# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:42:29 2024

@author: LENOVO
"""
#sort(): tăng dần
#sort(reverse=True): giảm dần
from typing import List
def question_25(nums: List[int])-> list[int]:
    binhphuong=[]
    for i in nums:
        binhphuong.append(i**2)
        binhphuong.sort()
    return binhphuong
print(question_25( nums = [-4, -1, 0, 3, 10]))