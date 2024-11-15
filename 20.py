# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:59:12 2024

@author: LENOVO
"""

from typing import Optional
def question_20() -> Optional[str]:
    s = input("Nhập giá trị từ bán phím: ")
    if s:
        return s
    else:
        return None
print(question_20())