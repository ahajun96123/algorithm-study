n = int(input())

def pnt(i):
  star = '*'*i
  blank = ' '*(n-i)*2
  print(star+blank+star)
  
for i in range(1, n):
  pnt(i)
for i in range(n, 0, -1):
  pnt(i)