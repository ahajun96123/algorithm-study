import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
d = {}
for i in range(1, n+1):
  t = input()
  i = str(i)
  d[t] = i
  d[i] = t
for _ in range(m):
  print(d[input()])