from itertools import combinations
n, m = map(int, input().split())
l = list(range(1, n+1))
for cur in combinations(l, m): print(*cur)