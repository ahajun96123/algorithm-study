n, k = map(int, input().split())
l = list(range(1, 1+n))
k -=1
idx = k
ans = []
while 1:
  ans.append(l[idx])
  del l[idx]
  if not l: break
  idx += k
  idx %= len(l)
print('<', end='')
for i in ans:
  print(i, end='')
  if i == ans[-1]: break
  print(end=', ')
print('>')