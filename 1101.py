"""https://adventofcode.com/2022/day/11"""

from collections import deque
import math

with open('./inputs/1101.txt') as f:
  data = f.read().strip()

# data = """
# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1"""

data = list(map(lambda x: x.split('\n'), data.split('\n\n')))

class Monkey:
  def __init__(self) -> None:
    self.items = []
    self.operator = None
    self.operatorValue = None
    self.divisibilityVal = None
    self.throwIfTrue = None
    self.throwIfFalse = None
    self.inspectionCount = 0

  def operation(self, old):
    self.inspectionCount += 1
    val = self.operatorValue
    if self.operatorValue == 'old':
      val = old
    if self.operator == '+':
      return old + int(val)
    return old * int(val)

  def test(self, item):
    if item % self.divisibilityVal == 0:
      return self.throwIfTrue
    return self.throwIfFalse

monkeys = []
for item in data:
  monkey = Monkey()
  for line in item:
    if 'Starting items:' in line:
      items = line[17:]
      items = items.split(', ')
      items = deque(map(lambda x: int(x), items))
      monkey.items = items
    elif 'Operation' in line:
      if '*' in line:
        monkey.operator = '*'
        monkey.operatorValue = line.split(' ')[-1]
      else:
        monkey.operator = '+'
        monkey.operatorValue = line.split(' ')[-1]
    elif 'Test' in line:
      monkey.divisibilityVal = int(line.split(' ')[-1])
    elif 'true' in line:
      monkey.throwIfTrue = int(line.split(' ')[-1])
    elif 'false' in line:
      monkey.throwIfFalse = int(line.split(' ')[-1])
  monkeys.append(monkey)

for i in range(20):
  for monkey in monkeys:
    while len(monkey.items) > 0:
      item = monkey.items.popleft()
      item = monkey.operation(item)
      item = item // 3
      newMonkey = monkey.test(item)
      monkeys[newMonkey].items.append(item)

inspections = list(map(lambda monkey: monkey.inspectionCount, monkeys))
inspections.sort()
print(inspections[-1] * inspections[-2])
