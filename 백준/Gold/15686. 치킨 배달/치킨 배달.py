import sys
from itertools import combinations as com
input = sys.stdin.readline
n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
two = []
one = []
for i in range(n):
  for j in range(n):
    if l[i][j] == 2:
      two.append((i, j))
      l[i][j] = 0
    elif l[i][j] == 1:
      one.append((i, j))

br = [[0]*len(two) for _ in range(len(one))]
for i in range(len(one)):
  ox, oy = one[i]
  for j in range(len(two)):
    tx, ty = two[j]
    dis = abs(ox-tx) + abs(oy-ty)
    br[i][j] = dis

idxs = com(list(range(len(two))), m)
msum = int(1e9)
for cidxs in idxs:
  tsum = 0
  for i in range(len(one)):
    tsum += min([br[i][idx] for idx in cidxs])
  msum = min(msum, tsum)

print(msum)