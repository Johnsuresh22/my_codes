def frequency_count(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = frequency_count(numbers)
print(count)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}
