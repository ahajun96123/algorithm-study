def cnt_two(n):
  cnt = 0
  while n:
    n //= 2
    cnt += n
  return cnt

def cnt_five(n):
  cnt = 0
  while n:
    n //= 5
    cnt += n
  return cnt

a, b = map(int, input().split())
print(min(cnt_two(a)-cnt_two(a-b)-cnt_two(b), cnt_five(a)-cnt_five(a-b)-cnt_five(b)))