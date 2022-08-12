import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)


parent = [0]*(n+1)
def dfs(srt):
  for i in tree[srt]:
    if parent[i]==0:
      parent[i] = srt
      dfs(i)


dfs(1)
for i in range(2, n+1): print(parent[i])