# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:42:34 2024

@author: P.JOHN
"""

def romanToInt(s: str) -> int:
    # Define the mapping of Roman numerals to integers
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    print('---',s)
    
    # Iterate through each character in the string
    for char in s:
        current_value = roman_to_int[char]
        print(current_value,'>',prev_value)
        
        # If current value is greater than previous value, subtract twice the previous value
        if current_value > prev_value:
            print(current_value,'-',2 ,'*',prev_value)
            total += current_value - 2 * prev_value
        else:
            print('-----')
            total += current_value
        
        # Update previous value to current value for next iteration
        print('------',prev_value)
        prev_value = current_value
    
    return total

# Example usage:
print(romanToInt("III"))     # Output: 3
print(romanToInt("LVIII"))   # Output: 58
print(romanToInt("MCMXCIV")) # Output: 1994
