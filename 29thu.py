# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:52:49 2024

@author: LENOVO
"""

#29 Tìm số trung vị của một danh sách

def question_29(nums: list[int]) -> float:
    nums.sort()
    n=len(nums)
  # Kiểm tra nếu số lượng phần tử là lẻ
    if n%2==1:
        return nums[n//2]
  # Nếu số lượng phần tử là chẵn, tính trung bình cộng của hai giá trị ở giữa
    else:
        giua1= nums[n//2-1]
        giua2= nums[n//2]
    return (giua1+ giua2) / 2
print(question_29(nums = [3, 1, 4, 5, 9, 2, 6, 8, 7]))