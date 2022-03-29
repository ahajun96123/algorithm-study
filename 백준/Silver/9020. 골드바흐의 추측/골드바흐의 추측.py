l = [0]*10000
for i in range(2, 10000):
  for j in range(2, int(i**0.5+1)):
    if i%j == 0:
      break
  else: l[i] = 1
for _ in range(int(input())):
  n = int(input())
  for i in range(n//2, 1, -1):
    if l[i] == 1 and l[n-i] == 1:
      print(i, n-i)
      break
      