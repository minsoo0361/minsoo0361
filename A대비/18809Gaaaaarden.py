from collections import deque
queue = deque()

N, M, G, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N