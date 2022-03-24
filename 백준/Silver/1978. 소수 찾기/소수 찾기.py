input()
l = list(map(int, input().split()))
cnt = 0
for n in l:
  if n == 1: continue
  for i in range(2, int(n**0.5+1)):
    if n % i == 0:
      break
  else:
    cnt+=1
print(cnt)