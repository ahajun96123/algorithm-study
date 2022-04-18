import sys
from collections import Counter as c
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
  l.append(int(input()))

l.sort()
print(round(sum(l)/n))
print(l[n//2])

f = c(l).most_common(2)

print(f[0][0] if len(f)==1 else f[0][0] if f[0][1]>f[1][1] else f[1][0])

print(l[-1] - l[0])