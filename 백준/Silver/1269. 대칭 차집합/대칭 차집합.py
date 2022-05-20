a, b = map(int, input().split())
l_a = set(map(int, input().split()))
l_b = set(map(int, input().split()))
ans = l_a ^ l_b
print(len(ans))