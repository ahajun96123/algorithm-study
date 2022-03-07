for _ in range(int(input())):
  s = input()
  j = 1
  hap = 0
  for i in s:
    if i == 'O':
      hap += j
      j += 1
    else: j = 1
  print(hap)