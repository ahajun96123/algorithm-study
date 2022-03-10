import sys

s = sys.stdin.readline().rstrip()

d = {chr(i):-1 for i in range(ord('a'), ord('a')+26)}

for c in s:
  d[c] = s.index(c)

print(*d.values())