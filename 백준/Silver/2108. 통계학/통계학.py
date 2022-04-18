import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
  l.append(int(input()))

l.sort()
print(round(sum(l)/n))
print(l[n//2])

cnt, m_cnt = 1, 1
stack = {i:[] for i in range(1, n+1)}
for i in range(1, n):
  if l[i] == l[i-1]: cnt+=1
  else:
    if cnt >= m_cnt:
      m_cnt = cnt
      stack[m_cnt].append(l[i-1])
    cnt = 1
  if i == n-1 :
    stack[cnt].append(l[i])
    if m_cnt < cnt : m_cnt = cnt
if n == 1 :
	stack[1].append(l[0])

stack[m_cnt].sort()
if len(stack[m_cnt]) == 1 :
	print(stack[m_cnt][0])
else :
	print(stack[m_cnt][1])

print(l[-1] - l[0])