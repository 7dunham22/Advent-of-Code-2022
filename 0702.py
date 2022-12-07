"""
Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

Delete directory e, which would increase unused space by 584.
Delete directory a, which would increase unused space by 94853.
Delete directory d, which would increase unused space by 24933642.
Delete directory /, which would increase unused space by 48381165.
Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
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

def calculateSize(folder: Directory):
  size = reduce(lambda a,b: a+b, [x.size for x in folder.files], 0)
  for subdirectory in folder.subfolders:
    size += calculateSize(folder.subfolders[subdirectory])
  folder.size = size
  return size

calculateSize(root)

totalSpace = 70000000
reqSpace = 30000000
currFreespace = totalSpace - root.size

def getDeletionFolder(curr: Directory):
  if currFreespace + curr.size >= reqSpace:
    deletionSizes = [getDeletionFolder(curr.subfolders[folder]) for folder in curr.subfolders.keys()]
    deletionSizes = list(filter(lambda x: x != -1, deletionSizes))
    if len(deletionSizes) == 0:
      return curr.size
    return min(deletionSizes)
  return -1

print(getDeletionFolder(root))
