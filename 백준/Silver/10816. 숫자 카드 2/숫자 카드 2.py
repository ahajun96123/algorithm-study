from collections import Counter as c
n = int(input())
l_n = list(map(int, input().split()))
m = int(input())
l_m = list(map(int, input().split()))

dic = c(l_n)

print(*[dic[l_m[i]] for i in range(m)])