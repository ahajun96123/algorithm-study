n, m = map(int, input().split())
l = list(map(int, input().split()))
from itertools import combinations

# a = 0

# maxim = 0

# for i in range(n):
#   if l[i]+a< m:
#     last = i
#     a += l[i]
#   if maxim < a: maxim = a

#   if maxim==m: break

# print(maxim)
maxim = 0
try:
  c = combinations(l, 3)
  t = list(map(sum, c))
  aa = [_ for _ in t]
  # print(*aa)
  for su in t:
    if su<=m and su>maxim: maxim=su
    # print('max: ',maxim)
    if maxim==m: raise Exception
except:
  pass
print(maxim)

