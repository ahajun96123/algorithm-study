import sys
iter = int(sys.stdin.readline().rstrip())
for i in range(iter):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)