#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:33:17 2022

@author: dennis
"""

import math
from copy import deepcopy

class Monkey:

    def __init__(self, id_, starting_items, operation, test, if_true, if_false):
        self.id = id_
        self.items = starting_items
        self.operation, self.operation_value = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

monkeys = []
with open('../input/day11.in') as f:
    for _ in range(8):
        id_ = f.readline()[-3]
        items = [int(x.strip(',')) for x in f.readline().strip().split()[2:]]
        operation = f.readline().strip().split()[-2:]
        test = int(f.readline().strip().split()[-1])
        if_true = int(f.readline()[-2])
        if_false = int(f.readline()[-2])
        _ = f.readline()
        monkeys.append(Monkey(id_, items, operation, test, if_true, if_false))
monkeys2 = deepcopy(monkeys)

for r in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            if monkey.operation == '*':
                if monkey.operation_value.isnumeric():
                    item *= int(monkey.operation_value)
                else:
                    item *= item
            elif monkey.operation == '+':
                if monkey.operation_value.isnumeric():
                    item += int(monkey.operation_value)
                else:
                    item += item
            item = item // 3
            if not item % monkey.test:
                monkeys[monkey.if_true].items.append(item)
            else:
                monkeys[monkey.if_false].items.append(item)
            monkey.inspected += 1
        monkey.items = []

part1 = math.prod(sorted([monkey.inspected for monkey in monkeys], reverse=True)[:2])
print('Part 1:', part1)

product = math.prod(monkey.test for monkey in monkeys)
for r in range(10000):
    for monkey in monkeys2:
        for item in monkey.items:
            if monkey.operation == '*':
                if monkey.operation_value.isnumeric():
                    item *= int(monkey.operation_value)
                else:
                    item *= item
            elif monkey.operation == '+':
                if monkey.operation_value.isnumeric():
                    item += int(monkey.operation_value)
                else:
                    item += item
            item %= product
            if not item % monkey.test:
                monkeys2[monkey.if_true].items.append(item)
            else:
                monkeys2[monkey.if_false].items.append(item)
            monkey.inspected += 1
        monkey.items = []

part1 = math.prod(sorted([monkey.inspected for monkey in monkeys2], reverse=True)[:2])
print('Part 1:', part1)
