# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:33:28 2024

@author: wooihaw
"""

def mean(data):
    return sum(data)/len(data)

def median(data):
    n = len(data)
    if n % 2:
        return data[n // 2]
    else:
        return (data[n//2 - 1] + data[n // 2]) / 2

raw_data = None
with open("data/Heathrow.txt", "r") as f:
    raw_data = f.readlines()

if raw_data is not None:
    # print(raw_data)
    data = [float(t.strip()) for t in raw_data]
    # print(data)
    data.sort()
    print(f"Lowest temperature: {data[0]}")
    print(f"Highest temperature: {data[-1]}")
    print(f"Mean temperature: {mean(data):.2f}")
    print(f"Median temperature: {median(data)}")
else:
    print("Error in opening the file")