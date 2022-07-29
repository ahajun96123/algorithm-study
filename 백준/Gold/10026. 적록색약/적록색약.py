import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = int(input())
l = []
l2 = []

for i in range(n):
  tl = list(input())
  l.append(tl[:])
  for j in range(n):
    t = tl[j]
    if t=='R' or t=='G':
      tl[j] = 'C'
  l2.append(tl)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(r, c, rgb):
  if r<0 or c<0 or r>=n or c>=n or l[r][c]!=rgb: return
  l[r][c] = 'a'
  for i in range(4):
    nr, nc = r+dr[i], c+dc[i]
    dfs(nr, nc, rgb)
    

cnt = 0
for i in range(n):
  for j in range(n):
    if l[i][j] != 'a':
      dfs(i, j, l[i][j])
      cnt += 1

l = l2

cnt2 = 0
for i in range(n):
  for j in range(n):
    if l[i][j] != 'a':
      dfs(i, j, l[i][j])
      cnt2 += 1

print(cnt, cnt2)