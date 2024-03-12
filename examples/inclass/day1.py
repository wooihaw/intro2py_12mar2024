# In-class examples for Day 1

#%% Numeric data types
a = 28374659283740293840892035983402809829483759870924385082348764359823498570
b = a ** 10
print(a, b, sep=",")
print(a.__sizeof__())
print(b.__sizeof__())

c = 123_456_789
print(c)

#%% Binary and hexademical numbers
a = 0b10110101
b = 0x12cafe
print(a, b, sep=",")
print(bin(a), hex(b))

#%% Variables

# class = 123  # Using keywords as variable names will cause syntax error

a = 'bcd'
print(type(a))

# type = 2  # Built-in functions can be shadowed by variables of the same name
# del type  # This will delete the variable
# print(type(a))

#%% Convert between different data types
a, b, c = 1, 2.3, '456'
print(type(a), type(b), type(c), sep=",")

d = float(a)
e = str(b)
f = int(c)
print(d, e, f, sep=",")
print(type(d), type(e), type(f), sep=",")

g = '123abc'
h = int(g, base=16)
print(h, hex(h), type(h), sep=",")

#%% Arithmetic operators
a = 3 ** 2
b = -3 ** 2
c = (-3) ** 2
print(a, b, c, sep=", ")

#%% Comparison operators
a = 10
b = 25
print(a < b)
print(a > b)
print(a == b)
print(a != b)

print(0 <= a < 50)
print(50 <= b < 100)

#%% Raw string

print("You can insert \n as a new line character.")
print(r"You can insert \n as a new line character.")

#%% String indexing and slicing
s = "Introduction to Python"
print("First character: ", s[0])
print("Last character: ", s[-1])
print("First 12 characters: ", s[:12])
print("Last 6 characters: ", s[-6:])
print("Reverse the string: ", s[::-1])

#%% String concatenation and repetition
a = '45'
s = '123'
t = s + a
print(a, s, t, sep=", ")

u = 5 * "Ha "
print(u)

#%% String methods
s = "Introduction to Python"
print(s.upper())
print(s.lower())
print(s.title())
print(s.replace('n', 'm'))
print(s)  # s has never changed

t = s.lower().replace('p', 'c')  # methods can be chained
print(t)

#%% f-string formatting
a = 12.345
b = 6789

print(f"{a = }, {a = :.0f},  {a = :.1f}, {a = :.2f}")

print(f"Binary: {b:016b}, Hex: {b:08X}")

#%% Getting input from user
ans = input("Enter an integer: ")

print(f"{ans = }, {type(ans) = }")

print(f"10 times of {ans} is {10 * ans}")

if ans.isdigit():
    print(f"10 times of {ans} is {10 * int(ans)}")
else:
    print(f"{ans} is not an integer!")

#%% List join, append and extend
alist = [1, 2, 3]
print(f"{alist = }")

alist = alist + [4]
print(f"{alist = }")

alist += [5]  # similar to alist = alist + [5]
print(f"{alist = }")

alist.append(6)
print(f"{alist = }")

alist.extend([7, 8])
print(f"{alist = }")

print(f"{len(alist) = }")

#%% Sorting list
blist = [3, 1, 4, 2, 6, 5, 0]
clist = sorted(blist)  # return a list sorted in ascending order
dlist = sorted(blist, reverse=True)  # return a list softed in descending order
print(f"{blist = }, {clist = }, {dlist = }")

elist = blist.sort()
print(f"{blist = }, {elist = }")

#%% List methods
alist = [1, 2, 3.4, 'abc', [5, 6.78], 'yz', 1, 'a']

print(f"{alist.count(1) = }")
print(f"{alist.count('a') = }")
print(f"{alist.index(1) = }")  # only return the index of the first occurance

alist.remove(1)
print(f"{alist = }")  # only remove the first occurance of the item

alist.insert(2, 5)
print(f"{alist = }")

r = alist.pop(1)
print(f"{r = }, {alist = }")

#%% Tuple pack and unpacking
atuple = 1, 2.3, 4.5, 6
print(f"{atuple = }, {type(atuple) = }")

a, b, c, d = atuple
print(f"{a = }, {b = }, {c = }, {d = }")

x, *y = atuple
print(f"{x = }, {y = }")

*p, q, r = atuple
print(f"{p = }, {q = }. {r  = }")

























