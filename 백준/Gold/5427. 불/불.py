from pprint import pprint
from collections import deque
def bfs(si, sj):
    tmp = deque()

    for i in range(H+2):
        for j in range(W+2):
            if arr[i][j]== '*':
                arr[i][j] = -1
                tmp.append([i, j])

    tmp.append([si, sj])
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while tmp:
        i, j = tmp.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < H + 2 and 0 <= ny < W + 2 and arr[nx][ny] == '.':
                if arr[i][j] == -1:
                    arr[nx][ny] = -1
                    tmp.append([nx, ny])

                elif arr[i][j] >= 0:
                    arr[nx][ny] = arr[i][j] + 1
                    tmp.append([nx, ny])

            elif arr[nx][ny] == '0':
                if arr[i][j] >= 0:
                    arr[nx][ny] = arr[i][j] + 1
                    return arr[nx][ny]

    return 'IMPOSSIBLE'


T = int(input())
for tc in range(1, T + 1):
    W, H = map(int, input().split())
    arr = [['0']+list(map(str, input()))+['0'] for _ in range(H)]
    arr = ([['0'] * (W+2)]) + arr + ([['0'] * (W+2)])
    for i in range(H+2):
        for j in range(W+2):
            if arr[i][j] == '@':
                si, sj = i, j
                arr[si][sj] = 0
                print(bfs(si, sj))
                break




