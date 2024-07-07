# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:27:45 2024

@author: P.JOHN
"""

def merge_sorted_lists(list1,list2):
    i,j=0,0
    result =[]
    while i<len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            
            i+=1
        else:
            result.append(list2[j])
            j+=1
            
        
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = merge_sorted_lists(list1, list2)
print(merged_list)