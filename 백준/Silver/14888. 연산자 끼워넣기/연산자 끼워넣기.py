input()
nums = list(map(int, input().split()))
# + - * //
oper = list(map(int, input().split()))
m = int(1e10)
M = -m
def dfs(n, idx):
  global M, m
  if idx==len(nums)-1:
    if M<n: M=n
    if m>n: m=n
    return
  for i in range(4):
    if oper[i]>0:
      oper[i] -= 1
      if i==0: nn = n + nums[idx+1]
      elif i==1: nn = n - nums[idx+1]
      elif i==2: nn = n * nums[idx+1]
      else:
        if n<0: nn=-(abs(n)//nums[idx+1])
        else: nn = n // nums[idx+1]
      dfs(nn, idx+1)
      oper[i] += 1
dfs(nums[0], 0)
print(M, m)