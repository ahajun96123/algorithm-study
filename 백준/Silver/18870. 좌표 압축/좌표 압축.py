input()
l = list(map(int, input().split()))
dic = {k:v for v, k in enumerate(sorted(set(l)))}
for i in l:
  print(dic[i])