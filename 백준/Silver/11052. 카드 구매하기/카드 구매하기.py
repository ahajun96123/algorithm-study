n = int(input())
l = list(map(int, input().split()))
dp = [0]*(n+1)
for i in range(n):
  dp[i+1] = max([dp[i-j] + l[j] for j in range(i+1)])
  # for j in range(i+1):
  #   dp[i+1] = max(dp[i-j] + l[j], dp[i+1])
  
print(dp[n])