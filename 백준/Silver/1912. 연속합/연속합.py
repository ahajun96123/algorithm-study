n = int(input())
l = list(map(int, input().split()))
ma = 0
cur = 0
for i in l:
  cur += i
  if cur < 0:
    cur = 0
  if ma < cur: ma = cur
print(ma if ma != 0 else max(l))