import sys
input = sys.stdin.readline
l = []
for _ in range(int(input())):
  l.append(list(map(int, input().split())))
l.sort()
for i in l:
  print(*i)