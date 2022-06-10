# https://youtu.be/acqm9mM1P6o?t=3322
# 다익스트라 문제는 생각 좀 해야함.
# 테스트케이스 2개
# 3 2 1
# 1 2 4
# 1 3 2
# :2 4
# 6 11 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# :5 4

import heapq as hq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b, dist = map(int, input().split())
  graph[a].append((b, dist))
graph[c]
ans = [INF]*(n+1)

q = []
hq.heappush(q, (0, c))
while q:
  # 우선순위큐에서 하나 꺼내서
  cur_e, cur_v = hq.heappop(q)
  if ans[cur_v] <= cur_e: continue
  # 방문 안 했거나 큐에서 꺼낸 값이 더 작으면 그것을 저장.    
  ans[cur_v] = cur_e
  # 해당 v의 값이 가장 작기 때문에 연결된 간선을 모두 큐에 넣음.
  for v, e in graph[cur_v]:
    hq.heappush(q, (cur_e+e, v))
# 못 가는곳 제외(거리가 무한)
ans = list(filter(lambda x: x!=INF, ans))
# 자기 자신(거리0)은 제외
print(len(ans)-1, max(ans))
