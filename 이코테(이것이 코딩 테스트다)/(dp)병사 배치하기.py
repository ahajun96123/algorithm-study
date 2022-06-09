# https://youtu.be/5Lu34WIx2Us?t=3590
# dp 테이블의 현재 index 앞쪽을 모두 검사해야 하는 문제


n = int(input())
l = list(map(int, input().split()))
dp = [1]*n
for i in range(1, n):
  cur = l[i]
  # 바로 밑 주석은 틀린코드. 현재 인덱스를 줄여나가다가 만나는 최초의 cur보다 큰 dp[j] 하나만을 참조하는 것이 아니라 i 이전의 dp 테이블을 모두 검사해야 하기 때문.
  # cur이 전보다 작은지 체크
  # for j in range(i-1, -1, -1):
  #   if l[j] > cur:
  #     dp[i] = dp[j]+1
  #     break
  dp[i] = max([dp[j] for j in range(i) if l[j]>cur])+1
print(*dp)
print(n-max(dp))
