#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:15:35 2022

@author: dennis
"""

class Folder:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.folders = dict()
        self.files = dict()

    def add_folder(self, name):
        self.folders[name] = Folder(name, self)

    def add_file(self, name, size):
        self.files[name] = size

    def get_size(self):
        size = sum(size for size in self.files.values())
        for folder in self.folders.values():
            size += folder.get_size()
        return size

    def traverse_all(self):
        folders = [self.get_size()]
        for folder in self.folders.values():
            folders += folder.traverse_all()
        return folders

root = Folder('/', None)
pwd = root
line_count = 0
with open('../input/day7.in') as f:
    for line in f.readlines()[2:]:
        line_count += 1
        line = line.rstrip()
        if line.startswith('$'):
            if line.startswith('$ cd'):
                name = line.split()[-1]
                if name == '..' and pwd.parent:
                    pwd = pwd.parent
                else:
                    pwd = pwd.folders[name]
        else:
            if line.startswith('dir'):
                name = line.split()[-1]
                pwd.add_folder(name)
            else:
                size, name = line.split()
                size = int(size)
                pwd.add_file(name, size)

folders = root.traverse_all()
print('Part 1:', sum(size for size in folders if size <= 100000))

unused_size = 70000000 - root.get_size()
minimum_size = 30000000 - unused_size
print('Part 2:', min(size for size in folders if size >= minimum_size))
