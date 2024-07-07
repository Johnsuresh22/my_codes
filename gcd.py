# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:25:45 2024

@author: P.JOHN
"""

def gcd(x,y):
    while y:
        
        x,y = y,x%y
    return x
print(gcd(27,9))