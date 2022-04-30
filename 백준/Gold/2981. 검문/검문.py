import sys, math as m
input = sys.stdin.readline

# 입력, 연산
n = int(input())
l = [0]*n
gcd = 0
for i in range(n):
  l[i] = int(input())
  if i == 1: gcd = abs(l[1]-l[0])
  gcd = m.gcd(gcd, abs(l[i]-l[i-1]))
ans = []
for i in range(2, int(gcd**0.5 + 1)):
  if gcd % i == 0:
    ans.append(i)
    ans.append(gcd//i)
ans.append(gcd)

# 출력
print(*sorted(list(set(ans))))