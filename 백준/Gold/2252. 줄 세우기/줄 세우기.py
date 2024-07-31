def bfs():
    for i in range(1, N+1):
        if arr[i] == 0:
            queue.append(i)
    while queue:
        now = queue.pop(0)
        print(now, end = ' ')
        for j in graph[now]:
            arr[j] -= 1
            if arr[j] == 0:
                queue.append(j)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
arr = [0] * (N+1)
queue = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    arr[b] += 1
bfs()