fullOverlapCount = 0

with open("Day4/input.txt") as input:
  for pair in input:
    pair = pair.strip("\n").split(",")
    elfGroup = []
    for item in pair: 
      elfGroup.append(item.split("-"))

    firstCheck = int(elfGroup[0][0]) <= int(elfGroup[1][0])
    secondCheck = int(elfGroup[0][1]) >= int(elfGroup[1][1])
    thirdCheck = int(elfGroup[0][0]) >= int(elfGroup[1][0])
    fourthCheck = int(elfGroup[0][1]) <= int(elfGroup[1][1])

    if((firstCheck and secondCheck) or (thirdCheck and fourthCheck)):
      fullOverlapCount+=1

print(fullOverlapCount)