import sys
from collections import deque
input = sys.stdin.readline
v_n, e_n, v_start = map(int, input().split())
graph = [[] for _ in range(v_n+1)]
for _ in range(e_n):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
v_check = [0]*(v_n+1)

def dfs(v):
  if v_check[v]: return
  print(v, end=' ')
  v_check[v] = 1
  for i in sorted(graph[v]):
    dfs(i)

def bfs(v_s):
  q = deque()
  q.append(v_s)
  while q:
    v = q.popleft()
    if v_check[v]: continue
    print(v, end=' ')
    q.extend(sorted(graph[v]))
    v_check[v] = 1

dfs(v_start)
print()
v_check = [0]*(v_n+1)
bfs(v_start)