n = int(input())
d = [1, 1] + [0]*(n-2)
for i in range(2, n):
  d[i] = d[i-1] + d[i-2]
print(d[n-1])