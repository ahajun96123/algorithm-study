import sys
input = sys.stdin.readline
l = []
while 1:
  a,b = map(int, input().split())
  if a==b == 0: break
  l.append((a, b))
for a, b in l:
  if a%b==0: print('multiple')
  elif b%a==0: print('factor')
  else: print('neither')