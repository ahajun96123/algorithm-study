m = cnt = 0
for _ in range(4):
  o, i = map(int, input().split())
  cnt -= o
  cnt += i
  m = max(m, cnt)
print(m)