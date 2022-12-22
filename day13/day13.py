#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:59:27 2022

@author: dennis
"""

# def create_list(s):
#     li = []
#     depth = 1
#     for 
    
#     return li

pairs = []
with open('../input/day13.test') as f:
    for _ in range(1000):
        left = eval(f.readline().strip())
        if not left:
            break
        right = eval(f.readline().strip())
        _ = f.readline()
        pairs.append((left, right))

li = []
depth = 1
for x in right.split('['):
    if not  x:
        depth += 1
