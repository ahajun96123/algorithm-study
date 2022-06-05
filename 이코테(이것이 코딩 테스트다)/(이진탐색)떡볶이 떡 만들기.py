# 나동빈의 (이코테 2021 강의 몰아보기) 5. 이진 탐색
# https://youtu.be/94RC-DsGMLo?t=750
# map과 reduce를 활용해보았다.

from functools import reduce
n, m = map(int, input().split())
l = list(map(int, input().split()))

st, en = 0, max(l)
ans = 0
while st <= en:
  mi = (st+en)//2
  # tl = map(lambda x: x-mi if x>mi else 0, l)
  # ts = sum(tl)
  ts = reduce(lambda a,b: b-mi+a if b>mi else a, l, 0)
  if ts < m:
    en = mi-1
  else:
    ans = mi
    st = mi+1
print(ans)
