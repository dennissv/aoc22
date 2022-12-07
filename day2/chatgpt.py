#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:41:39 2022

@author: dennis
"""

# Create a dictionary mapping each hand shape to its score
HANDS = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

# Read the strategy guide from the input
strategy = []
# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     strategy.append(line)

with open('../input/day2.in') as f:
    for line in f:
        strategy.append(line)

# Calculate the total score by iterating over the strategy guide
total_score = 0
for line in strategy:
    opponent, hand = line.strip().split()

    # Calculate the outcome of the round
    if opponent == hand:
        outcome = 3
    elif (HANDS[opponent] + 1) % 3 == HANDS[hand]:
        outcome = 6
    else:
        outcome = 0

    # Calculate the score for the round and add it to the total score
    total_score += HANDS[hand] + outcome

# Print the total score
print(total_score)
