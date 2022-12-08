input = open("Day6/input.txt").read()

for index, character in enumerate(input):
  possibleStart = []
  for i in range(4):
    possibleStart.append(input[index+i])
  if(len(set(possibleStart)) == len(possibleStart)):
    print("YES!", index+4)
    break
