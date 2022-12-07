#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:48:13 2022

@author: dennis
"""

import re
from copy import deepcopy

with open('../input/day5.in') as f:
    lines = [line.rstrip('\n') for line in f]

crates = [[] for _ in range(9)]
for line in lines[:8][::-1]:
    line = line.replace('    ', '[ ]')
    symbols = re.findall(r'\[(.*?)\]', line)
    for i, symbol in enumerate(symbols):
        if symbol != ' ':
            crates[i].append(symbol)
crates2 = deepcopy(crates)

for instruction in lines[10:]:
    numbers = re.findall(r'\d+', instruction)
    n, from_, to = [int(num) for num in numbers]
    for _ in range(n):
        crates[to - 1].append((crates[from_ - 1].pop()))
print('Part 1:', ''.join(crate[-1] for crate in crates))

for instruction in lines[10:]:
    numbers = re.findall(r'\d+', instruction)
    n, from_, to = [int(num) for num in numbers]
    crates2[to - 1] += crates2[from_ - 1][-n:]
    crates2[from_ - 1] = crates2[from_ - 1][:-n]
print('Part 2:', ''.join(crate[-1] for crate in crates2))
