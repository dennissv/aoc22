#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:17:09 2022

@author: dennis
"""

from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def as_string(self):
        return f'{self.x},{self.y}'

class Rope:

    def __init__(self, n):
        self.knots = [Position(0, 0) for _ in range(n)]
        self.direction_dict = {'U': Position(0, 1),
                               'D': Position(0, -1),
                               'L': Position(-1, 0),
                               'R': Position(1, 0)}
        self.visited = set()

    def step(self, direction):
        self.move_head(direction)
        self.move_tails()
        self.save_tail_position()

    def move_head(self, direction):
        self.knots[0] += self.direction_dict[direction]

    def move_tails(self):
        for i in range(1, len(self.knots)):
            dx, dy = self._distance(i)
            if (abs(dx) == 2) or (abs(dy) == 2):
                if self.knots[i].x < self.knots[i-1].x:
                    self.knots[i].x += 1
                elif self.knots[i].x > self.knots[i-1].x:
                    self.knots[i].x -= 1
                if self.knots[i].y < self.knots[i-1].y:
                    self.knots[i].y += 1
                elif self.knots[i].y > self.knots[i-1].y:
                    self.knots[i].y -= 1

    def save_tail_position(self):
        self.visited.add(self.knots[-1].as_string())

    def _distance(self, i):
        return self.knots[i-1].x - self.knots[i].x, self.knots[i-1].y - self.knots[i].y

with open('../input/day9.in') as f:
    instructions = [line.strip().split() for line in f]

rope1 = Rope(2)
rope2 = Rope(10)
visited = set()
for instruction in instructions:
    direction, steps = instruction
    for _ in range(int(steps)):
        rope1.step(direction)
        rope2.step(direction)

print('Part 1:', len(rope1.visited))
print('Part 2:', len(rope2.visited))
