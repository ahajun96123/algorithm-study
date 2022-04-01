for _ in range(int(input())):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  r_b, r_s = (r1, r2) if r1>r2 else (r2, r1)
  d, r_sum = ((x1-x2)**2 + (y1-y2)**2)**0.5, r1+r2
  # 접점 2개
  if d < r_sum and d+r_s > r_b: cnt=2
  # 접점 1개
  elif d == r_sum or d+r_s == r_b: cnt=1
  # 접점 0개
  elif d > r_sum or r_b > r_s+d: cnt=0
  # 접점 무한개
  if x1==x2 and y1==y2 and r1==r2: cnt=-1
    
  print(cnt)