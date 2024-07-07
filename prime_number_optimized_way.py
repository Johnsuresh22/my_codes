# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 22:24:18 2024

@author: P.JOHN
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(29))  # Output: True
print(is_prime(15))  # Output: False
