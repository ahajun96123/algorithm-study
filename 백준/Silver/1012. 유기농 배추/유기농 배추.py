import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dh = [1, -1, 0, 0]
dv = [0, 0, 1, -1]

def dfs(h, v):
  # h, v가 graph의 인덱스를 벗어나는경우나 해당 장소를 이미 방문한 경우 return
  if h<0 or h>=h_n or v<0 or v>=v_n or not graph[h][v]: return
  graph[h][v] = 0
  for i in range(4):
    dfs(h+dh[i], v+dv[i])

for _ in range(int(input())):
  h_n, v_n, k_n = map(int, input().split())
  graph = [[0]*v_n for _ in range(h_n)]
  cnt = 0
  for _ in range(k_n):
    a, b = map(int, input().split())
    graph[a][b] = 1
  for i in range(h_n):
    for j in range(v_n):
      if graph[i][j] == 1:
        dfs(i, j)
        cnt += 1
  print(cnt)