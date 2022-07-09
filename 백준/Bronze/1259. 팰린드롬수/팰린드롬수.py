while (n:=input()) != '0':
  for i in range(len(n)//2):
    if n[i] != n[-i-1]:
      print('no')
      break
  else: print('yes')