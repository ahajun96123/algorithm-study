c_h, c_m = map(int, input().split())
t = int(input())
c_h = (c_h + (c_m + t) // 60) % 24
c_m = (c_m + t) % 60
print(c_h, c_m)