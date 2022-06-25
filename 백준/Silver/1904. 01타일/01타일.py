n = int(input())
dp = [1, 2] + [0] * n
for i in range(2, n):
  dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[n-1])