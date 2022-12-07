#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:51:12 2022

@author: dennis
"""

# import time
# import os
# import random

# def generate_colors(stars):
#     return ''.join(random.choices(["\033[31m*", "\033[32m*", "\033[0m*"], weights=[1, 5, 1], k=stars))

# def print_tree(n_lines):
#     for line_number in range(1, n_lines*2, 2):
#         spaces = (7 - line_number) // 2
#         print(f"{' ' * spaces}{generate_colors(line_number)}{' ' * spaces}")
#     print("\033[33m   *")

# while True:
#     os.system("clear" if os.name == "posix" else "cls")
#     print_tree(4)
#     time.sleep(0.5)

# import time
# import os
# import random

# def generate_colors(stars):
#     # Generate the colors for the '*' in the line
#     return ''.join(random.choices(["\033[31m*", "\033[32m*", "\033[0m*"], weights=[1, 5, 1], k=stars))

# def print_tree(n_lines):
#     for line_number in range(1, n_lines*2, 2):
#         spaces = (7 - line_number) // 2
#         print(f"{' ' * spaces}{generate_colors(line_number)}{' ' * spaces}")
#     print("\033[33m   *")

# while True:
#     os.system("clear" if os.name == "posix" else "cls")

#     # Generate multiple trees of different sizes
#     for i in range(3):
#         for j in range(3):
#             print_tree(3 - i)
#         print()
#     print()

#     time.sleep(0.5)

import time
import os
import random

def generate_colors(stars):
    # Generate the colors for the '*' in the line
    return ''.join(random.choices(["\033[31m*", "\033[32m*", "\033[0m*"], weights=[1, 5, 1], k=stars))

def add_tree(grid, x, y, n_lines):
    for line_number in range(1, n_lines*2, 2):
        spaces = (7 - line_number) // 2
        if x + line_number - 1 < len(grid) and y + spaces < len(grid[0]):
            grid[x + line_number - 1][y + spaces] = generate_colors(line_number)
    if x + n_lines - 1 < len(grid) and y + 3 < len(grid[0]):
        grid[x + n_lines - 1][y + 3] = "\033[33m*"

while True:
    os.system("clear" if os.name == "posix" else "cls")

    # Generate a random grid of trees
    grid_size = 100
    grid = [[" " for _ in range(grid_size)] for _ in range(grid_size)]
    for i in range(3):
        n_lines = 5 - random.randint(0, 2)
        x = random.randint(n_lines, grid_size - 1 - n_lines)
        y = random.randint(n_lines, grid_size - 1)
        # if grid[x][y] == " " and x + n_lines - 1 < len(grid) and y + 3 < len(grid[0]):
        add_tree(grid, x, y, n_lines)

    # Print the grid of trees
    for row in grid:
        print(''.join(row))

    time.sleep(0.5)
