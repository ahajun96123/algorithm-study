n = int(input())
INF = int(1e9)
d = [INF]*(n+1)
d[0] =0
if n>=5: d[5] = 1
if n>=3: d[3] = 1
for i in range(6, n+1):
  d[i] = min(d[i-3], d[i-5]) + 1
print(-1 if d[n] >= INF else d[n])