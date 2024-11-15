# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:46:55 2024

@author: LENOVO
"""

from collections import Counter
def question_26(s: str)-> int:
    demchuoi = Counter(s)
    dodai = 0
    cokitule = False
    for dem in demchuoi.values():
        dodai += dem // 2*2
        if dem % 2 ==1:
            cokitule = True
    if cokitule:
        dodai +=1
    return dodai
print(question_26("abccccdd"))

   