n = int(input())
l = list(map(int, input().split()))
ma = -int(1e5)
cur = 0
for i in l:
  cur += i
  if ma < cur: ma = cur
  if cur < 0: cur = 0
print(ma)