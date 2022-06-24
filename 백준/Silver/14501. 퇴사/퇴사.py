import sys
input = sys.stdin.readline
n = int(input())
l = [map(int, input().split()) for _ in range(n)]
d = [0]*(n+1)
for i in range(n-1, -1, -1):
  day, sal = l[i]
  if day + i > n:
    d[i] = d[i+1]
    continue
  # i+day+sal vs i+1 비교 후 큰 거 넣기
  d[i] = max(d[i+day] + sal, d[i+1])
print(d[0])