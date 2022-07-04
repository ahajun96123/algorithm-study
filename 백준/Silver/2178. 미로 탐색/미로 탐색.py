import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
l = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
def bfs():
  q = deque()
  q.append((0, 0, 1))
  while q:
    cx, cy, cnt = q.popleft()
    if cx<0 or cx>=n or cy<0 or cy>=m or l[cx][cy]==0: continue
    l[cx][cy] = 0
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      q.append((nx, ny, cnt+1))
    if cx==n-1 and cy==m-1:
      print(cnt)
      break
  
bfs()