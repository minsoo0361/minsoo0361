def bfs(s, N, G):     # 시작정점 s, 노드개수 N
    q = []                  # 큐 생성
    visited = [0] * (N+1)   # visited 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 인큐 표시
    while q:                # 큐가 비워질 때까지... (남은 정점이 있으면)
        t = q.pop(0)        # 처리할 정점 디큐
        if t == G :         # t에서 할 일
            return visited[t] -1  # -1을 하는 이유 : 시작정점이 1이기 때문.
                                  #  몇개의 간선을 지나가니? 라고 물었기 떄문에
        for i in adjl[t]:         # t의 인접 정점이
            if visited[i]==0:       # 인큐되지 않았으면(처리된적이 없었으면)
                q.append(i)
                visited[i] = visited[t] + 1 # 방문표시 (나 t에서 한 개 더 온거다!)
    return 0                # G까지 경로가 없는 경우



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjl = [[]for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    S, G = map(int, input().split())

    print(f'#{tc}', bfs(S, V, G))