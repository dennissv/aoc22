#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:17:09 2022

@author: dennis
"""

def read_input(day):
    with open(f'input/day{day}.in') as f:
        return [line.strip() for line in f]
