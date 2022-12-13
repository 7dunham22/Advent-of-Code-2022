import functools

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

packets = []
for [a,b] in pairs:
  packets.append(eval(a))
  packets.append(eval(b))

packets.append([[2]])
packets.append([[6]])

def compare(a,b):
  if isinstance(a, list) and isinstance(b, list):
    for i in range(len(a)):
      if i == len(b):
        return 1
      comp = compare(a[i], b[i])
      if comp < 0:
        return -1
      if comp > 0:
        return 1
    if len(a) < len(b):
      return -1
    return 0
  if isinstance(a, list):
    return compare(a, [b])
  if isinstance(b, list):
    return compare([a], b)
  return a-b

packets = sorted(packets, key=functools.cmp_to_key(compare))

res = 1
for i in range(len(packets)):
  packet = packets[i]
  if packet == [[2]] or packet == [[6]]:
    res *= i+1

print(res)
