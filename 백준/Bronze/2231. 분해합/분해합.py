n = int(input())
m = len(str(n))
ans = 0
start = max(n-m*9, 1)
for i in range(start, n+1):
  if n == i + sum(map(int, str(i))): ans = i;break
print(ans)