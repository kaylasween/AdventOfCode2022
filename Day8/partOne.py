import numpy as np

testInput = ["30373", "25512", "65332", "33549", "35390"]
testGrid = []

for line in testInput: 
  testGrid.append([*line])

testGrid = np.array(testGrid, dtype=int)

input = open("Day8/input.txt").read()
input = input.split("\n")

grid = []

for line in input:
  grid.append([*line])

grid = np.array(grid, dtype=int)

def partOne(inputGrid):
  visible = 0
  for y,x in np.ndindex(inputGrid.shape):
    tree = inputGrid[y, x]
    west = all(tree > inputGrid[y, :x])
    east = all(tree > inputGrid[y, x + 1:])
    north = all(tree > inputGrid[:y, x])
    south = all(tree > inputGrid[y + 1:, x])

    if(north or south or east or west):
      visible += 1

  return visible

print(partOne(testGrid))
print(partOne(grid))

# Tests
def partOneTest(): 
  assert partOne(testGrid) == 21

partOneTest()
  


