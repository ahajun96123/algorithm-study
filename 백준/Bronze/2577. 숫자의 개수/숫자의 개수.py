import sys
m = 1

for _ in range(3):
  m *= int(sys.stdin.readline().rstrip())
m = str(m)
l = [0 for _ in range(10)]

for n in m:
  l[int(n)] += 1

for i in l:
  print(i)