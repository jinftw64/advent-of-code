# Advent of Code 2022
# Day 03 Part 2

import string
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)

def lower_convert(character):
    if character.islower():
        for value, letter in enumerate(alphabet_lower, 1):
            if character == letter:
                return value
    else:
        for value, letter in enumerate(alphabet_upper, 27):
            if character == letter:
                return value

list_3_lines = []
total = 0

with open('text.txt') as file:
    lines = file.read().splitlines()

# remove print debug function and 
# implement intersect method 
for line in lines:
    if len(list_3_lines) == 3:
        common_letter = list_3_lines[0].intersection(list_3_lines[1], list_3_lines[2])
        total += lower_convert(common_letter[0])
        list_3_lines = []
    else:
        list_3_lines.append(set(line))

print(f"The total is: {total}")
