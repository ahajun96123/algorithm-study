n, m = map(int, input().split())
stack = []

def re(start, end):
  if len(stack)==m:
    print(*stack)
    return
    
  for i in range(start, end):
    stack.append(i)
    re(i+1, end + 1)
    stack.pop()

re(1, n-m+2)