def dfs(matrix, row, col, visited):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) \
     or matrix[row][col] != 'W' or visited[row][col]:
        return 0
    visited[row][col] = 1
    size = 1
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            size += dfs(matrix, row + dr, col + dc, visited)
    return size


def max_area(matrix):
    max_area0 = 0
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'W' and not visited[row][col]:
                area = dfs(matrix, row, col, visited)
                max_area0 = max(area, max_area0)
    return max_area0


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    matrix_input = [input().strip() for _ in range(a)]
    print(max_area(matrix_input))
