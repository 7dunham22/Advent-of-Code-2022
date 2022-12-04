"""
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""

with open('./inputs/0401.txt') as f:
  data = f.read().strip()

pairs = list(map(lambda x: x.split(','), data.split('\n')))

res = 0
for [a,b] in pairs:
  [aStart, aEnd] = a.split('-')
  [bStart, bEnd] = b.split('-')
  aStart, aEnd, bStart, bEnd = [int(aStart), int(aEnd), int(bStart), int(bEnd)]
  if aStart <= bStart and aEnd >= bStart:
    res += 1
  elif aStart >= bStart and aStart <= bEnd:
    res += 1

print(res)
