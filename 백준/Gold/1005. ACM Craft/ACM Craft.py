def bfs():
    for i in range(1, N+1):
        if arr[i] == 0:
            queue.append(i)
            ans[i] = time[i]
    while queue:
        now = queue.pop(0)
        for next in graph[now]:
            ans[next] = max(time[next]+ans[now], ans[next])
            arr[next] -= 1
            if arr[next] == 0:
                queue.append(next)
    return ans[W]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    queue = []
    arr = [0] * (N+1)
    ans = [0] * (N+1)
    time = [0] + list(map(int, input().split()))
    for _ in range(K):
        a, b  = map(int, input().split())
        graph[a].append(b)
        arr[b] += 1
    W = int(input())
    print(bfs())