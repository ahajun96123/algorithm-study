import sys
input = sys.stdin.readline
# 주어지는 원이 시작 or 도착 점 중 하나만 포함할 때 cnt + 1
# 포함하는지 알아볼 때는 if 점과 원 중심 거리 < r : 포함.
def isin(c_x, c_y, r, x, y):
  dist = ((x - c_x)**2 + (y - c_y)**2)**0.5
  if dist < r : return True
  return False
for _ in range(int(input())):
  x1, y1, x2, y2 = map(int, input().split())
  cnt = 0
  for _ in range(int(input())):
    x, y, r = map(int, input().split())
    if isin(x, y, r, x1, y1) ^ isin(x, y, r, x2, y2): cnt += 1
  print(cnt)