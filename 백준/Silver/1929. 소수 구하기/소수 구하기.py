def isPrime(n):
  for i in range(2, int(n**0.5+1)):
    if n%i == 0:
      break
  else: print(n)

import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
a = max([a, 2])
for i in range(a, b+1):
  isPrime(i)