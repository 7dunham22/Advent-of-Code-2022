"""
https://adventofcode.com/2022/day/9
Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?
"""

with open('./inputs/0901.txt') as f:
  data = f.read().strip()

# data = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""

data = data.split('\n')
moves = list(map(lambda x: x.split(' '), data))

head = [0,0]
tail = [0,0]
visited = set(['0:0'])

def moveHead(direction, distance):
  global head
  deltas = {
    'R': [1,0],
    'D': [0,-1],
    'L': [-1,0],
    'U': [0,1]
  }
  for _ in range(distance):
    delta = deltas[direction]
    head[0] += delta[0]
    head[1] += delta[1]
    moveTail()

def moveTail():
  global head
  global tail
  global visited
  xAbsDistance = abs(head[0] - tail[0])
  yAbsDistance = abs(head[1] - tail[1])
  xDistance = head[0] - tail[0]
  yDistance = head[1] - tail[1]
  if xAbsDistance == 0 and yAbsDistance > 0:
    if tail[1] > head[1]:
      tail[1] = head[1] + 1
    else:
      tail[1] = head[1] - 1
  elif yAbsDistance == 0 and xAbsDistance > 0:
    if tail[0] > head[0]:
      tail[0] = head[0] + 1
    else:
      tail[0] = head[0] - 1
  elif yAbsDistance > 1 and xAbsDistance == 1:
    tail[0] += xDistance
    if yDistance > 0:
      tail[1] += 1
    else:
      tail[1] -= 1
  elif xAbsDistance > 1 and yAbsDistance == 1:
    tail[1] += yDistance
    if xDistance > 0:
      tail[0] += 1
    else:
      tail[0] -= 1
  visited.add(str(tail[0]) + ':' + str(tail[1]))

for [direction, distance] in moves:
  moveHead(direction, int(distance))

print(len(visited))
