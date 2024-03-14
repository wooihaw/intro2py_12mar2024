# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:14:36 2024

@author: wooihaw
"""

# r + c = 35
# 4*r + 2*c = 94

for c in range(36):
    r = 35 - c
    if 2*c + 4*r == 94:
        print(f"There are {c} chickens and {r} rabbits in the farm.")
