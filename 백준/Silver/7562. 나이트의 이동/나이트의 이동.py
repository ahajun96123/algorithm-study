import sys
input = sys.stdin.readline

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(srt, end):
  cnt = 0
  d_r, d_c = end
  q = [srt]
  b = False
  while q:
    tq = []
    while q:
      r, c = q.pop()
      if d_r==r and d_c==c:
        b = True
        break
      for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr<0 or nc<0 or nr>=n or nc>=n or v[nr][nc]: continue
        v[nr][nc] = 1
        tq.append((nr, nc))
    if b: break
    q = tq[:]
    cnt += 1

  return cnt

ans = []
for _ in range(int(input())):
  n = int(input())
  v = [[0]*n for _ in range(n)]
  srt = list(map(int, input().split()))
  end = list(map(int, input().split()))
  cnt = bfs(srt, end)
  # print(cnt)
  ans.append(cnt)
print(*ans)