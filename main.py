import string

values = dict()

letters = string.ascii_lowercase + string.ascii_uppercase

for index, letter in enumerate(letters):
   values[letter] = index + 1

prioritiesSum = 0

with open("Day3/input.txt") as input:
  for rucksack in input:
    contents = rucksack.strip("\n")
    compartments = [contents[slice(0, len(contents)//2)], contents[slice(len(contents)//2, len(contents))]]

    similarity = list(set(compartments[0])&set(compartments[1]))[0]

    print(similarity)

    prioritiesSum = prioritiesSum + values[similarity]


print(prioritiesSum)
    