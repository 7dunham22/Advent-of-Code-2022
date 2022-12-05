"""
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
from collections import deque

with open('./inputs/0501.txt') as f:
  data = f.read().strip()

[ship, commands] = data.split('\n\n')

stacks = [[] for x in range(9)]
levels = ship.split('\n')
for i in range(len(levels)-1, -1, -1):
  level = levels[i]
  i = 0
  while i < len(level):
    if level[i] == '[':
      stacks[i//4].append(level[i+1])
    i += 4

commands = commands.split('\n')
for command in commands:
  moves = command.split(' ')
  moveQuant = int(moves[1])
  moveFrom = int(moves[3])
  moveTo = int(moves[5])
  crane = deque()
  for i in range(moveQuant):
    crane.appendleft(stacks[moveFrom - 1].pop())
  for i in range(moveQuant):
    stacks[moveTo - 1].append(crane.popleft())

res = ""
for stack in stacks:
  res += stack[-1]

print(res)
