n, m = map(int, input().split())
laplace_matrix = [[0] * n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    laplace_matrix[a][a] += 1
    laplace_matrix[b][b] += 1
    laplace_matrix[a][b] = -1
    laplace_matrix[b][a] = -1
for j in range(n):
    print(' '.join(map(str, laplace_matrix[j])))
