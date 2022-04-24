n = int(input())
l = list(map(int, input().split()))
l_s = sorted(set(l))
dic = {k:v for v, k in enumerate(l_s)}
for i in l:
  print(dic[i])
