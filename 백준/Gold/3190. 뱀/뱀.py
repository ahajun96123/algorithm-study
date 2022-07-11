import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
l = [[0]*(n) for _ in range(n)]
for _ in range(int(input())):
  r, c = map(int, input().split())
  l[r-1][c-1] = 1
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r = c = cnt = dir = 0
br = False
q = deque()
q.append((0, 0))
l[0][0] = 2
dd = [input().rstrip().split() for _ in range(int(input()))]
# for _ in range(int(input())):
for con, d in dd:
  # con, d = input().rstrip().split()
  for i in range(int(con) - cnt):
    nr, nc = r + dr[dir], c + dc[dir]
    # print(cnt, nr, nc, q)
    # 벽이거나 자신일때
    if nr<0 or nr>=n or nc<0 or nc>=n or l[nr][nc]==2:
      br = True
      break
    # 사과가 아닐때
    if l[nr][nc]!=1:
      tr, tc = q.popleft()
      l[tr][tc] = 0
    l[nr][nc] = 2
    q.append((nr, nc))
    r, c = nr, nc
    cnt += 1
  # print('turn')
  if br: break

  if d=='D': dir = (dir + 1) % 4
  else: dir = (dir + 3) % 4

if not br:
  while 1:
    nr, nc = r + dr[dir], c + dc[dir]
    if nr<0 or nr>=n or nc<0 or nc>=n or l[nr][nc]==2: break
    if l[nr][nc]!=1:
      tr, tc = q.popleft()
      l[tr][tc] = 0
    l[nr][nc] = 2
    q.append((nr, nc))
    r, c = nr, nc
    cnt += 1

print(cnt+1)