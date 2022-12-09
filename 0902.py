with open('./inputs/0901.txt') as f:
  data = f.read().strip()

# data = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""

data = data.split('\n')
moves = list(map(lambda x: x.split(' '), data))

n = 10
knots = list(map(lambda x: [0,0], [None for i in range(n)]))
visited = set(['0:0'])

def moveHead(direction, distance):
  head = knots[0]
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
    moveTail(1)

def moveTail(knotIndex):
  global visited
  head = knots[knotIndex-1]
  tail = knots[knotIndex]
  xAbsDistance = abs(head[0] - tail[0])
  yAbsDistance = abs(head[1] - tail[1])
  xDistance = head[0] - tail[0]
  yDistance = head[1] - tail[1]

  # CASE 1: Head in lateral position. Move tail 1 over in whichever direction it moved.
  # a) vertical
  if xAbsDistance == 0 and yAbsDistance > 0:
    if tail[1] > head[1]:
      tail[1] = head[1] + 1
    else:
      tail[1] = head[1] - 1
  # b) horizontal
  elif yAbsDistance == 0 and xAbsDistance > 0:
    if tail[0] > head[0]:
      tail[0] = head[0] + 1
    else:
      tail[0] = head[0] - 1
  # CASE 2: Head moves into 'knight' position with abs distance [2,1] or [1,2]. Move tail to lateral position at whatever direction is at 2 abs diff.
  # a) vertical
  elif yAbsDistance > 1 and xAbsDistance == 1:
    tail[0] += xDistance
    if yDistance > 0:
      tail[1] += 1
    else:
      tail[1] -= 1
  # b) horizontal
  elif xAbsDistance > 1 and yAbsDistance == 1:
    tail[1] += yDistance
    if xDistance > 0:
      tail[0] += 1
    else:
      tail[0] -= 1
  # CASE 3: While the head can only move laterally, each tail can move diagonally, so account for case in which abs diff is [2,2]. If so, move to nearest diagonal position [1,1]
  elif xAbsDistance > 1 and yAbsDistance > 1:
    if yDistance > 0:
      tail[1] += 1
    else:
      tail[1] -= 1
    if xDistance > 0:
      tail[0] += 1
    else:
      tail[0] -= 1
  # Track only the last tail of the knots. Otherwise, move the next knot relative to the current knot's position.
  if knotIndex == n-1:
    visited.add(str(tail[0]) + ':' + str(tail[1]))
  else:
    moveTail(knotIndex+1)

for [direction, distance] in moves:
  moveHead(direction, int(distance))

print(len(visited))
