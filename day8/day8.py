#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:09:26 2022

@author: dennis
"""

import math

class Grid:

    def __init__(self, file_path):
        self.grid = []
        with open(file_path) as f:
            for line in f:
                self.grid.append([int(x) for x in line.strip()])

    def process(self, x, y):
        v = self.grid[y][x]
        row = self.grid[y]
        column = [row[x] for row in self.grid]
        directions = [row[:x][::-1], row[x+1:], column[:y][::-1], column[y+1:]]
        part1 =  max(max(direction) < v for direction in directions)
        part2 = math.prod(self._viewing_distance(direction, v) for direction in directions)
        return part1, part2
    
    def _viewing_distance(self, trees, v):
        for i, x in enumerate(trees, start=1):
            if x >= v:
                break
        return i

grid = Grid('../input/day8.in')
n_visible = len(grid.grid)*2 + len(grid.grid[0])*2 - 4
highest_scenic_score = 0
for y in range(1, len(grid.grid) - 1):
    for x in range(1, len(grid.grid[0]) - 1):
        part1, part2 = grid.process(x, y)
        n_visible += part1
        highest_scenic_score = max(highest_scenic_score, part2)

print('Part 1:', n_visible)
print('Part 2:', highest_scenic_score)
