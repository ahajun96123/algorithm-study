import sys

input = sys.stdin.readline
s = set()
for _ in range(int(input())):
  l = input().rstrip().split()
  if len(l) > 1:
    oper, n = l
    n = int(n)
  else:
    oper = l[0]
  if oper == 'add':
    s.add(n)
  elif oper == 'remove':
    try: s.remove(n)
    except: pass
  elif oper == 'check': print(1 if n in s else 0)
  elif oper == 'toggle':
    try: s.remove(n)
    except: s.add(n)
  elif oper == 'all': s = set(range(1, 21))
  else: s = set()
