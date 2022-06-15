import sys
inp = lambda: int(sys.stdin.readline())
n = inp()
l = [inp() for _ in range(n)]
m = max(l)
d = [0]*(m+1)
if n>=3: d[3] = 4
if n>=2: d[2] = 2
if n>=1: d[1] = 1
for i in range(4, m+1):
  d[i] = d[i-1]+d[i-2]+d[i-3]
for i in l: print(d[i])