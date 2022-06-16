n = int(input())
l = list(map(int, input().split()))
d = [0]*1001
d[l[0]] = 1
for i in range(1, n):
  d[l[i]] = max(d[:l[i]]) + 1
print(max(d))