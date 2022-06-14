import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
cnt = 0
ans_cnt = 0
ans_l = []

def dfs(r, c):
  global cnt
  if r<0 or r>=n or c<0 or c>=n or graph[r][c]==0: return
  cnt += 1
  graph[r][c] = 0
  for i in range(4):
    dfs(r+dr[i], c+dc[i])

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      dfs(i, j)
      ans_cnt += 1
      ans_l.append(cnt)
      cnt = 0
print(ans_cnt)
ans_l.sort()
print(*ans_l, sep='\n')