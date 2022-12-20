# Advent of Code
# Day 4 Part 1

def split_pair(line):
    return line.split(",")

def is_contained(elf1, elf2):
    elf1_list = [int(x) for x in elf1.split("-")]
    elf2_list = [int(x) for x in elf2.split("-")]
    set1 = {*range(elf1_list[0], elf1_list[1] + 1)}
    set2 = {*range(elf2_list[0], elf2_list[1] + 1)}
    if set1.issubset(set2) or set2.issubset(set1):
        return True
    else:
        return False

total = 0

with open('text.txt') as file:
    lines = file.read().splitlines()
    for pair in lines:
        elf1, elf2 = split_pair(pair)
        if is_contained(elf1, elf2):
            total += 1
            
print(f"The total is: {total}")
