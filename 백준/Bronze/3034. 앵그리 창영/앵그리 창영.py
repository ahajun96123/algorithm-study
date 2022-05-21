import sys
input = sys.stdin.readline
n, a, b = map(int, input().split())
dia = int((a**2 + b**2)**0.5)
for _ in range(n):
  if int(input()) <= dia: print('DA')
  else: print('NE')