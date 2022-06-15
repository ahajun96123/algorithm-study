import sys
inp = lambda: map(int, sys.stdin.readline().split())
n, k = inp()
bag = [0]*(k+1)
for _ in range(n):
  w, v = inp()
  bag_t = bag[:]
  for cw in range(k+1):
    if cw >= w:
      bag[cw] = max(bag_t[cw], bag_t[cw-w] + v)
print(bag[k])