# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:43:49 2024

@author: LENOVO
"""

from typing import List
def question_22(nums: List[int])-> None:
    so= 0
    for i in range(len(nums)):
       if nums[i] !=0:
           nums[so], nums[i]= nums[i], nums[so]
           so+=1
    return nums   
print(question_22(nums = [0,1,0,3,12]))