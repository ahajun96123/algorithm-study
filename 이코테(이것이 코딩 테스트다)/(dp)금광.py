# https://youtu.be/5Lu34WIx2Us?t=3150
# l=[[0]*m]*n 이런 식으로 초기화하면 l[마지막][j]을 바꿀때 l[전][j]도 다 바뀜. 이유는 모르겠음. 그러므로 2차원 배열 초기화는 for문을 쓰거나 append 하자.
# 이 문제는 따로 dp를 위한 메모 테이블을 만들 필요 없다.
# 주석된 코드는 유튜브 코드.


for _ in range(int(input())):
  n, m = map(int, input().split())
  d = [[0 for j in range(m)] for i in range(n)]
  # d = []
  g = list(map(int, input().split()))
  ti = 0
  for i in range(n):
    for j in range(m):
      d[i][j] = g[ti]
      ti+=1
  # for i in range(n):
  #   d.append(g[ti:ti+m])
  #   ti+=m
  
  for j in range(1, m):
    for i in range(n):
      # 리스트 범위를 벗어나는지 체크
      d[i][j] = max([d[i+k][j-1] for k in range(-1, 2) if i+k>=0 and i+k<n]) + d[i][j]

  print(max([d[i][m-1] for i in range(n)]))
