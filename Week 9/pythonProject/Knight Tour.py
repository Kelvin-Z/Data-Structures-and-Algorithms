dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]

flag = False


def dfs(r, c, depth):
    if depth == size * size:
        global flag
        flag = True
        return
    if flag:
        return
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < size and 0 <= nc < size:
            if not chess[nr][nc]:
                chess[nr][nc] = True
                dfs(nr, nc, depth + 1)
                chess[nr][nc] = False


size = int(input())
y, x = map(int, input().split())
chess = [[False] * size for _ in range(size)]
chess[y][x] = True
dfs(y, x, 1)
if flag:
    print('success')
else:
    print('fail')
