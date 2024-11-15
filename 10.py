# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:32:06 2024

@author: LENOVO
"""

def question_10()->None:
    ds=input("Nhập vào danh sách số nguyên:")
    if not ds:
        return None
    ds_sn=[int(i) for i in ds.split()]
    return ds_sn
print(question_10())

