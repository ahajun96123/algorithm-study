import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
t = n
while 1:
  t1 = (t//10 + t%10)%10
  t10 = t%10*10
  t = t10 + t1
  cnt += 1
  if t == n: break

print(cnt)
