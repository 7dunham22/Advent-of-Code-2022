"""
https://adventofcode.com/2022/day/10
"""

with open('./inputs/1001.txt') as f:
  data = f.read().strip()

commands = data.splitlines()

X = 1
checks = set([20, 60, 100, 140, 180, 220])
nextCycle = []
res = 0
cycle = 1

i = 0
while i < len(commands):
  if cycle in checks:
    res += X * cycle
  cmd = commands[i]
  if len(nextCycle) > 0:
    X += nextCycle.pop()
  else:
    if 'noop' not in cmd:
      [_, val] = cmd.split(' ')
      nextCycle.append(int(val))
    i += 1
  cycle += 1

if len(nextCycle) > 0:
  if cycle in checks:
    res += X * cycle
  X += nextCycle.pop()
  cycle += 1

print(res)
