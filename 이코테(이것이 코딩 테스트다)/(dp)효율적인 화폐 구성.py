# https://youtu.be/5Lu34WIx2Us?t=2601


# l의 개수가 많을 경우 시간을 줄이기 위해
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]
# 메모리스트의 0을 제외한 모든 인덱스를 -1로 초기화
d = [-1]*(m+1)
d[0] = 0
for i in range(m+1):
  # 동전 리스트에서 하나씩 꺼내서 인덱스 범위 확인과 -1인지 아닌지 확인.
  # 만들어진 배열이 있으면 최소값 +1. 없으면 어차피 -1로 되어있음.
  if t:=[d[i-j] for j in l if i-j>=0 and d[i-j]!=-1]: d[i] = min(t)+1
print(d[m])
