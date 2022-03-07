import sys
m = 1

for _ in range(3):
  m *= int(sys.stdin.readline().rstrip())
m = str(m)
l = {}
for i in range(10):
  l[i] = 0

for n in m:
  l[int(n)] += 1

for i in range(10):
  print(l[i])