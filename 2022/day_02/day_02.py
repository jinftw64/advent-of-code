# Advent of Code 2022 Day 02
# Part 1

with open('text.txt') as file:
    strategy_guide = [line.split() for line in file]

def convert(letter):
    if letter in {"A", "X"}:
        return 1
    elif letter in {"B", "Y"}:
        return 2
    elif letter in {"C", "Z"}:
        return 3

def round(row):
    return convert(row[1]) - convert(row[0])

def subtotal(row):
    if round(row) in {-2, 1}:
        return convert(row[1]) + 6
    elif round(row) in {-1, 2}:
        return convert(row[1]) + 0
    elif round(row) == 0:
        return convert(row[1]) + 3

total = 0

for row in strategy_guide:
    total += subtotal(row)

print(f"Total of all rounds: {total}")

# part 2

condition = {
        "X": 0,
        "Y": 3,
        "Z": 6
        }


