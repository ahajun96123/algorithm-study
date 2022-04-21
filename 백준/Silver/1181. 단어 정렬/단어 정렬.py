import sys
N = lambda: sys.stdin.readline().rstrip()
print(*sorted(list(set(N()for _ in range(int(N())))),key=lambda x: (len(x), x)))