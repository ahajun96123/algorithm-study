import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
  if visit[v]: return
  visit[v] = 1
  for cv in graph[v]:
    dfs(cv)

vn, ev = map(int, input().split())
graph = [[] for _ in range(vn+1)]

for i in range(ev):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visit = [0]*(vn+1)
cnt = 0
for i in range(1, vn+1):
  if visit[i]: continue
  dfs(i)
  cnt += 1
print(cnt)