a, b = map(int, input().split())
ja, mo = 1, 1
for i in range(a, a-b, -1):
  ja *= i
for i in range(1, b+1):
  mo *= i
print(ja//mo%10007)