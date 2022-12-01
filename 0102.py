# By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

# To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

# In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

# https://adventofcode.com/2022/day/1#part2

from functools import reduce

def getMax(a,b):
  return max(int(a),int(b))

def sum(a,b):
  return int(a)+int(b)

def convertToSums(elf):
  elf = elf.split('\n')
  elf = list(map(lambda x: int(x), elf))
  return reduce(sum, elf)

with open('./inputs/0101.txt') as f:
  data = f.read().strip()

data = data.split('\n\n')
elfSums = list(map(convertToSums, data))
elfSums = sorted(elfSums)
topThree = reduce(sum, elfSums[-3:])
print(topThree)
