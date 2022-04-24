input()
l = list(map(int, input().split()))
dic = {k:v for v, k in enumerate(sorted(set(l)))}
print(*[dic[i]for i in l])