n = int(input())
se = {i for i in range(1, 100)}
for i in range(1, 10):
  for d in range(i, 10):
    d1 = (d-i)//2
    se.add(100*i + 10*(i+d1) + i+2*d1)
  for d in range(i+1):
    d2 = d//2
    se.add(100*i + 10*(i-d2) + i-2*d2)
print(len(set(filter(lambda x: x<=n, se))))