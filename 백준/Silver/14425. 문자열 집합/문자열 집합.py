import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
l_n = sorted([input() for _ in range(n)])
l_m = sorted([input() for _ in range(m)])

def isin(t):
  a, b = 0, n-1
  i = (a + b)//2
  while b - a >= 0:
    if l_n[i] == t: return 1
    if l_n[i] < t:
      a = i + 1
      i = (a + b)//2
    else :
      b = i - 1
      i = (a + b)//2
  return 0

ans = sum([isin(l_m[i]) for i in range(m)])
print(ans)