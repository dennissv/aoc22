#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:48:13 2022

@author: dennis
"""

import re
import os
import time
from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int

class Crane:
    
    def __init__(self, crates, instructions):
        self.crates = crates
        self.is_lifting = False
        self.is_in_position = False
        self.been_at_top = False
        self.lifted_crate = ''
        
        self.max_height = sum(len(crate) for crate in crates) + 3
        self.current_max_height = self._get_current_max_height()
        self.pos = Position(0, 5)
        self._update_grid()
    
    def _get_current_max_height(self):
        return max(len(col) for col in self.crates)
    
    def _update_grid(self):
        self.grid = [[' ' for _ in range(9)] for _ in range(self.max_height)]
        for n, col in enumerate(crates):
            for i, crate in enumerate(col):
                self.grid[i][n] = crate
    
    def next_instruction(self):
        pass
    
    def _move(self, x, y):
        self.is_in_position = False
        self.been_at_top = False
        while not self.is_in_position:
            if not self.been_at_top:
                self.pos.y += 1
                if self.pos.y == self.current_max_height + 2:
                    self.been_at_top = True
            elif self.been_at_top and self.pos.y > y and self.pos.x == x:
                self.pos.y -= 1
            elif self.pos.x < x:
                self.pos.x += 1
            elif self.pos.x > x:
                self.pos.x -= 1
            else:
                self.is_in_position = True
            self.visualize()

    def step(self, instruction):
        numbers = re.findall(r'\d+', instruction)
        n, from_, to = [int(num) for num in numbers]

        for _ in range(n):
            self._move(from_ - 1, len(crates[from_ - 1]))
            
            self.lifted_crate = self.crates[from_ - 1].pop()
            self.is_lifting = True
            self._move(to - 1, len(crates[to - 1]) + 1)
            
            self.crates[to - 1].append(self.lifted_crate)
            self.lifted_crate = ''
            self.is_lifting = False

        # self._move(Position(3, 12))
        # self.lifted_crate = self.crates[3].pop()
        # self.is_lifting = True
        # self._move(Position(8, 7))
        # self.crates[-1].append(self.lifted_crate)
        # self.is_lifting = False
        # self.lifted_crate = ''
        # self._move(Position(3, 12))

    def move_crate(self):
        pass

    def _add_crane(self):
        crane_symbol = '*'
        if crane.is_lifting:
            crane_symbol = '\033[32m' + crane_symbol + '\033[0m'
            self.grid[self.pos.y-1][self.pos.x] = '\033[32m' + self.lifted_crate + '\033[0m'
        self.grid[self.pos.y][self.pos.x] = crane_symbol

    def visualize(self):
        os.system("clear" if os.name == "posix" else "cls")
        
        self._update_grid()
        self._add_crane()
        
        # Flip grid instead of worrying about y coordinates being in reverse
        for row in self.grid[::-1]:
            row = ' '+ ' '.join(row) + ' '
            print(row)
        
        # self._remove_crane()
        self._update_grid()
        time.sleep(0.005)

with open('../input/day5.in') as f:
    lines = [line.rstrip('\n') for line in f]

crates = [[] for _ in range(9)]
for line in lines[:8][::-1]:
    line = line.replace('    ', '[ ]')
    symbols = re.findall(r'\[(.*?)\]', line)
    for i, symbol in enumerate(symbols):
        if symbol != ' ':
            crates[i].append(symbol)

for instruction in lines[10:]:
    numbers = re.findall(r'\d+', instruction)
    n, from_, to = [int(num) for num in numbers]
    for _ in range(n):
        crates[to - 1].append((crates[from_ - 1].pop()))

crane = Crane(crates, lines[10:])
# crane.visualize()
# crane._move(Position(3, 50))
for instruction in lines[10:]:
    crane.step(instruction)
