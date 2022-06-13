n = 0
ans = [0]*10100
for i in range(1, 10001):
  t = i
  while i:
    t += i%10
    i //= 10
  ans[t] = 1
for i in range(1, 10001):
  if ans[i]==0: print(i)