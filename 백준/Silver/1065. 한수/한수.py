n = int(input())
cnt = 0
for i in range(1, n+1):
  if i<100: cnt+=1; continue
  s = str(i)
  for j in range(len(s)-2):
    if not int(s[j]) - int(s[j+1]) == int(s[j+1]) - int(s[j+2]): break
  else: cnt+=1
print(cnt)