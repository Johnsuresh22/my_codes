# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:16:28 2023

@author: P.JOHN
"""
n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end =" ")
    for j in range(1,i+1):
        print(j,end =' ')
    for l in range(i-1,0,-1):
        print(l,end = " ")
    print()