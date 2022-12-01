# day 01 of Advent of Code 2022!

# part 1

# open file and split by lines
with open('text.txt') as file:
    contents = file.read().splitlines()

# create class for variables and method 
class CalorieCounter:
    def __init__(self):
        self.elf_Calorie_Total = 0
        self.food_book = []
        self.top3_total = 0
    def update_total(self, calorie):
        self.elf_Calorie_Total += int(calorie)
    def add_top_3_elves(self):
        descending_list = sorted(self.food_book, reverse=True)[:3]
        self.top3_total = sum(descending_list)

# instantiate class
expedition = CalorieCounter()

# interate thru list, empty line will append current total and reset
# non-empty line will add value to total
for line in contents:
    if not line:
        expedition.food_book.append(expedition.elf_Calorie_Total)
        expedition.elf_Calorie_Total = 0
    else:
        expedition.update_total(line)

# print max value
print(f"Max value is: {max(expedition.food_book)}")


# part 2

# sort list by descending order and total top 3
expedition.add_top_3_elves
print(f"Total of Top 3 elves: {expedition.top3_total}")
