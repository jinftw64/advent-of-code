# Advent of Code
# Day 4 Part 1

def split_pair(line):
    return line.split(",")

def create_sets(elf1, elf2):
    elf1_list = [int(x) for x in elf1.split("-")]
    elf2_list = [int(x) for x in elf2.split("-")]
    set1 = {*range(elf1_list[0], elf1_list[1] + 1)}
    set2 = {*range(elf2_list[0], elf2_list[1] + 1)}
    return set1, set2

def is_contained(set1, set2):
    if set1.issubset(set2) or set2.issubset(set1):
        return True
    else:
        return False

total = 0
overlap_total = 0

with open('text.txt') as file:
    lines = file.read().splitlines()
    for pair in lines:
        elf1, elf2 = split_pair(pair)
        set1, set2 = create_sets(elf1, elf2)
        if is_contained(set1, set2):
            total += 1
        elif bool(set1 & set2):
            overlap_total += 1

overlap_total += total

print(f"Total of pairs contained: {total}")
print(f"Total of any overlap: {overlap_total}")
