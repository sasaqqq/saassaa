# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:58:46 2024

@author: LENOVO
"""

def question_27(strs: list[str])-> str:
    tiento= strs[0]
    for s in strs[1:]:
        while not s.startswith(tiento):
            tiento= tiento[:-1]
            if not tiento:
                return " "
    return tiento
print(question_27(strs = ["flower", "flow", "flight"]))