import sys
input = sys.stdin.readline
l = [(lambda x,y: [int(x),y])(*input().split())for _ in range(int(input()))]
for i in sorted(l, key=lambda x: x[0]):
  print(*i)