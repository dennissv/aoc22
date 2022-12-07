#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:11:47 2022

@author: dennis
"""

def common_substrings(*strings):
  substrings = []
  for i in range(len(strings[0])):
    for j in range(i+1, len(strings[0])+1):
      if all(strings[0][i:j] in s for s in strings):
        substrings.append(strings[0][i:j])
  return substrings

def priority_score(ch):
   return ord(ch) - 38 if ch.isupper() else ord(ch) - 96

with open('../input/day3.in') as f:
    lines = [line.strip() for line in f]

score_part1, score_part2 = 0, 0
rucksacks = []
for rucksack in lines:
    substrings1 = common_substrings(rucksack[:len(rucksack)//2], 
                                    rucksack[len(rucksack)//2:])
    score_part1 += max(priority_score(substring) for substring in substrings1)
    
    rucksacks.append(rucksack)
    if len(rucksacks) == 3:
        substrings2 = common_substrings(*rucksacks)
        score_part2 += max(priority_score(substring) for substring in substrings2)
        rucksacks = []

print('Part 1:', score_part1)
print('Part 2:', score_part2)
