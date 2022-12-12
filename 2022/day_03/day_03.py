# Advent of Code 2022
# Day 3 Part 1

import string
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)

alphabet_lower = list(enumerate(alphabet_lower, 1))
alphabet_upper = list(enumerate(alphabet_upper, 27))

print(alphabet_lower)
