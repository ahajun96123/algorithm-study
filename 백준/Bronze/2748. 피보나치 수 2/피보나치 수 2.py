n = int(input())
d = [1]
if n>1: d.append(1)
for i in range(3, n+1):
  d.append(d[0]+d[1])
  del d[0]
print(d[-1])