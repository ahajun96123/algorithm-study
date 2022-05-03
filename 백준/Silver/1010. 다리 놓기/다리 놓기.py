import sys
input = sys.stdin.readline

def fac(n):
  if n==0: return 1
  return n * fac(n-1)

for _ in range(int(input())):
  a, b = map(int, input().split())
  # ans = 1
  # for i in range(1, a+1):
  #   ans *= (b-i+1)/i
  # print(int(ans))
  print(fac(b)//fac(a)//fac(b-a))