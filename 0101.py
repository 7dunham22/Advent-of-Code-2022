# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

# https://adventofcode.com/2022/day/1

from functools import reduce

def getMax(a,b):
  return max(int(a),int(b))

def sum(a,b):
  return int(a)+int(b)

def getSum(elf):
  elf = elf.split('\n')
  elf = list(map(lambda x: int(x), elf))
  return reduce(sum, elf)

with open('./inputs/0101.txt') as f:
  data = f.read().strip()

data = data.split('\n\n')
data = reduce(getMax, list(map(getSum, data)))
print(data)
