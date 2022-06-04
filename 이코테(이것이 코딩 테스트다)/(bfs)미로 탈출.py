# 나동빈의 (이코테 2021 강의 몰아보기) 3. DFS & BFS
# https://youtu.be/7C9RgOcvkvo?t=3076
# 미로 탈출. BFS 문제인데 비효율적으로 DFS와 BFS를 섞어서 풀었음. 답안처럼 재귀함수 쓰지 않고 while queue로 풀 수 있음.

from collections import deque
q = deque()

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c, ans):
  global dr, dc, graph, n, m
  if r>=n or r<0 or c>=m or c<0 or graph[r][c]==0: return
  if r == n-1 and c == m-1:
    print(ans)
    raise Exception
  graph[r][c] = 0
  q.extend([(r+dr[i], c+dc[i], ans+1) for i in range(4)])
  for _ in range(4): bfs(*q.popleft())
  
try: bfs(0, 0, 1)
except: pass
