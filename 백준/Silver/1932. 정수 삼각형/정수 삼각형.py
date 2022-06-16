import sys
input = sys.stdin.readline
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0] = l[0][0]
for i in range(1, n):
  d[i][0] += l[i][0] + d[i-1][0]
  d[i][i] += l[i][i] + d[i-1][i-1]
d[0][0] = l[0][0]
for i in range(1, n):
  for j in range(1, i):
    d[i][j] = max(d[i-1][j], d[i-1][j-1]) + l[i][j]
print(max(d[n-1]))