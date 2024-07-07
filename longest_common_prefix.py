# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:48:20 2024

@author: P.JOHN
"""

s = "hello"
prefix = "het"
print(s.startswith(prefix))  # Output: True
if not s.startswith(prefix):
    prefix = prefix[:-1]
    print(prefix)

prefix = "lo"
print(s.startswith(prefix))  # Output: False


def longest_common_prefix(lst):
    if not lst:
        return " "
    prefix = lst[0]
    for s in lst[1:]:
        while not s.startswith(prefix):
            prefix =prefix[:-1]
            if not prefix:
                return " "
    return prefix
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))