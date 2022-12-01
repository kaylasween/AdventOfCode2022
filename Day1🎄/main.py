weights = []
elfWeight = []

with open("input.txt") as f:
  for line in f:
    if (line != '\n'):
      elfWeight.append(int(line.strip('\n')))
    else:
      sum = 0
      for weight in elfWeight:
        sum = sum + weight
      weights.append(sum)
      elfWeight = []
  
  newWeights = sorted(weights, reverse=True)
  print(newWeights)

  threeSum = 0

  for number in newWeights[:3]:
    print(number)
    threeSum = threeSum + number

  print(threeSum)

# Part 1 
# highestWeight = 0

# for elf in weights:
#   sum = 0
#   for weight in elf:
#     sum = sum + weight
#   if (sum > highestWeight):
#     highestWeight = sum

# print(highestWeight)
