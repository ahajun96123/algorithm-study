from itertools import product
n, m = map(int, input().split())
l = list(range(1, n+1))
for cur in product(l, repeat=m): print(*cur)