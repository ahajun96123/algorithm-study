import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())


def dfs(no, clr):
  v[no] = clr
  q = e[no]
  for i in q:
    if v[i] == clr: return 0
    if v[i]: continue
    
    if not dfs(i, -clr): return 0
  return 1


for _ in range(n):
  nv, ne = map(int, input().split())
  e = [[] for _ in range(nv+1)]
  for _ in range(ne):
    a, b = map(int, input().split())
    e[a].append(b)
    e[b].append(a)
  v = [0]*(nv+1)
  bin = 1
  for i in range(1, nv+1):
    if v[i]: continue
    bin *= dfs(i, 1)
    if not bin: break
  
  if nv==0 and ne==0: print('NO')
  else: print('YES' if bin else 'NO')