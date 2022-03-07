import sys
l = []

for _ in range(9):
  l.append(int(sys.stdin.readline().rstrip()))

biggest = max(l)
idx = l.index(biggest)+1

print(biggest, idx)