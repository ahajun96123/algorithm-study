n = int(input())
cnt = [0]*(1001)
d = [0]*(1001)
cnt[1], cnt[2] = 1, 2
d[1], d[2] = 1, 1

for i in range(3, n+1):
  cnt[i] = cnt[i-1] + d[i-1]
  d[i] = d[i-1] + d[i-2]

print(cnt[n]%10007)