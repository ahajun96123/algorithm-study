n = input()
le = len(n)
n = int(n)

start = n - le * 9
if start < 0: start = 0
answer = 0
for i in range(start, n):
  s = str(i)
  hap = i + sum(map(int, s))
  if hap == n:
    answer = i
    break
print(answer)