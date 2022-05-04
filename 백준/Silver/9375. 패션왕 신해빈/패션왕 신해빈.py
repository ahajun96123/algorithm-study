import sys
input = sys.stdin.readline
for _ in range(int(input())):
  dic = {}
  m = 1
  for _ in range(int(input())):
    name, typ = input().split()
    if typ in dic: dic[typ] += 1
    else: dic[typ] = 2
  for key in dic:
    m *= dic[key]
  print(m-1)