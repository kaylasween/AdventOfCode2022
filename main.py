import numpy as np

input = open("Day8/input.txt").read()
input = input.split("\n")

testInput = ["30373", "25512", "65332", "33549", "35390"]
testGrid = []
for line in testInput: 
  testGrid.append([*line])

testGrid = np.array(testGrid, dtype=int)

grid = []

for line in input:
  grid.append([*line])

grid = np.array(grid, dtype=int)

print(testGrid)

visible = 0

west = testGrid[y, :x]
east = testGrid[y, x + 1:]

for y,x in np.ndindex(testGrid.shape):
  tree = testGrid[y, x]
  west = all(tree > )
  east = all(tree > )
  north = all(tree > )
  south = all(tree > testGrid[y + 1:, x])
  
  if(north or south or east or west):
    visible += 1

print(visible)



