import sys
inp = lambda: int(sys.stdin.readline())
d = [[0]*2 for _ in range(41)]
d[0][0] = 1
d[1][1] = 1
l = [inp() for _ in range(inp())]
iter_n = max(l) + 1
for i in range(2, iter_n):
  for j in range(2):
    d[i][j] = d[i-1][j] + d[i-2][j]
for i in l: print(*d[i])