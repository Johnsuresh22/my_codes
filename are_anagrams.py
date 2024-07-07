# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:29:44 2024

@author: P.JOHN
"""
def are_anagrams(word1,word2):
    word1= word1.lower()
    word2 = word2.lower()
    return sorted(word1)== sorted(word2)
print(are_anagrams("elbow", "below"))  # Output: True
print(are_anagrams("dustyy", "studyy"))  # Output: True
