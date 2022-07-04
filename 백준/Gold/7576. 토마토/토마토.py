import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
nz = cz = 0
q = deque()
for i in range(n):
  for j in range(m):
    if l[i][j] == 1:
      l[i][j] = 0
      q.append((i, j, 0))
    elif l[i][j] == 0: nz += 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
  x, y, days = q.popleft()
  if x<0 or x>=n or y<0 or y>=m or l[x][y]!=0: continue
  if days!=0: cz += 1
  l[x][y] = 1
  for i in range(4):
    q.append((x+dx[i], y+dy[i], days+1))

if cz != nz: print(-1)
else: print(days-1)