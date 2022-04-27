import sys
input = sys.stdin.readline

# 입력
l = [list(map(int, input().split()))for _ in range(int(input()))]

# 연산
for a, b in l:
  t1, t2 = a, b
  while t1%t2:
    t1, t2 = t2, t1%t2
    
  # 출력
  print(a*b//t2)