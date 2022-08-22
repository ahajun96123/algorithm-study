import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().split())

n, m = input()
l = [[10**6]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a, b = input()
  l[a][b] = 1
  l[b][a] = 1
for i in range(1, n+1):
  l[i][i] = 0

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      l[i][j] = min(l[i][k]+l[k][j], l[i][j])
idx = 0
mhap = 10**7
for i in range(1, n):
  t = sum(l[i])
  if mhap > t:
    mhap = t
    idx = i
    
print(idx)