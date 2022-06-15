n = int(input())
INF = int(1e9)
d = [INF]*(n+1)
d[1] = 0
for i in range(2, n+1):
  d[i] = min(d[i//3] if i%3==0 else INF, d[i//2] if i%2==0 else INF, d[i-1]) + 1
print(d[n])