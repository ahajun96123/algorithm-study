l = list(map(int, input().split()))
p = sorted(l)
if p==l: ans = 'ascending'
elif p==l[::-1]: ans = 'descending'
else: ans = 'mixed'
print(ans)