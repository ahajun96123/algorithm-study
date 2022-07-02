n, k = map(int, input().split())
b = bin(n)
cnt = 0
ans = 0
le = len(b)
for i in range(le):
  c = b[i]
  if c == '1':
    cnt += 1
    if cnt >= k:
      if i<le-1 and '1' in b[i+1:]: ans = 2**(le-i-1) - int(b[i+1:], 2)
      break

print(ans)