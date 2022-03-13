s = input()
minus = 0
for i in range(len(s)):
  if s[i] == '=':
    minus += 1
    if s[i-1] == 'z' and s[i-2] == 'd':
      minus += 1
  if s[i] == '-':
    minus += 1
  if s[i] == 'j':
    if s[i-1] == 'n' or s[i-1] == 'l':
      minus += 1
print(len(s)-minus)