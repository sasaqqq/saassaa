# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:28:18 2024

@author: LENOVO
"""

def question_9(s:str)->bool:
    chuoi_s=''.join(i.lower()for i in s if i.isalnum())
    chuoi_s_dao=chuoi_s[::-1]
    return chuoi_s==chuoi_s_dao
print(question_9("A man, a plan,a canal:Panama"))