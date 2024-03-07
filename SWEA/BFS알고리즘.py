'''
V E : V - 1 ~ V 번까지 V개의 정점. E 개의 간선
E개의 간선 정보
7 8
1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
'''
def bfs(s, N):     # 시작정점 s, 노드개수 N
    q = []                  # 큐
    visited = [0] * (N+1)   # visited
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 방문표시
    while q:                # 큐가 비워질 때까지... (남은 정점이 있으면)
        t = q.pop(0)
        # t에서 할 일
        print(t)
        for i in adjl[t]:   # t에 인접인 정점 i
            if visited[i] == 0:  # 방문하지 않은 정점이면
                q.append(i)      # 인큐
                visited[i] = 1 + visited[t]   # 방문표시 (나 t에서 한 개 더 온거다!)
    print(visited)
V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접 리스트
adjl = [[]for _ in range(V+1)]                  #  [ [], [2,3],< 1번행 [1, 4, 5] < 2번행
for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
# 다른 방법
# for i in range(0, E*2, 2)
    # n1, n2 = arr[i], arr[i+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)   # 무향 그래프, 만약 화살표가 있다면 이 식은 들어가면 x

bfs(1, V)
