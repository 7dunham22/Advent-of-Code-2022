with open('./inputs/1401.txt') as f:
  data = f.read().strip()

# data = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9"""

rocks = data.splitlines()
rocks = list(map(lambda x: list(map(lambda y: list(map(lambda z: int(z), y.split(','))), x.split(' -> '))), rocks))

def getDimensions(rocks):
  minWidth = float('inf')
  maxWidth = 0
  maxDepth = 0
  for rockPath in rocks:
    for [start, end] in rockPath:
      if start < minWidth:
        minWidth = start
      if start > maxWidth:
        maxWidth = start
      if end > maxDepth:
        maxDepth = end
  return [minWidth, maxWidth, maxDepth]

[minWidth, maxWidth, maxDepth] = getDimensions(rocks)
minWidth -= 1
maxWidth += 1

cave = [['.' for x in range(maxWidth+1 - minWidth)] for _ in range(maxDepth+1)]
n = len(cave)
m = len(cave[0])

def buildRockPath(rockPath):
  for i in range(len(rockPath)-1):
    [startCol, startRow] = rockPath[i]
    [endCol, endRow] = rockPath[i+1]
    startCol -= minWidth
    endCol -= minWidth
    if startCol == endCol:
      for r in range(min(startRow, endRow), max(startRow, endRow) + 1):
        cave[r][startCol] = '#'
    else:
      for c in range(min(startCol, endCol), max(startCol, endCol) + 1):
        cave[startRow][c] = '#'

for rockPath in rocks:
  buildRockPath(rockPath)

sandStart = [0, 500 - minWidth]

def fallSand(r, c):
  if r == n-1:
    return True
  if cave[r+1][c] != 'o' and cave[r+1][c] != '#':
    return fallSand(r+1,c)
  if c > 0 and cave[r+1][c-1] != 'o' and cave[r+1][c-1] != '#':
    return fallSand(r+1,c-1)
  if c < m-1 and cave[r+1][c+1] != 'o' and cave[r+1][c+1] != '#':
    return fallSand(r+1,c+1)
  cave[r][c] = 'o'
  return False

def getMinAbyss():
  res = 0
  while True:
    isInAbyss = fallSand(sandStart[0], sandStart[1])
    if isInAbyss:
      return res
    res += 1

print(getMinAbyss())
