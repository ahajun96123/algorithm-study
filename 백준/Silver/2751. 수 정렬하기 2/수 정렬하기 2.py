import sys
input = sys.stdin.readline
l = [int(input()) for _ in range(int(input()))]
print(*sorted(l))