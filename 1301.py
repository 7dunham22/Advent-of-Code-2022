from functools import reduce

with open('./inputs/1301.txt') as f:
  data = f.read().strip()

# data = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]"""

pairs = list(map(lambda x: x.splitlines(), data.split('\n\n')))

for pair in pairs:
  [a,b] = pair
  pair[0] = eval(a)
  pair[1] = eval(b)

def compare(a,b):
  if isinstance(a, list) and isinstance(b, list):
    for i in range(len(a)):
      if i == len(b):
        return -1
      comp = compare(a[i], b[i])
      if comp < 0:
        return -1
      if comp > 0:
        return 1
    if len(a) < len(b):
      return 1
    return 0
  if isinstance(a, list):
    return compare(a, [b])
  if isinstance(b, list):
    return compare([a], b)
  return b-a

res = 0
for i in range(len(pairs)):
  [a,b] = pairs[i]
  if compare(a,b) >= 0:
    res += i+1

print(res)
