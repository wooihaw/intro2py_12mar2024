# Write a Python script to concatenate following dictionaries to create a new one.
# Expected Result: 
# d4 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

d1 = {'a': 10, 'b': 20}
d2 = {'c': 30, 'd': 40}
d3 = {'e': 50}

# Method 1 - Use the union operator
d4_1 = d1 | d2 | d3
print(f"{d4_1 = }")

# Method 2 - Use the update() method
d4_2 = {}
for d in (d1, d2, d3):
    d4_2.update(d)
print(f"{d4_2 = }")
