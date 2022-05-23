n = int(input())
l = [list(map(int, input().split())) for _ in range(6)]
t = sorted([l[i][1] for i in range(6)])
area = t[-1] * t[-2]
for i in range(-3, 6):
  if l[i][0] == l[i+2][0] and l[i+1][0] == l[i+3][0]:
    print((l[i-2][1] * l[i-1][1] - l[i+2][1] * l[i+1][1]) * n)
    break