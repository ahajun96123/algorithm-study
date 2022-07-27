import sys
sys.setrecursionlimit(int(1e6))

input = lambda: sys.stdin.readline().rstrip()

dr = [1, 1, 1, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(r, c):

  l[r][c] = 0
  for i in range(8):
    nr, nc = r+dr[i], c+dc[i]
    if nr<0 or nc<0 or nr>=h or nc>=w or l[nr][nc]==0: continue
    dfs(nr, nc)

while 1:
  cnt = 0
  w, h = map(int, input().split())
  if w==0 and h==0: break
  l = [list(map(int, input().split())) for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if l[i][j] == 1:
        dfs(i, j)
        cnt += 1
  print(cnt)
  