# 나동빈의 (이코테 2021 강의 몰아보기) 3. DFS & BFS
# https://youtu.be/7C9RgOcvkvo?t=2563
# 음료수 얼려먹기. DFS로 풀었음.

n, m = map(int, input().split())
cnt = 0
l = [list(map(int, input())) for _ in range(n)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
  global l, dr, dc, n, m
  l[r][c] = 1
  for i in range(4):
    nr, nc = r + dr[i], c + dc[i]
    if nr < n and nr >= 0 and nc < m and nc >= 0 and l[nr][nc] == 0: dfs(nr, nc)
  # else: cnt += 1

for r in range(n):
  for c in range(m):
    if l[r][c] == 0:
      dfs(r, c)
      cnt += 1
print(cnt)
