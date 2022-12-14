import numpy as np

input = open("Day8/input.txt").read()
input = input.split("\n")

grid = []

for line in input:
  grid.append([*line])

grid = np.array(grid, dtype=int)

visible = 0

for y,x in np.ndindex(grid.shape):
  tree = grid[y, x]
  west = all(tree > grid[y, :x])
  east = all(tree > grid[y, x + 1:])
  north = all(tree > grid[:y, x])
  south = all(tree > grid[y + 1:, x])
  
  if(north or south or east or west):
    visible += 1

print(visible)



