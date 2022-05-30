from itertools import combinations_with_replacement as cwr
n, m = map(int, input().split())
l = list(range(1, n+1))
for cur in cwr(l, m): print(*cur)