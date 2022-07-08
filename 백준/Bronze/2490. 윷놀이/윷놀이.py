for _ in range(3):
  cnt = 0
  ans = 'A'
  for i in map(int, input().split()):
    if i == 0: cnt += 1
  if cnt == 0: ans = 'E'
  elif cnt == 1: ans = 'A'
  elif cnt == 2: ans = 'B'
  elif cnt == 3: ans = 'C'
  else: ans = 'D'
  print(ans)