import sys

for _ in range(int(sys.stdin.readline().rstrip())):
  n, s = sys.stdin.readline().rstrip().split()
  for c in s:
    print(c*int(n), end='')
  print()
  