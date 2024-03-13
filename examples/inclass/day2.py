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


















