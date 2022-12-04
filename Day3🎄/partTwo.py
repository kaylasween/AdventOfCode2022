import string

values = dict()

letters = string.ascii_lowercase + string.ascii_uppercase

for index, letter in enumerate(letters):
  values[letter] = index + 1

prioritiesSum = 0
rucksacks = []
groupedRucksacks = []

with open("Day3/input.txt") as input:
  for rucksack in input:
    rucksacks.append(rucksack.strip("\n"))

  for i in range(0, len(rucksacks), 3):
    groupedRucksacks.append(list(rucksacks[i:i + 3]))

  for rucksack in groupedRucksacks:
    similarity = list(set(rucksack[0]) & set(rucksack[1])& set(rucksack[2]))[0]

    prioritiesSum = prioritiesSum + values[similarity]

  print(prioritiesSum)
