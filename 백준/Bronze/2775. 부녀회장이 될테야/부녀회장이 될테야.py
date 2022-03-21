for _ in range(int(input())):
  k = int(input())
  n = int(input())
  a = [[1 for _ in range(14)] for _ in range(14)]
  l = [i+1 for i in range(14)]
  a.insert(0, l)
  for i in range(1, 15):
    for j in range(1, 14):
      a[i][j] = a[i-1][j] + a[i][j-1]
  print(a[k][n-1])