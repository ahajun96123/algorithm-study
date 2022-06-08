# https://youtu.be/5Lu34WIx2Us?t=2167
# 짧은데 dp가 생소해서 오래걸렸다...

n = int(input())
d = [0]*(n+1)
cal = [5, 3, 2]
for i in range(2, n+1):
  d[i] = min([d[i//c] for c in cal if i%c==0] + [d[i-1]]) + 1
print(d[n])
