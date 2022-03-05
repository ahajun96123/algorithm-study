import sys
n, x = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
for l in a:
  if l < x: print(l, end=' ')