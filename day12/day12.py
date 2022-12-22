#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:06:03 2022

@author: dennis
"""

from dataclasses import dataclass
import numpy as np

@dataclass
class Position:
    x: int
    y: int

def find_climbable(myPos):
    x = myPos.x
    y = myPos.y
    climbable = []
    myLevel = c2i(grid[y][x])
    if myPos.x:
        if myLevel + 1 >= c2i(grid[y][x-1]) and not distances[y][x-1]:
            climbable.append(Position(x-1, y))
            distances[y][x-1] = dist
    if myPos.x <= len(grid[0]) - 2:
        if myLevel + 1 >= c2i(grid[y][x+1]) and not distances[y][x+1]:
            climbable.append(Position(x+1, y))
            distances[y][x+1] = dist
    if myPos.y:
        if myLevel + 1 >= c2i(grid[y-1][x]) and not distances[y-1][x]:
            climbable.append(Position(x, y-1))
            distances[y-1][x] = dist
    if myPos.y <= len(grid) - 2:
        if myLevel + 1 >= c2i(grid[y+1][x]) and not distances[y+1][x]:
            climbable.append(Position(x, y+1))
            distances[y+1][x] = dist
    return climbable

def c2i(char):
    if char == 'S':
        char = 'a'
    elif char == 'E':
        char = 'z'
    return ord(char) - 97

with open('../input/day12.in') as f:
    grid = [line.strip() for line in f]

starting_positions = []
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == 'S':
            part1_start = Position(row.index('S'), y)
            starting_positions.append(Position(x, y))
        elif char == 'E':
            exit = Position(row.index('E'), y)
        elif char =='a':
            starting_positions.append(Position(x, y))

shortest = np.inf
for start in starting_positions:
    distances = [[0 for _ in range(len(grid[0]))] for _ in grid]
    dist = 1
    queue = find_climbable(start)

    while queue:
        dist += 1
        new_queue = []
        for neighbour in queue:
            new_queue += find_climbable(neighbour)
        queue = new_queue

    distToExit = distances[exit.y][exit.x]
    if distToExit:
        shortest = min(shortest, distToExit)
    if start == part1_start:
        print('Part 1:', distToExit)
print('Part 2:', shortest)
