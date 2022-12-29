# Advent of Code 2022
# Day 5 Part 1

stacks = []
row = []

with open("stacks.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        row = []
        for i in range(9):
            row.append(line[(i * 3):(i * 3 + 4)])
        stacks.append(row)

for i in stacks:
    print(i)
