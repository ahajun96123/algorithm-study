a, b = map(int, input().split())
h = list(range(24))
m = list(range(60))
if b-45<0: a = h[a-1]
b = m[b-45]
print(a, b)