n = int(input())
x = 1
while x * (x + 1) / 2 < n:
  x += 1
h = x*(x-1)//2
b = n - h
p = ''
if x % 2 == 1:
  p = f'{x-b+1}/{b}'
else: p = f'{b}/{x-b+1}'
print(p)