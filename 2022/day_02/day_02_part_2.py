# Advent of Code 2022
# Day 02 Part 2

with open ('text.txt') as file:
    strategy_guide = [line.split() for line in file]

class Game:
    win_against = {
            "A": 8,
            "B": 9,
            "C": 7
            }

    lost_against = {
            "A": 3,
            "B": 1,
            "C": 2
            }

    draw_against = {
            "A": 4,
            "B": 5,
            "C": 6
            }
    
    def points(self, list):
            player = list[1]
            elf = list[0]

            if player == "X":
                return Game.lost_against[elf]
            elif player == "Y":
                return Game.draw_against[elf]
            elif player == "Z":
                return Game.win_against[elf]

    def total(self, file):
        total_score = 0
        for line in file:
            total_score += Game.points(line)
        return total_score

day2part2 = Game()
print(f"Total score for Part 2: {day2part2.total(strategy_guide)}")
