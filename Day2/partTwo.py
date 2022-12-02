# A = Rock = 1
# B = Paper = 2
# C = Scissors = 3

# Winning = 6
# Draw = 3
# Losing = 0

# X = lose
# Y = draw
# Z = win

# Score for a round is move + outcome

totalScore = 0

outcome = {
  "X": 0,
  "Y": 3,
  "Z": 6
}

moveScore = {
  "A": 1,
  "B": 2,
  "C": 3
}

winningMove = {
  "A": "B",
  "B": "C",
  "C": "A"
}
  

with open("Day2/input.txt") as f:
  for round in f:
    round = round.strip("\n").split(" ")
    moveNeeded = ""

    if round[1] == "Y":
      moveNeeded = round[0]
    elif round[1] == "Z":
      moveNeeded = winningMove[round[0]]
    else: 
      moveNeeded = list(winningMove.keys())[list(winningMove.values()).index(round[0])]
    
    totalScore = totalScore + outcome[round[1]] + moveScore[moveNeeded]

print(totalScore)
