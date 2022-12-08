input = []

with open("Day5/input.txt") as file:
  for line in file: 
    if (line == '\n'):
      line = 'BREAK'
    input.append(line.strip('\n'))

  input = [l.split(',') for l in ','.join(input).split('BREAK')]

  initialState = input[0]
  instructions = input[1]

  initialState.pop()
  instructions.pop(0)

  crates = []
  crateStacks = []

  for row in initialState:
    crates.append([row[containers * 4 + 1] for containers in range(len(row) // 4 + 1)])
  
  crateStacks = [list("".join(stackCol)) for stackCol in zip(*crates)]

  for stack in crateStacks:
    stack[:] = [x for x in stack if x != ' ']
    stack.remove(stack[-1])

  for instruction in instructions:
    instruction = instruction.split(" ")
    howMany = int(instruction[1])
    startStackIndex = int(instruction[3]) - 1
    destStackIndex = int(instruction[5]) - 1
    
    if(howMany > len(crateStacks[startStackIndex])):
      howMany = len(crateStacks[startStackIndex])

    crateStacks[destStackIndex][0:0] = crateStacks[startStackIndex][0:howMany]

    for i in range(howMany):
      if(crateStacks[startStackIndex]):
        crateStacks[startStackIndex].pop(0)

  print(crateStacks)
  
  for stack in crateStacks:
    print(stack[0])
