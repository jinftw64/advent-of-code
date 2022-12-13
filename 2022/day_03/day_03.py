# Advent of Code 2022
# Day 3 Part 1

import string
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)

class Reorg:
    def __init__(self):
        self.total_points = 0

    @staticmethod
    def split_rucksack(string):
        return (string[:len(string)//2], string[len(string)//2:])

    @staticmethod
    def find_duplicate(tuple):
        for char in tuple[0]:
            if char in tuple[1]:
                return char

    def total(self, char):
        if char.islower():
            for value, letter in enumerate(alphabet_lower, 1):
                if char == letter:
                    self.total_points += value
        else:
            for value, letter in enumerate(alphabet_upper, 27):
                if char == letter:
                    self.total_points += value

Day_3 = Reorg()

with open('text.txt') as file:
    for line in file:


