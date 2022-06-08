# https://youtu.be/5Lu34WIx2Us?t=1609
# if else로 나눠서 풀었는데 아래쪽의 답안을 보면 dp를 제대로 쓰면 if를 사용하지 않고 최적해를 구할 수 있다.

# 내가 구한 방식의 dp. i-2와 i-3을 비교해서 l[i]를 더했다.
# 2 4 4  6 1  4  1  1  8
# 2 4 6 10 7 14 11 15 22

n = int(input())
l = list(map(int, input().split()))
ch = [0]*n
if n <= 2: print(max(l))
else:
  ch[0], ch[1] = l[0], l[1]
  for i in range(2, n):
    ch[i] = max(ch[i-2], ch[i-3]) + l[i]
  print(ch[n-1])
  
  
# n = int(input())
# l = list(map(int, input().split()))
# ch = [0]*n
# ch[0], ch[1] = l[0], max(l[0], l[1])
# for i in range(2, n):
#   ch[i] = max(ch[i-1], ch[i-2] + l[i])
# print(ch[n-1])
