import sys
input = sys.stdin.readline
v_n = int(input())
e_n = int(input())
graph = [[] for _ in range(v_n+1)]
for i in range(e_n):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visit = [0]*(v_n+1)
cnt = 0

def dfs(v):
  global cnt
  if visit[v]: return
  cnt += 1
  visit[v] = 1
  for next in graph[v]:
    dfs(next)

dfs(1)
print(cnt-1)