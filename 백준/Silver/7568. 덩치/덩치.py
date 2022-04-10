n = int(input())
l = []
for _ in range(n):
  l.append(list(map(int, input().split())))

for d in l:
  r = 1
  for i in range(n):
    if l[i][0] > d[0] and l[i][1] > d[1]:
      r+=1
  print(r)