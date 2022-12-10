#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:05:20 2022

@author: dennis
"""

class Computer:
    
    def __init__(self, file_path):
        self.cycle = 1
        self.x = 1
        self.during = [1]
        
        with open(file_path) as f:
    
    def step(self, instruction):
        command = instruction[0]
        if command == 'noop':
            self.noop()
        elif command == 'addx':
            self.addx(int(instruction[1]))

    def noop(self):
        self._save_state()
        self.cycle += 1

    def addx(self, v):
        self.cycle += 1
        self._save_state()
        self._save_state()
        self.x += v
    
    def draw(self):
        row = ''
        for cycle in range(1, 241):
            x = self.during[cycle]
            if cycle % 40 in range(x, x+3):
                row += '#'
            else:
                row += '.'
            if cycle % 40 == 0:
                print(row)
                row = ''

    def _save_state(self):
        self.during.append(self.x)

computer = Computer('../input/day10.in')
for instruction in computer.instructions:
    computer.step(instruction)

print('Part 1:', sum(computer.during[cycle]*cycle for cycle in range(20, 221, 40)))
computer.draw()
