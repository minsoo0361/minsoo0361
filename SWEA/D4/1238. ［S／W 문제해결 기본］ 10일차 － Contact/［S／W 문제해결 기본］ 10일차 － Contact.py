# import sys
# sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(start):
    global cnt
    visited = [False] * 101
    visited[start] = True
    queue = deque()
    queue.append(start)

    # 가장 깊은 depth의 가장 큰 수
    max_number = start
    # 가장 깊은 depth를 저장
    max_depth = 1

    while queue:
        v = queue.popleft()
        for w in graph[v]:

            if visited[w]:
                continue
            # 중요!!! 현재 방문 = 이전방문 + 1번만에 왔다!
            visited[w] = visited[v] + 1

            # depth가 더 깊어졌네? -> max_number 초기화
            # depth 는 같은데 max_number 가 더 커졌네? -> 초기화
            if max_depth < visited[w] or (max_depth == visited[w] and max_number < w):
                max_depth = visited[w]
                max_number = w

            queue.append(w)
    return max_number

T = 10
for tc in range(1, 11):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range (101)]
    cnt = 0
    for i in range(0, N, 2):
        a, b = arr[i], arr[i+1]
        graph[a].append(b)
    a = bfs(M)
    print(f'#{tc} {a}')
