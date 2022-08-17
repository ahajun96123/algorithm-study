import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
l = []
p = [0]*(n+1)
for _ in range(int(input())):
  tp, ts = map(int, input().split())
  p[ts] = tp
va = [a]
vb = [b]
f = True
while 1:
  la, lb = va[-1], vb[-1]
  if not (la or lb):
    f = False
    break
  bina = lb in va
  ainb = la in vb
  if bina:
    cntb = len(vb) - 1
    cnta = va.index(lb)
    break
  elif ainb:
    cnta = len(va) - 1
    cntb = vb.index(la)
    break
  va.append(p[va[-1]])
  vb.append(p[vb[-1]])
print(cntb + cnta if f else -1)