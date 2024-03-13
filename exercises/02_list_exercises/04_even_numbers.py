# Write a Python script that takes a list of numbers and returns a new list containing only the even numbers from the original list.
alist = [12, 43, 57, 98, 83, -103, 256, -55, 168, -6]
print(f'{alist=}')

# Use the for loop
even_num1 = []
for n in alist:
    if n % 2 == 0:
        even_num1.append(n)
print(f"{even_num1 = }")

# Use list comprehension
print(f"{[n for n in alist if n%2 == 0]}")