a, b, c = 300, 60, 10
n = int(input())
aa = bb = cc = 0

aa = n // a
n %= a
bb = n // b
n %= b
cc = n // c
n %= c

if n % 10 != 0: print(-1)
else: print(aa, bb, cc)
