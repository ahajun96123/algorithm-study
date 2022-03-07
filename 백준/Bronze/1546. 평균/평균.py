n = int(input())
l = list(map(int, input().split()))
m = max(l)

for i in range(n):
  l[i] *= 100/m

print(sum(l)/n)