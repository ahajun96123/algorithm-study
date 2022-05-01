import math as m
input()
l = list(map(int, input().split()))
cir = l[0]
del l[0]
ans = []

for i in l:
  gcd = m.gcd(cir, i)
  ans.append(f'{cir//gcd}/{i//gcd}')

print(*ans)