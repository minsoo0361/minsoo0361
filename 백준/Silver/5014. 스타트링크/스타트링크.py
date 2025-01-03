from collections import deque

def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited = [False] * (F+1)

    visited[start] = True

    while queue:
        n, cnt = queue.popleft()        
        if n == G:
            print(cnt)
            return
        if n + U <= F and not visited[n+U]:
            queue.append((n+U, cnt+1))
            visited[n+U] = True
        if n-D >= 1 and not visited[n-D]:
            queue.append((n-D, cnt +1))
            visited[n-D] = True

    print("use the stairs")

F, S, G, U, D = map(int, input().split())
# 총 F층 고층 건물
# 스타트링크가 있는 곳의 위치는 G층
# 강호가 있는 곳은 S층
# 10 1 10 2 1 이 예시일때
# 강호는 1층, 스타트팅크는 10층
# U =2 라서 한번에 2칸씩 밖에 못올라감.
# 1 > 3 > 5 > 7 > 9 > 8 > 10
# 6번
# 100 2 1 1 0
# 2층 > 1층
# D가 0이라 아래로 못감

bfs(S)

