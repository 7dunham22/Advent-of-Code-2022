"""
https://adventofcode.com/2022/day/7
"""
from functools import reduce

with open('./inputs/0701.txt') as f:
  data = f.read().strip()

commands = data.split('\n')

class Directory:
  def __init__(self, name) -> None:
    self.name = name
    self.size = None
    self.files = []
    self.subfolders = {}

class File:
  def __init__(self, name, size) -> None:
    self.name = name
    self.size = size

root = Directory('/')
hist = []

curr = root
for command in commands:
  if '$' in command:
    if 'cd' in command:
      target = command.split(' ')[2]
      if target == '/':
        curr = root
      elif target == '..':
        curr = hist.pop()
      else:
        hist.append(curr)
        curr = curr.subfolders[target]
  elif 'dir' in command:
    folder = command.split(' ')[1]
    if folder not in curr.subfolders:
      curr.subfolders[folder] = Directory(folder)
  else:
    [size, name] = command.split(' ')
    curr.files.append(File(name, int(size)))

res = 0

def calculateSize(folder: Directory):
  global res
  size = reduce(lambda a,b: a+b, [x.size for x in folder.files], 0)
  for subdirectory in folder.subfolders:
    size += calculateSize(folder.subfolders[subdirectory])
  folder.size = size
  if size <= 100000:
    res += size
  return size

calculateSize(root)
print(res)
