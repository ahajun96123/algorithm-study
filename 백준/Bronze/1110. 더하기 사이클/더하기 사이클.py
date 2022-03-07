import sys
cnt = 0
n = sys.stdin.readline().rstrip()

if len(n) == 1 : n = '0'+n
t = n
while 1:
    cnt += 1
    try:
        t = t[1] + str(int(t[0]) + int(t[1]))[1]
    except:
        t = t[1] + str(int(t[0]) + int(t[1]))
    if t == n: break

print(cnt)