a = list(range(1, 10001))
for n in range(1, 10000):
  s = str(n)
  m = n
  for c in s:
    m += int(c)
  try:
    a.remove(m)
  except: pass
for n in a:
  print(n)