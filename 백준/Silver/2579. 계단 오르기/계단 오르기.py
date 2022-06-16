import sys
input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]
# 계단마다 전 계단을 밟았거나(1) 안 밟았거나(0)
d = [[l[0], l[0]]] + [[0]*2 for _ in range(300)]
if n>1: d[1] = [l[1], l[1]+l[0]]
for i in range(2, n):
  d[i][0] = max(d[i-2][0], d[i-2][1]) + l[i]
  d[i][1] = d[i-1][0] + l[i]
print(max(d[n-1]))