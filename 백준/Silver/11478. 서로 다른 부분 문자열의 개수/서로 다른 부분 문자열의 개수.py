s = input()
ans = set(s)
for n in range(2, len(s)+1):
  for i in range(len(s)-n+1):
    ans.add(s[i:i+n])
print(len(ans))