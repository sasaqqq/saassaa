# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:20:31 2024

@author: LENOVO
"""

from typing import Optional
def question_21(nums: list[int], target: int)->Optional[tuple[int, int]]:
    ds = {}
    for a in nums:
        socantim = target - a
        if socantim in ds:
            return(socantim, a)
        ds[a] = True
    return None
print(question_21(nums = [2,7,11,15], target = 9))