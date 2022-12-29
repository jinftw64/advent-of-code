# Advent of Code 2023
# Day 5 Part 1

import re

def main():
    stacks = []
    row = []
    moves = []

# stack parser
    with open("stacks.txt") as file:
        lines = file.read().splitlines()
        for line in lines:
            row = []
            for i in range(9):
                row.append(line[(i * 4):(i * 4 + 3)])
            stacks.append(row)

# move parser
    with open("text.txt") as file:
        lines = file.read().splitlines()
        for line in lines:
            move = re.findall(r'\d+', line)
            moves.append(move)

    def is_top(column):
        for num, row in enumerate(stacks):
            if row[column].isspace() and not stacks[num + 1][column].isspace():
                return stacks[num + 1].pop(column - 1)

    for move in moves:
        count, source, destination = map(int(), move)
        container = None
        while count > 0:
            if container:
                pass
            else:
                if is_top(source):
