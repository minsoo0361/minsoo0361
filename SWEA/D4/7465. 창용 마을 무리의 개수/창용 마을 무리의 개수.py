def dfs(start):
    visited[start] = True
    for w in graph[start]:
        if visited[w]:
            continue
        dfs(w)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    cnt = 0

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N+1):
        if visited[i]:
            continue
        dfs(i)
        cnt += 1
    print(f'#{tc} {cnt}')