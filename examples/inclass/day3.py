# In-class examples for Day 3

#%% Use pickle to store a dictionary to a file
import pickle

data = {}
ans = 'y'
while ans.lower() in ('y', 'yes'):
    name = input("Enter name: ") or "Unknown"
    age = input("Enter age: ") or "0"
    data[name] = age
    ans = input("Do you want to enter another data? ([y]/n) ") or "y"
    
print(f"{data = }")

with open("nameage.pkl", "wb") as f:
    pickle.dump(data, f)

#%% Use pickle to retrieve the saved dictionary from a file
import pickle

with open("nameage.pkl", "rb") as f:
    mydata = pickle.load(f)

print(f"{mydata = }")

#%% Exception handling

while True:
    try:
        num = int(input("Enter an integer: "))
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"You have entered {num}")
        break

#%% Functions and return value
def myfunc1(x, y):
    print(x, y)

def myfunc2(x: int|float, y: int|float) -> int|float:
    '''This is a function to add 2 arguments'''
    return x + y

a = myfunc1(11, 22)
b = myfunc2(33, 44)

print(f"{a = }, {b = }")

#%% Function that returns multiple values
def myfunc3(x: int, y: int, z: int) -> tuple[int]:
    '''This is a function whicn returns 3 values'''
    return x*x, y*y, z*z

a = myfunc3(2, 3, 4)
print(f"{a = }, {type(a) = }")

b, c, d = myfunc3(5, 6, 7)
print(f"{b = }, {c = }, {d = }")

#%% Functions are objects
def func1(x):
    return x + 1

def func2(y):
    return y - 1

def func3(z):
    return z * 2

functions = (func1, func2, func3)
for f in functions:
    print(f(10))
    
d_func = {'function 1': func1, 'function 2': func2, 'function 3': func3}
for k in d_func:
    print(f"{k} returns {d_func[k](10)}")

#%% Lambda function example 1
alist = [(1, 2, 3), (11, 4, 1), (7, 9, 2)]
blist = sorted(alist)
print(f"{alist = }\n{blist = }")

# To sort according to the 3rd element of each tuple in descending order
clist = sorted(alist, key=lambda x: x[2], reverse=True)
print(f"{clist = }")

#%% Lambda function example 2
# Sort the list based on the ID numbers
IDs = ['ID21', 'ID7', 'ID55', 'ID101', 'ID3', 'ID82', 'ID12', 'ID234']
print(f"{sorted(IDs)}")

sorted_IDs = sorted(IDs, key=lambda x:int(x[2:]))
print(f"{sorted_IDs = }")

print(f"Oldest member: {min(IDs, key=lambda x:int(x[2:]))}")
print(f"Youngest member: {max(IDs, key=lambda x:int(x[2:]))}")

#%% Lambda function example 3
GIDs = ['G2ID25', 'G1ID14', 'G2ID10', 'G1ID2', 'G2ID33', 'G1ID25']

print(f"{sorted(GIDs) = }")

# Sort group in descending order and ID in ascending order
sorted_GIDs = sorted(GIDs, key=lambda z: (-int(z[1]), int(z[4:])))
print(f"{sorted_GIDs = }")

#%% Example of map() function
# Reverse each string in a list
words = ['apple', 'bell', 'cat', 'door', 'eggs']

# Method 1 - Use the for loop
r1 = []
for w in words:
    r1.append(w[::-1])
print(f"{r1 = }")

# Method 2 - list comprehension
r2 = [w[::-1] for w in words]
print(f"{r2 = }")

# Method 3 - Use map() function
r3 = list(map(lambda w:w[::-1], words))
print(f"{r3 = }")

#%% Example of filter() function
# Select only the palindrome from the tuple
words = ('ant', 'boy', 'civic', 'dad', 'fish', 'madam')

# Method 1 - Use the for loop
p1 = []
for w in words:
    if w == w[::-1]:
        p1.append(w)
print(f"{p1 = }")

# Method 2 - Use list comprehension
p2 = [w for w in words if w == w[::-1]]
print(f"{p2 = }")

# Method 3 - Use filter() function
p3 = list(filter(lambda w: w == w[::-1], words))
print(f"{p3 = }")










        
