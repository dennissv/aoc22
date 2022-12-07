#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:18:10 2022

@author: dennis
"""

SCORES = {'A': {'X': 4, 'Y': 8, 'Z': 3},
          'B': {'X': 1, 'Y': 5, 'Z': 9},
          'C': {'X': 7, 'Y': 2, 'Z': 6}}
TO_CHOOSE = {'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
             'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
             'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}}

score_part1 = 0
score_part2 = 0
with open('../input/day2.in') as f:
    for line in f:
        player1, player2 = line.strip().split()
        score_part1 += SCORES[player1][player2]
        score_part2 += SCORES[player1][TO_CHOOSE[player1][player2]]

print('Part 1:', score_part1)
print('Part 2:', score_part2)
