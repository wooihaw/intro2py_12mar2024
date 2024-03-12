# Write a Python script to ask for a string and two substrings,
# and print the string with all occurrences of the first substring
# replaced by the second substring.
# E.g.
# Enter a string: Hello world!
# Enter substring to replace: world
# Enter replacement substring: Python
# Hello Python!

s1 = input("Enter a string: ")
s2 = input("Enter substring to replace: ")
s3 = input("Enter replacement substring: ")

print(s1.replace(s2, s3))