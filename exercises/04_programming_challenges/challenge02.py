# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:19:52 2024

@author: wooihaw
"""

try:
    invest = float(input("Enter initial investment: "))
    rate = float(input("Enter annual rate (%): "))
    years = int(input("Enter the years of investment: "))
except Exception as e:
    print(f"Error: {e}")
else:
    for y in range(years):
        invest = invest + invest * rate/100
        print(f"Year {y+1}: RM{invest: .2f}")
        