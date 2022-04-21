import sys
input = lambda: sys.stdin.readline().rstrip()
l = list(set(input()for _ in range(int(input()))))
l.sort(key=lambda x: (len(x), x))
print(*l,sep='\n')