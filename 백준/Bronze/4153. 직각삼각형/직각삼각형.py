while 1:
  l = list(map(int, input().split()))
  c = max(l)
  if c == 0: break
  l.remove(c)
  a, b = l
  tri = 'wrong'
  if c**2 == a**2 + b**2: tri = 'right'
  print(tri)
  