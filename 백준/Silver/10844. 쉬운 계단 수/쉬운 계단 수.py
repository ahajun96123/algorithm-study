n = int(input())
dp = [[1]*10] + [[0]*10 for _ in range(n-1)]
for i in range(1, n):
  for j in range(10):
    if j > 0: dp[i][j] += dp[i-1][j-1]
    if j < 9: dp[i][j] += dp[i-1][j+1]
print((sum(dp[n-1]) - dp[n-1][0]) % 1000000000)