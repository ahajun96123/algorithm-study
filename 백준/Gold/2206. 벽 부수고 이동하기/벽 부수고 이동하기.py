import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
l = [input().rstrip() for _ in range(n)]
v = [ [[0]*m for _ in range(n)] ]
v.append([[0]*m for _ in range(n)])

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs():
  d_r, d_c = n-1, m-1
  # 좌표, cnt, 벽 뚫었는지 여부
  q = deque()
  q.append([(0, 0), 1, 0])
  bool = False
  while q:
    cor, cnt, b = q.popleft()
    r, c = cor
    if d_r==r and d_c==c:
      bool = True
      break
    for i in range(4):
      nb = b
      nr = r + dr[i]
      nc = c + dc[i]
      if nr<0 or nc<0 or nr>=n or nc>=m: continue
      if b and l[nr][nc]=='1': continue
      elif b==0 and l[nr][nc]=='1': nb=1
      if v[nb][nr][nc]: continue
      q.append([(nr, nc), cnt+1, nb])
      v[nb][nr][nc] = 1

  return cnt if bool else -1


print(bfs())