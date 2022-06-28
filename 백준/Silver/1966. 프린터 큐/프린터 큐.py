import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
  q = deque()
  n, idx = map(int, input().split())
  tl = list(input().rstrip().split())
  for i in range(n):
    q.append((tl[i], i))
  tl.sort()
  i = 0
  while 1:
    # 현재 제일 큰거랑 비교
    if tl[-1] == q[0][0]:
      i+=1
      if q[0][1] == idx:
        print(i)
        break
      tl.pop()
      q.popleft()
    else: q.append(q.popleft())