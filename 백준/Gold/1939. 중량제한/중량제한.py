def check_bfs(mid):
    visited = [False] * (N+1)
    queue = []
    queue.append(start)
    visited[start] = True
    while queue:
        now = queue.pop(0)
        for node, weight in graph[now]:
            if visited[node] == True:
                continue
            if weight >= mid:
                queue.append(node)
                visited[node] = True
    return visited[end]             


N, M = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
start, end = map(int, input().split())
l = 1
r = 1000000000
while l <= r:
    mid = (l+r) // 2
    if check_bfs(mid) == True:
        l = mid + 1
    else:
        r = mid - 1
print(r)