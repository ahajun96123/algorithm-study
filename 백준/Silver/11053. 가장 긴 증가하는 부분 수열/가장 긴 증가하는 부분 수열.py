from bisect import bisect_left as bl
n = int(input())
l = list(map(int, input().split()))
d = [1]
dp = [l[0]]
for i in range(1, n):
  idx = bl(dp, l[i])
  d.insert(idx, max(d[:idx] if idx!=0 else [0]) + 1)
  dp.insert(idx, l[i])
print(max(d))