dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]
ans = 0


def dfs(r, c, depth):
    if depth == m * n:
        global ans
        ans += 1
        return
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < m and 0 <= nc < n:
            if not chess[nr][nc]:
                chess[nr][nc] = True
                dfs(nr, nc, depth + 1)
                chess[nr][nc] = False


for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    chess = [[False] * n for _ in range(m)]
    ans = 0
    chess[y][x] = True
    dfs(y, x, 1)
    print(ans)
