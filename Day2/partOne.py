# A = X = Rock = 1
# B = Y = Paper = 2
# C = Z = Scissors = 3

# Winning = 6
# Draw = 3
# Losing = 0

# Score for a round is move + outcome

totalScore = 0

scores = {
  "A X": 4,
  "A Y": 8,
  "A Z": 3,
  "B X": 1,
  "B Y": 5,
  "B Z": 9,
  "C X": 7,
  "C Y": 2,
  "C Z": 6
}
  

with open("Day2/input.txt") as f:
  for round in f:
    round = round.strip("\n")
    totalScore = totalScore + scores[round]

print(totalScore)
