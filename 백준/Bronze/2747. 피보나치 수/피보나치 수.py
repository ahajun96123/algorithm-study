n = int(input())
dp = [1, 1] + [0]*(n-2)
for i in range(2, n):
  dp[i] = dp[i-1] + dp[i-2]
print(dp[n-1])