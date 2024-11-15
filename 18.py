# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:32:52 2024

@author: LENOVO
"""

def question_18(s: str) -> str:
    s = s.strip()
    s = " ".join(s.split())
    return s
print(question_18("   Hello   World   "))
