#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 00:46:58 2022

@author: dennis
"""

with open('../input/day1.in') as f:
    meals = sorted([sum(int(c) for c in m.split()) for m in f.read()[:-1].split('\n\n')])
print('Part 1:', meals[-1])
print('Part 2:', sum(meals[-3:]))
