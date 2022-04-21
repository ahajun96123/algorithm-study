import sys
input = lambda: sys.stdin.readline().rstrip()
print(*sorted(list(set(input()for _ in range(int(input())))),key=lambda x: (len(x), x)),sep='\n')