n = int(input())

def pnt(i):
  for j in range(0, i):
    print('*', end='')
  print()

for i in range(1, n):
  pnt(i)
for i in range(n, 0, -1):
  pnt(i)