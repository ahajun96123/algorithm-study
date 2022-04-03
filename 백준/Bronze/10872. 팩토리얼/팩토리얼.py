n = int(input())
f = 1
for i in range(1, n+1):
  f *= i
print(f)

# 문제에선 재귀로 풀으라고 하지만 반복문이 더 빠름
# def fac(n):
#   if n==1 or n==0: return 1
#   return n * fac(n-1)
# print(fac(int(input())))
