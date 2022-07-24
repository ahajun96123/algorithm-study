from collections import deque
# 입력 받을때 개수를 기억하기
# bfs로 움직일때는 상 - 좌 - (우 - 하) 순으로 움직일것.
n = int(input())
l = []
# cl = [0] * 7
size = 2
cnt = 0

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

for i in range(n):
    tl = list(map(int, input().split()))
    l.append(tl)
    for j in range(n):
        t = int(tl[j])
        if t == 9:
            r, c = i, j
            l[i][j] = 0
            continue
        # if t != 0:
        #     c[t] += 1


def bfs(sr, sc):
    # print('시작')
    q = []
    q.append((sr, sc, 0, 0))
    f = False
    # while q:
    length = 0
    while 1:

        tl = []
        # print(q)
        if not q: break
        length += 1
        while q:

            r, c, tc, tra = q.pop()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nc < 0 or nr >= n or nc >= n or v[nr][
                        nc] or l[nr][nc] > size:
                    continue
                v[nr][nc] = 1
                if l[nr][nc] != 0 and l[nr][nc] < size:
                    f = True
                    tl.append((nr, nc, tc + 1, 1))
                tl.append((nr, nc, tc + 1, 0))
        if f: break
        q = tl[:]
    if f:
        tl = list(filter(lambda x: x[3] == 1, tl))
        tl.sort()
        # print(tl)
        re = tl[0]
        l[re[0]][re[1]] = 0
        return tl[0]
    return (0, 0, 0, 0)

    #     r, c, tc = q.popleft()
    #     if l[r][c] != 0 and l[r][c] < size:
    #         f = True
    #         l[r][c] = 0
    #         break
    #     for i in range(4):
    #         nr, nc = r + dr[i], c + dc[i]
    #         if nr < 0 or nc < 0 or nr >= n or nc >= n or v[nr][
    #                 nc] or l[nr][nc] > size:
    #             continue
    #         v[nr][nc] = 1
    #         q.append((nr, nc, tc + 1))
    # return (r, c, tc) if f else (r, c, 0)


b = False
while 1:
    for _ in range(size):
        v = [[0] * n for _ in range(n)]
        r, c, tc, tra = bfs(r, c)
        if tc == 0:
            b = True
            break
        cnt += tc
    if b: break
    size += 1
print(cnt)

# 자기보다 작은 것이 있을때 bfs하다가 없으면 count 했던거 버리고 답 출력.

# 자기 몸집보다 작은 것들 고른다.
# 고를 때 같은 거리가 여러개면 row 작은거 다음으로 col 작은거
# 자기 몸집만큼 먹으면(cnt==몸집) 몸집+=1

# 아기상어 위치확인 및 크기:2
