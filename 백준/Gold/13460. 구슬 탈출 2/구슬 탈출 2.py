import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
l = []
for i in range(n):
  tl = input().rstrip()
  l.append(tl)
  if 'R' in tl:
    red = (i, tl.index('R'))
  if 'B' in tl:
    blue = (i, tl.index('B'))
  if 'O' in tl:
    hole = (i, tl.index('O'))

v = {(red, blue): 1}
q = deque()
q.append((red, blue, 1))
f = False
while q:
  r, b, cnt = q.popleft()
  if cnt > 10: break
  for i in range(4):
    rh = bh = False
    rr, rc = r
    br, bc = b
    cntr = cntb = 0
    while l[(nbr:=br+dr[i])][(nbc:=bc+dc[i])]!='#':
      if l[nbr][nbc]=='O':
        bh = True
        break
      cntb += 1
      br += dr[i]
      bc += dc[i]
    if bh: continue
    while l[(nrr:=rr+dr[i])][(nrc:=rc+dc[i])]!='#':
      if l[nrr][nrc]=='O':
        rh = True
        break
      cntr += 1
      rr += dr[i]
      rc += dc[i]
    if rh:
      f = True
      break
    
    nr = (rr, rc)
    nb = (br, bc)
    
    if nr == nb:
      if cntr > cntb: nr = (rr-dr[i], rc-dc[i])
      else: nb = (br-dr[i], bc-dc[i])
    
    try:
      t = v[(nr, nb)]
      continue
    except: pass
    v[(nr, nb)] = 1
    q.append((nr, nb, cnt+1))
  if f: break

print(cnt if f else -1)