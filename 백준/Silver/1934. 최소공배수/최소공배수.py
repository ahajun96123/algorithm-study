import sys, math as m
input = sys.stdin.readline
# 입력
l = [list(map(int, input().split()))for _ in range(int(input()))]
# 연산
print(*[m.lcm(a, b) for a, b in l])