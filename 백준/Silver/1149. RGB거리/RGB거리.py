import sys
input = sys.stdin.readline
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
d = [l[0]] + [[0]*3 for _ in range(n-1)]
for i in range(1, n):
  for j in range(3):
    d[i][j] = min([d[i-1][k] if k!=j else d[i-1][k-1] for k in range(3)]) + l[i][j]
print(min(d[n-1]))