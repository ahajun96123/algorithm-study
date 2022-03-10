s = input()
d = {}
for c in s.upper():
  if c in d:
    d[c] += 1
  else:
    d[c] = 1
l = list(d.values())
m = max(l)
b = l.count(m)
if 1 < b:
  print('?')
else:
  for k in d.keys():
    if d[k] == m:
      print(k)
      break