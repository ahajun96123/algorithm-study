import sys
input = lambda: sys.stdin.readline().rstrip()
a, b = map(int, input().split())
a = {input() for _ in range(a)}
b = {input() for _ in range(b)}
inter = sorted(a & b)
print(len(inter), *inter, sep = '\n')