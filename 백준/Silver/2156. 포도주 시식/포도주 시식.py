import sys
inp = lambda: int(sys.stdin.readline())
n = inp()
l = [inp() for _ in range(n)]
# n, *l = list(map(int, input().split()))
dp = [l[0]]
if n > 1: dp.append(l[0]+l[1])
if n > 2: dp.append(max(l[1]+l[2], l[0]+l[2], dp[1]))
for i in range(3, n):
  dp.append(max(dp[0]+l[i], dp[1]+l[i], dp[0]+l[i-1]+l[i], dp[2]))
  # print(i, max(dp[0]+l[i], dp[1]+l[i], dp[0]+l[i-1]+l[i]), dp)
  del dp[0]
print(max(dp))