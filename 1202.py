from collections import deque

with open('./inputs/1201.txt') as f:
  data = f.read().strip()

# data = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi"""

df = list(map(lambda x: list(x), data.splitlines()))
n = len(df)
m = len(df[0])

def getMinPath(sRow, sCol):
  queue = deque([[sRow, sCol, 'a', 0]])
  deltas = [[0,1], [1,0], [0,-1], [-1,0]]
  visited = set()
  while len(queue) > 0:
    [r,c,prev,dist] = queue.popleft()
    pos = str(r) + ":" + str(c)
    if r<0 or r==n or c<0 or c==m or pos in visited:
      continue
    curr = df[r][c]
    if curr == 'S':
      curr = 'a'
    elif curr == 'E':
      curr = 'z'
    if ord(curr) - ord(prev) > 1:
      continue
    if df[r][c] == 'E':
      return dist
    visited.add(pos)
    for [dr, dc] in deltas:
      r2 = r + dr
      c2 = c + dc
      queue.append([r2, c2, curr, dist+1])
  return float('inf')

def getBestPath(df):
  minPath = float('inf')
  for r in range(n):
    for c in range(m):
      if df[r][c] == 'S' or df[r][c] == 'a':
        minPath = min(minPath, getMinPath(r,c))
  return minPath

print(getBestPath(df))
