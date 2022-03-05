a, b, c = map(int, input().split())
p = 0
if a == b == c:
  p = 10000 + 1000*a
elif a ==b or b==c or a==c:
  if a==b : p = 1000 + 100*a
  elif b==c : p = 1000 + 100*b
  else : p = 1000 + 100*c
else:
  p = max([a, b, c]) * 100

print(p)