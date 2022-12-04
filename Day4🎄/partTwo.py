overlapCount = 0

with open("Day4/input.txt") as input:
  for pair in input:
    pair = pair.strip("\n").split(",")
    elfGroup = []
    for item in pair: 
      elfGroup.append(item.split("-"))

    print(elfGroup)

    a = int(elfGroup[0][0])
    b = int(elfGroup[0][1])
    c = int(elfGroup[1][0])
    d = int(elfGroup[1][1])

    firstCheck = (a >= c) and (a <= d)
    secondCheck = (b >= c) and (b <= d)
    thirdCheck = (c >= a) and (c <= b)
    fourthCheck = (d <= a) and (d >= b)

    if(firstCheck or secondCheck or thirdCheck or fourthCheck):
      overlapCount+=1

print(overlapCount)