import sys
input = sys.stdin.readline
n, k = map(int, input().split())
l = [int(input()) for _ in range(n)][::-1]
cnt = 0
for cur in l:
  cnt += k//cur
  k %= cur
print(cnt)