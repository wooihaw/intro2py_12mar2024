# Write a Python script to find the frequency of occurance for each alphabet in a string.
astring = 'The quick brown fox jumps over the lazy dog.'

# Clean and normalize the string
t = [c.lower() for c in astring if c.isalpha()]

# Method 1 - Use the for loop
freq1 = {}
for c in sorted(set(t)):
    freq1[c] = t.count(c)
print(f"{freq1 = }")

# Method 2 - dictionary comprehension
freq2 = {c: t.count(c) for c in sorted(set(t))}
print(f"{freq2 = }")

print(f"The letter 'o' appears {freq2['o']} times in the string.")