# In-class examples for Day 2
#%% Dictionary creation and modification
adict = dict(a=1, b=2.5, c='abc')
print(f"{adict['b'] = }")

adict['a'] = 3.45  # modify the value for key 'a'
print(f"{adict = }")

adict['d'] = [1, 2, 3]  # insert a new key-value pair
print(f"{adict = }")

del adict['c']
print(f"{adict = }")

#%% Dictionary methods
adict = dict(a=1, b=2.5, c='abc')

# print(f"{adict['e'] = }")  # KeyError as the key is not found in the dictionary

# Use get() method to return the default value if the key is not found
print(f"{adict.get('e', 'Not found') = }")
print(f"{adict = }")

# The setdefault() method will insert the key and default value if the key is not found
print(f"{adict.setdefault('e', 'Not found') = }")
print(f"{adict = }")

#%% Joining 2 dictionaries

d1 = {'a':1, 'b':2, 'c':3}
d2 = dict(x=4, y=5, z=6)

# Method 1
d3 = d1.copy()
d3.update(d2)
print(f"{d3 = }")

# Method 2
d4 = d1 | d2
print(f"{d4 = }")

#%% Set methods
name1 = ['Ali', 'Baba', 'Cloud', 'Dave', 'Edward']
name2 = ['John', 'Donald', 'Edward', 'Peter', 'Ali']

common_names = list(set(name1) & set(name2))
print(f"{common_names = }")

uncommon_names = list(set(name1).symmetric_difference(set(name2)))
print(f"{uncommon_names = }")

all_names = list(set(name1) | set(name2))
print(f"{all_names = }")

#%% Conditional statement
mark = 45
if mark >= 50:
    print("Passed the test.")
    print("Still passed the test.")
    print("Passed the test again.")
else:
    print("Failed the test.")
    print("Still failled the test.")
    print("Failed the test again.")
print("Outside of if-else block")

#%% Ternary operator

num = int(input("Enter an integer: "))

# Use if-else statement
if num % 2:
    print("This is an odd number.")
else:
    print("This is an even number.")

# Use ternary operator
print(f"This is an {'odd' if num % 2 else 'even'} number.")

#%% Examples for loop
names = ['ali', 'baba', 'cloud', 'data']
ages = [13, 37, 45, 59]
blood_types = ['a', 'o', 'b', 'ab', 'o']

# Using index to loop through multiple lists
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old with blood type {blood_types[i]}.")

# Using zip() to combine multiple lists
for i, j, k in zip(names, ages, blood_types):
    print(f"{i} is {j} years old with blood type {k}.")
    
# Using enumerate() to automatically add an index to each iteration
for n, (i, j, k) in enumerate(zip(names, ages, blood_types), start=1):
    print(f"{n}. {i.capitalize()} is {j} years old with blood type {k.upper()}.")

#%% Example for while loop

while True:
    name = input("Enter your name: ")
    print(f"Hello {name}!")
    ...
    ans = input("Do you want to repeat? ([y]/n) ") or 'y'
    if ans in ('y', 'Y'):
        continue
    elif ans in ('n', 'N'):
        print("Good bye!")
    else:
        print("Invalid choice!")
    break

#%% List comprehension example 1
# Select the words that start with vowels
words = ('ant', 'boy', 'eggs', 'cake', 'door', 'whale', 'orange')

# Method 1 - Use the for loop
vowel_words1 = []
for w in words:
    if w[0] in 'aeiou':
        vowel_words1.append(w)
print(f"{vowel_words1  = }")

# Method 2 - Use list comprehension
vowel_words2 = [w for w in words if w[0] in 'aeiou']
print(f"{vowel_words2  = }")

#%% List comprehension example 2
# Calculate the number of odd numbers in a list
numbers = [1, 4, 3, 2, 5, 10, 11, 45, 23, 36, 57]

# Method 1 - Use the for loop
count = 0
for n in numbers:
    if n % 2:
        count += 1
print(f"There are {count} odd numbers in the list.")

# Method 2 - Use list comprehension
print(f"There are {sum([1 for n in numbers if n % 2])} odd numbers in the list.")

#%% Dictionary comprehension
# Create a new dictionary for discounted price (after 10% discount)

prices = dict(apple=1.5, orange=2.5, durian=20, mango=8)

# Method 1 - Use the for loop
new_prices1 = {}
for k in prices:
    new_prices1[k] = prices[k] * 0.9
print(f"{new_prices1 = }")

# Method 2 - Use dictionary comprehension
new_prices2 = {k: prices[k] * 0.9 for k in prices}
print(f"{new_prices2 = }")

#%% Use any() and all() functions
# Check whether any words in the tuple starts with a vowels
words = ('bees', 'cats', 'eggs', 'boy')

# Method 1 - Use the for loop
ans = False
for w in words:
    if w[0] in 'aeiou':
        ans = True
        break
if ans:
    print("There is at least one word that starts with a vowel.")
else:
    print("There is no word that starts with a vowel.")

# Method 2 - Use any() and list comprehension
if any(True for w in words if w[0] in 'aeiou'):
    print("There is at least one word that starts with a vowel.")
else:
    print("There is no word that starts with a vowel.")    

# Check whether all words in the tuple starts with a vowel
words2 = ('apple', 'eggs', 'orange')
if all(True if w[0] in 'aeiou' else False for w in words2):
    print("All words in the tuple start with a vowel.")
else:
    print("Not all words in the tuple start with a vowel.")



















