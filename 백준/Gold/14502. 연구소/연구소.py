import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
dh = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# 1을 (0,0)부터 차례로 놓고 감염부분 계산
# 
def count(h, c):
  if h<0 or h>=n or c<0 or c>=m or tl[h][c]>0: return 0
  tl[h][c] = 2
  cnt = 1
  for i in range(4):
    cnt += count(h+dh[i], c+dc[i])
  return cnt

# 벽을 세울 수 있는 부분(0인 부분)
z = [(i, j) for i in range(n) for j in range(m) if l[i][j]==0]
tw = [(i, j) for i in range(n) for j in range(m) if l[i][j]==2]
n_z = len(z)
mi = int(1e9)
for i in range(n_z-2):
  l[z[i][0]][z[i][1]] = 1
  for j in range(i+1, n_z-1):
    l[z[j][0]][z[j][1]] = 1
    for k in range(j+1, n_z):
      l[z[k][0]][z[k][1]] = 1
      tl = [t[:] for t in l]
      cnt = 0
      for t in tw:
        tl[t[0]][t[1]] = 0
        cnt += count(*t)
      cnt -= len(tw)
      # print(cnt)
      if cnt < mi: mi = cnt
      l[z[k][0]][z[k][1]] = 0
    l[z[j][0]][z[j][1]] = 0
  l[z[i][0]][z[i][1]] = 0
print(n_z - mi - 3)