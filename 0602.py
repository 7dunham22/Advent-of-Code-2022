"""
Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
How many characters need to be processed before the first start-of-message marker is detected?
"""

with open('./inputs/0601.txt') as f:
  sequence = f.read().strip()

def getMessage():
  for i in range(13, len(sequence)-1):
    marker = set()
    isValid = True
    for j in range(i, i-14, -1):
      if sequence[j] in marker:
        isValid = False
        break
      marker.add(sequence[j])
    if isValid:
      return i + 1

print(getMessage())
