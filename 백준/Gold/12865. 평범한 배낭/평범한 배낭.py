import sys
inp = lambda: map(int, sys.stdin.readline().split())
n, k = inp()
bag = [0]*(k+1)
for _ in range(n):
  w, v = inp()
  for cw in range(k, w-1, -1):
    bag[cw] = max(bag[cw], bag[cw-w] + v)
print(bag[k])