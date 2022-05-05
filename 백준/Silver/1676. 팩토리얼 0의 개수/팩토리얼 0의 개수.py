import math as m
cnt = 0
n = m.factorial(int(input()))
while not n%10:
  cnt += 1
  n //= 10
print(cnt)