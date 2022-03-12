n = int(input())
cnt = 0
for _ in range(n):
  s = input()
  t = ''
  a_set = set()
  try:
    for c in s:
      if t != c:
        if c in a_set:
          raise Exception()
      a_set.add(c)
      t = c
  except: continue
  cnt += 1

print(cnt)