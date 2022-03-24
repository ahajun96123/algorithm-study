a = int(input())
b = int(input())
mi, su = [], 0
for n in range(a, b+1):
  if n == 1: continue
  for i in range(2, int(n**0.5+1)):
    if n % i == 0:
      break
  else:
    mi.append(n)
    su += n
if mi:
  print(su)
  print(mi[0])
else: print(-1)