n = int(input())

def pnt(i):
  for j in range(n-i):
    print(end=' ')
  for j in range(1, i*2):
    print('*', end='')
  print()

for i in range(n, 0, -1):
  pnt(i)