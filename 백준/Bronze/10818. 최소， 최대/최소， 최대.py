import sys
n = int(sys.stdin.readline().rstrip())

l = list(map(int, sys.stdin.readline().rstrip().split()))
print(min(l), max(l))