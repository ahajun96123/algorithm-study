import sys
inp = lambda: int(sys.stdin.readline())
n = inp()
d = [0]*(11)
d[3], d[2], d[1] = 4, 2, 1
for i in range(4, 11):
  d[i] = d[i-1] + d[i-2] + d[i-3]
for _ in range(n):
  print(d[inp()])