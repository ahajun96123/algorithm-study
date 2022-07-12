import sys
input = sys.stdin.readline
l = [[0],
  [1],
  [2, 4, 8, 6],
  [3, 9, 7, 1],
  [4, 6],
  [5],
  [6],
  [7, 9, 3, 1],
  [8, 4, 2, 6],
  [9, 1]]
for _ in range(int(input())):
  a, b = map(int, input().split())
  t = l[a%10]
  ans = t[b%len(t)-1]
  if not ans: ans = 10
  print(ans)
