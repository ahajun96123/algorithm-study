import sys
input = sys.stdin.readline
l = []
for _ in range(int(input())):
  n = int(input())
  if n == 0: del l[-1]
  else: l.append(n)
print(sum(l))