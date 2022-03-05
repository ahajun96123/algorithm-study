import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    star = '*'*(i+1)
    blank = ' '*(n-i-1)
    print(blank, star, sep='')