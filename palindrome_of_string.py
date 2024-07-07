# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 22:40:11 2024

@author: P.JOHN
"""


def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
