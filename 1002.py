with open('./inputs/1001.txt') as f:
  data = f.read().strip()

commands = data.splitlines()
n = 6
m = 40

screen = [['.' for x in range(m)] for y in range(n)]

nextCycle = []
sprite = [0,1]
screen[0][0] = "#"
cmdIndex = 0

def moveSprite(distance):
  for i in range(abs(distance)):
    if distance < 0:
      sprite[1] -= 1
    else:
      sprite[1] += 1

for r in range(n):
  for c in range(m):
    if c == sprite[1]-1 or c == sprite[1] or c == sprite[1]+1:
      screen[r][c] = '#'
    cmd = commands[cmdIndex]
    if len(nextCycle) > 0:
      moveSprite(nextCycle.pop())
    else:
      if 'noop' not in cmd:
        [_, val] = cmd.split(' ')
        nextCycle.append(int(val))
      cmdIndex += 1

for row in screen:
  print("".join(row))
