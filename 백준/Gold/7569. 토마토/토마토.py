import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n, h = map(int, input().split())

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

cnt = 0
def bfs(ones):
  global cnt, cz
  cnt += 1
  q = []
  for one in ones:
    z, x, y = one
    for i in range(6):
      nz, nx, ny = z+dz[i], x+dx[i], y+dy[i]
      if nz<0 or nx<0 or ny<0 or nz>=h or nx>=n or ny>=m or l[nz][nx][ny]!=0: continue
      l[nz][nx][ny] = 1
      cz -= 1
      q.append((nz, nx, ny))
  if q: bfs(q)

l = []
ones = []
cz = 0
for k in range(h):
  tl = []
  for i in range(n):
    tl2 = list(map(int, input().split()))
    for j in range(m):
      if tl2[j] == 0: cz+=1
      if tl2[j] == 1: ones.append((k, i, j))
    tl.append(tl2)
  l.append(tl)

bfs(ones)
if cz == 0: print(cnt-1)
else: print(-1)
