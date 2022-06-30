s = input()
l = [0]*26
for c in s:
  idx = ord(c)-97
  l[idx] += 1
print(*l)