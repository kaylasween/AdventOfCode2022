# A = X = Rock = 1
# B = Y = Paper = 2
# C = Z = Scissors = 3

# Winning = 6
# Draw = 3
# Losing = 0

# Score for a round is move + outcome

totalScore = 0

with open("Day2/input.txt") as f:
  
  
  for round in f:
    moves = round.strip("\n").split(" ")
    scores = []
    roundScore = 0
    
    for move in moves:
      if move == "A" or move == "X":
        scores.append(1)
      elif move == "B" or move == "Y":
        scores.append(2)
      elif move == "C" or move == "Z":
        scores.append(3)

    if scores[0] > scores[1]:
      roundScore = scores[1] 
      print("lost: ", roundScore)
    elif scores[0] == scores[1]:
      roundScore = scores[1] + 3
      print("tie: ", roundScore)
    elif scores[0] < scores[1]: 
      roundScore = scores[1] + 6
      print("win: ", roundScore)

    totalScore = totalScore + roundScore
    print("running total: ", totalScore)
    

  print(totalScore)
