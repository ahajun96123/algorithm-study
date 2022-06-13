n = int(input())
l = sorted(list(map(int, input().split())))
s = 0
for i in range(n):
  s += (n-i)*l[i]
print(s)