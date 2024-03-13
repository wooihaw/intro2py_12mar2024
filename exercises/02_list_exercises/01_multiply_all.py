# Write a Python script to multiply all the items in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -1]
print(f'{alist=}')

# Eg.
total = 0
for i in alist:
    total += i
print(f"The total is {total}.")
print(f"{sum(alist) = }")

# Solution
product = 1
for i in alist:
    product *= i
print(f"The product is {product:,}.")

# Use list comprehension
p = 1
product = [p:=p*i for i in alist]
print(f"The product is {product[-1]:,}.")