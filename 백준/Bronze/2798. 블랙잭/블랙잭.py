n, m = map(int, input().split())
l = list(map(int, input().split()))
from itertools import combinations as com

maxim = 0
t = map(sum, com(l, 3))
for s in t:
  if s<=m and s>maxim: maxim=s
  if maxim==m: break
print(maxim)