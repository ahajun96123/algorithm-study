a, b = map(int, input().split())
t1, t2 = (a, b) if a>b else (b, a)
while t1 % t2:
  t1 %= t2
  t1, t2 = t2, t1
print(t2, a*b//t2)