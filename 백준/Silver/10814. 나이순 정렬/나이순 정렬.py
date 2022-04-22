import sys
input = sys.stdin.readline
l = map(lambda x: [int(x[0]), x[1]],[input().split()for _ in range(int(input()))])
for i in sorted(l, key=lambda x: x[0]):
  print(*i)