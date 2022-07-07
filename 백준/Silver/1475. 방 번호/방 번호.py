n = list(map(int, input()))
l = [0]*9
t = 0
for i in n:
  if i==6 or i==9:
    t += 1
    continue
  l[i] += 1
t = (t+1)//2
l.append(t)
print(max(l))