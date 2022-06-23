import sys
input = sys.stdin.readline
l = [int(input()) for _ in range(int(input()))]
m = max(l)
dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10, m):
  dp.append(dp[-1] + dp[-5])
for i in l:
  print(dp[i-1])