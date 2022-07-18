import sys
input = sys.stdin.readline
for _ in range(int(input())):
  oper = input().rstrip()
  input()
  l = eval(input())
  f = e = 0
  b = False
  for o in oper:
    if o=='D':
      if b: e+=1
      else: f+=1
    else:
      b = not b
  if len(l) < f+e: print('error')
  else:
    l = l[f:len(l)-e]
    l = l[::-1] if b else l
    print('[', end='')
    print(*l, sep=',', end=']\n')
  