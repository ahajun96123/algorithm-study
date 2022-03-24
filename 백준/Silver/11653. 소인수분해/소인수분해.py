n = int(input())
l = []
for i in range(2, n+1):
  while n%i == 0:
    n //= i
    l.append(i)

print(*l, sep='\n')