# https://youtu.be/acqm9mM1P6o?t=3674
# 플로이드 워셜 알고리즘.


# 테스트 케이스
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# :3

import sys
INF = int(1e9)
auto = lambda: map(int, sys.stdin.readline().split())
n, m = auto()
graph = [[] for _ in range(n+1)]
dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
  a, b = auto()
  dist[a][b] = 1
  dist[b][a] = 1
x, k = auto()
for i in range(n+1):
  dist[i][i] = 0

for k in range(n+1):
  for i in range(n+1):
    for j in range(n+1):
      dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
ans = dist[1][k] + dist[k][x]
if INF <= ans: print(-1)
else: print(ans)
