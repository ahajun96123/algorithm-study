import sys
input = sys.stdin.readline
l = [tuple(map(int, input().split())) for _ in range(int(input()))]
l.sort(key=lambda x: (x[1], x[0]))
cnt, line = 0, 0
for start, end in l:
  if start >= line:
    line = end
    cnt += 1
print(cnt)