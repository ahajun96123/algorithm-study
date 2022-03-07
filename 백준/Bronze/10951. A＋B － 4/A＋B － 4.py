import sys
try:
    while 1:
      a, b = map(int, sys.stdin.readline().rstrip().split())
      print(a+b)
except:
    pass