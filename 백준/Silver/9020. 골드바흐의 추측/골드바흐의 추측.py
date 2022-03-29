l = [1]*10000
l[1] = 0
for i in range(2, 100):
  for j in range(i*2, 10000, i):
    l[j] = 0
for _ in range(int(input())):
  n = int(input())
  for i in range(n//2, 1, -1):
    if l[i] == 1 and l[n-i] == 1:
      print(i, n-i)
      break
      