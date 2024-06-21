def max_weights(n, weight, edge):
    graph = [[] for _ in range(n)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * n
    max_weight = 0

    def dfs(node):
        visited[node] = True
        total_weight = weight[node]
        for neighbor in graph[node]:
            if not visited[neighbor]:
                total_weight += dfs(neighbor)
        return total_weight

    for i in range(n):
        if not visited[i]:
            max_weight = max(max_weight, dfs(i))
    return max_weight


n, m = map(int, input().split())
weight = list(map(int, input().split()))
edge = []
for _ in range(m):
    u, v = map(int, input().split())
    edge.append((u, v))
print(max_weights(n, weight, edge))