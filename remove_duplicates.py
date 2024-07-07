# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 20:06:03 2024

@author: P.JOHN
"""
def remove_duplicates(lst):
    elements =set()
    result = []
    for i in lst:
        if i not in elements:
            elements.add(i)
            result.append(i)
    return result
numbers = [1, 2, 3, 1, 2, 3, 4, 5]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers) 