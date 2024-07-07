# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:19:42 2024

@author: P.JOHN
"""

def binary_search(lst , target):
    left =0 
    right= len(lst)-1
    while left<=right:
        mid = (left+right)//2
        if lst[mid]==target:
            return mid
        elif target > lst[mid]:
            left = mid+1
        else:
            right =mid-1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = binary_search(numbers, 5)
print(index)