import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
cors = []
l = [[0]*n for _ in range(m)]
for _ in range(k):
  c1, r1, c2, r2 = map(int, input().split())
  nr, nc = r2-r1, c2-c1
  for i in range(nr):
    for j in range(nc):
      l[r1+i][c1+j] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
  tcnt = 0
  l[r][c] = 1
  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if nr<0 or nc<0 or nr>=m or nc>=n or l[nr][nc]: continue
    tcnt += dfs(nr, nc)
  return tcnt+1


cnt = 0
area = []
for i in range(m):
  for j in range(n):
    if l[i][j]: continue
    cnt += 1
    area.append(dfs(i, j))
print(cnt)
print(*sorted(area))