#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:56:28 2022

@author: dennis
"""

import re

with open('../input/day4.in') as f:
    lines = [line.strip() for line in f]

def range_check(r1, r2, s1, s2):
    rs1 = [x in r2 for x in r1]
    rs2 = [x in r1 for x in r2]
    s1 += (sum(rs1) == len(r1)) or (sum(rs2) == len(r2))
    s2 += max(rs1) or max(rs2)
    return s1, s2

s1, s2 = 0, 0
for pair in lines:
    start1, end1, start2, end2 = (int(x) for x in re.split(',|-', pair))
    s1, s2 = range_check(range(start1, end1+1), range(start2, end2+1), s1, s2)
print('Part1:', s1)
print('Part2:', s2)
