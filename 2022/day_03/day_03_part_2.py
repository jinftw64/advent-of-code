# Advent of Code 2022
# Day 03 Part 2

import string
from itertools import zip_longest

alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)

total = 0

def lower_convert(character):
    if character.islower():
        for value, letter in enumerate(alphabet_lower, 1):
            if character == letter:
                return value
    else:
        for value, letter in enumerate(alphabet_upper, 27):
            if character == letter:
                return value

def group_lines(iterable, n, fillvalue = None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue = fillvalue)

with open('text.txt') as file:
    lines = file.read().splitlines()
    print(list(group_lines(lines, 3)))

print(f"The total is: {total}")
