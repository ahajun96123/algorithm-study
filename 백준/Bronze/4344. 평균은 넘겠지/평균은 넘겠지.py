n = int(input())
for _ in range(n):
  l = list(map(int, input().split()))
  nn = l[0]
  stu = l[1:]
  avg = sum(stu)/nn
  cnt = 0
  for j in stu:
    if j > avg: cnt+=1
  print(f'{cnt/nn*100:.3f}%')