V = 7
arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
    # u1, v1, u2, v2...
# 그래프를 표현 : 인접 리스트(노드 간의 연결 정보)
# 인접리스트 초기화
graph = [[] for _ in range(V + 1)]
for idx in range(0, len(arr), 2):
    u, v = arr[idx], arr[idx+1]
    graph[u].append(v) # u -> v
    graph[v].append(u) # v -> u


# BFS -> 해당 노드를 인접된 노드를 차례대로 방문

def bfs(start):
    visited = [False] * (V+1)
    queue = []   # 큐 : 방문할 노드들

    # 시작정점 start에 대해서 방문체크와 큐에 삽입
    visited[start] = True  # 재방문 하지 않도록 True 설정
    queue.append(start)
    while queue:   # 큐가 빌때까지 반복
        u = queue.pop(0)
        print('-', u, end = '')
        # 인접되어 있는 방문하지 않은 노드들을 큐에 삽입
        for v in graph[u]:  # u -> v1, v2 ...
            if visited[v] == False:
                queue.append(v)
                visited[v] = True

bfs(1)   # 1번 노드를 기준으로 BFS 탐색 진행
print()
# DFS -> 해당 노드에서 다른 노드로 먼저 깊게 탐색
# 스택 : 다시 되돌아 갈 수 있는 노드
def dfs(start):
    # 기저조건(의미없음) : 이미 방문한 노드라면 종료
    visited[start] = True
    print('-', start, end = '')
    # 재귀호출 : 다음 노드를 계속 탐색...
    for v in graph[start]:  # strat -> v1, v2...
        if visited[v] == False:
            dfs(v)

visited = [False] * (V+1)
dfs(1)
