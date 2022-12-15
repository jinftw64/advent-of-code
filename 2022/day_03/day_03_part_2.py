# Advent of Code 2022
# Day 03 Part 2

import string
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)

list_3_lines = []

with open('text.txt') as file:
    lines = file.read().splitlines()

# remove print debug function and 
# implement intersect method 
for line in lines:
    if len(list_3_lines) == 3:
        print(f"This is a set {list_3_lines}")
        list_3_lines = []
    else:
        list_3_lines.append(set(line))
