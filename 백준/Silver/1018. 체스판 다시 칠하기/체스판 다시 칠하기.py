n, m = map(int, input().split())
mat = []
for _ in range(n):
  mat.append(input())

wb, bw = 'WB'*4, 'BW'*4
m_wb = [*(wb, bw)*4]

r, c = n-7, m-7
diff_min = 64
for i in range(r):
  for j in range(c):
    diff = 0
    temp = list(map(lambda x: x[j:j+8], mat[i:i+8]))
    for r_i in range(8):
      for c_i in range(8):
        if temp[r_i][c_i] != m_wb[r_i][c_i]:
          diff+=1
    if diff > 32: diff = 64-diff
    if diff < diff_min: diff_min = diff
    
print(diff_min)