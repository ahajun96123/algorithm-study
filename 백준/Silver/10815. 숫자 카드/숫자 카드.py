n = int(input())
l_n = sorted(list(map(int, input().split())))
m = int(input())
l_m = list(map(int, input().split()))

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

ans = [isin(l_m[i]) for i in range(m)]
print(*ans)