# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:16:29 2024

@author: LENOVO
"""

from typing import List
def question_24(nums: List[int])-> int:
    phantu = None
    dem = 0
    for so in nums:
        if dem == 0:
            phantu = so
        dem+=1 if so == phantu else -1
    return phantu
print(question_24(nums = [3,2,3]))