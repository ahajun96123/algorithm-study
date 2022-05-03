import sys
input = sys.stdin.readline
def fac(n):
  if n==0: return 1
  return n * fac(n-1)
for _ in range(int(input())):
  a, b = map(int, input().split())
  print(fac(b)//fac(a)//fac(b-a))