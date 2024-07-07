def invert_dict(d):
    return {v: k for k, v in d.items()}

original = {'a': 1, 'b': 2, 'c': 3}
inverted = invert_dict(original)
print(inverted)  # Output: {1: 'a', 2: 'b', 3: 'c'}
