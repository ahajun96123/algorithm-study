import sys
input = sys.stdin.readline
w, h, x, y, p = map(int, input().split())
r = h//2
def isin(c_x, c_y, x, y):
  global r
  dist = ((c_x - x)**2 + (c_y - y)**2) **0.5
  if dist <= r: return True
  else: return False
    
cnt = 0
for _ in range(p):
  a, b = map(int, input().split())
  if isin(x, y+h//2, a, b) or isin(x+w, y+r, a, b) or (x<=a<=x+w and y<=b<=y+h): cnt+=1
print(cnt)