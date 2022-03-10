dic = {}
i = 3
a = ord('A')
def filldic(n=3):
  global dic, i, a
  for _ in range(n):
    dic[chr(a)] = i
    a += 1
  i += 1
for _ in range(5): filldic()
filldic(4)
filldic(3)
filldic(4)
s = input()
print(sum([dic[c] for c in s]))