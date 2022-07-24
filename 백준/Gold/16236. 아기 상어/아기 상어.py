n = int(input())
l = []
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


def found(r, c):
    return l[r][c] and l[r][c] < size


def bfs(sr, sc):
    q = []
    q.append((sr, sc, 0))
    f = False
    length = 0
    while 1:

        tl = []
        if not q: break
        length += 1
        while q:

            r, c, tc = q.pop()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nc < 0 or nr >= n or nc >= n or v[nr][
                        nc] or l[nr][nc] > size:
                    continue
                v[nr][nc] = 1
                if found(nr, nc):
                    f = True
                    tl.append((nr, nc, tc + 1))
                tl.append((nr, nc, tc + 1))
        if f: break
        q = tl[:]
    if f:
        tl = list(filter(lambda x: found(x[0], x[1]), tl))
        tl.sort()
        re = tl[0]
        l[re[0]][re[1]] = 0
        return tl[0]
    return (0, 0, 0)


b = False
while 1:
    for _ in range(size):
        v = [[0] * n for _ in range(n)]
        r, c, tc = bfs(r, c)
        if tc == 0:
            b = True
            break
        cnt += tc
    if b: break
    size += 1
print(cnt)
