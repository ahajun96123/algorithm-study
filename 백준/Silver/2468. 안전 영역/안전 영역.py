import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

se = set()
n = int(input())
l = []
for i in range(n):
  tl = list(map(int, input().split()))
  l.append(tl)
  for j in range(n):
    se.add(tl[j])

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c, h):
  v[r][c] = 1
  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if nr<0 or nc<0 or nr>=n or nc >=n or l[nr][nc]<=h or v[nr][nc]: continue
    dfs(nr, nc, h)

se.add(0)
mcnt = 0
for h in sorted(list(se)):
  v = [[0]*n for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(n):
      if v[i][j] or l[i][j] <= h: continue
      dfs(i, j, h)
      cnt += 1
  mcnt = max(mcnt, cnt)

print(mcnt)