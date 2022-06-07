# 나동빈의 (이코테 2021 강의 몰아보기) 5. 이진 탐색
# https://youtu.be/94RC-DsGMLo?t=1351
# bisect를 이용하여 풀면 쉽다.

from bisect import bisect_left as bl, bisect_right as br
n, x = map(int, input().split())
l = list(map(int, input().split()))
print(br(l, x) - bl(l, x))
