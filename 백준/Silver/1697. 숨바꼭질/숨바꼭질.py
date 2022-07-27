n, k = map(int, input().split())
# d = [0] * (k * 3 // 2)
d = list(range(n, -1, -1)) + [0] * ((k - n) * 2 if k - n > 0 else 0)
for i in range(n+1, k+1):
    d[i] = min(d[i - 1] + 1, d[i // 2] + 1 if i % 2 == 0 else d[i // 2 + 1] + 2,
               d[i // 2] + 2)
    # print(i, d[i])

# print(d[n])
print(d[k])
