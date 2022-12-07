#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:34:34 2022

@author: dennis
"""

with open('../input/day6.in') as f:
    stream = f.readline().strip()

def find_packet_marker(s, n):
    for i in range(n-1, len(s)):
        marker = s[i-n+1:i+1]
        if len(set(marker)) == n:
            return i+1

print('Part 1:', find_packet_marker(stream, 4))
print('Part 2:', find_packet_marker(stream, 14))
