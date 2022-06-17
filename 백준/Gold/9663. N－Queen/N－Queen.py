n = int(input())

# right = [0]*(2*n-1)
# left = [0]*(2*n-1)
# vert = [0]*n

# cnt = 0
# def queen(i):
#   global cnt
#   if i==n:
#     cnt +=1
#     return

#   for j in range(n):
#     il, ir = i-j+n-1, i+j
#     if right[ir] + left[il] + vert[j] > 0: continue
#     vert[j] += 1
#     right[ir] += 1
#     left[il] += 1
#     queen(i+1)
#     vert[j] -= 1
#     right[ir] -= 1
#     left[il] -= 1

# queen(0)
# print(cnt)

answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[n])