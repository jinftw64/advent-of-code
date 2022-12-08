# Advent of Code 2022 Day 02
# Part 1

with open('text.txt') as file:
    strategy_guide = [line.split() for line in file]

class Game():
    win = {
            "X": "C", # rock: scissor
            "Y": "A", # paper: rock
            "Z": "B"  # scissor: paper
            }
    
    draw = {
            "X": "A", # rock
            "Y": "B", # paper
            "Z": "C"  # scissor
            }

    sign_points = {
            "X": 1,
            "Y": 2,
            "Z": 3
            }

    total_points = 0

    def points(self, list):
        player = list[1]
        elf = list[0]
        if (player, elf) in Game.draw.items():
            return Game.sign_points[player] + 3
        elif (player, elf) in Game.win.items():
            return Game.sign_points[player] + 6
        else:
            return Game.sign_points[player] + 0

part1 = Game()

for row in strategy_guide:
    part1.total_points += part1.points(row)

print(f"Total points for Part 1: {part1.total_points}")


