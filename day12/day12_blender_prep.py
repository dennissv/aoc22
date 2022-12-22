#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:06:03 2022

@author: dennis
"""

from dataclasses import dataclass
import numpy as np
import networkx as nx

@dataclass
class Position:
    x: int
    y: int

def find_climbable(x, y):
    climbable = []
    myLevel = c2i(grid[y][x])
    if x:
        if myLevel + 1 >= c2i(grid[y][x-1]):
            climbable.append(f'{x-1},{y}')
    if x <= len(grid[0]) - 2:
        if myLevel + 1 >= c2i(grid[y][x+1]):
            climbable.append(f'{x+1},{y}')
    if y:
        if myLevel + 1 >= c2i(grid[y-1][x]):
            climbable.append(f'{x},{y-1}')
    if y <= len(grid) - 2:
        if myLevel + 1 >= c2i(grid[y+1][x]):
            climbable.append(f'{x},{y+1}')
    return climbable

def c2i(char):
    if char == 'S':
        char = 'a'
    elif char == 'E':
        char = 'z'
    return ord(char) - 97

with open('../input/day12.in') as f:
    grid = [line.strip() for line in f]

# Start = 20, 0
# End = 20, 43
nodes = set()
G = nx.DiGraph()
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        node = f'{x},{y}'
        if node not in nodes:
            nodes.add(node)
            G.add_node(node)
        neighbours = find_climbable(x, y)
        for neighbour in neighbours:
            if neighbour not in nodes:
                nodes.add(neighbour)
            G.add_edge(node, neighbour)

print(nx.shortest_path(G, '0,20', '43,20'))
