inp = []
while n:=int(input()):
  inp.append(n)
l = [0 for _ in range(246913)]
for n in range(2, 246913):
  for i in range(2, int(n**0.5+1)):
    if n%i==0:
      break
  else:l[n] = 1

for n in inp:
  print(sum(l[n+1:2*n+1]))