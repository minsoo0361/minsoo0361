T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    di = [-1, 1, 1, -1]
    dj = [1, 1, -1, -1]
    answer = []
    for i in range(N):
        for j in range(N):
            total = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + dx[k] * l
                    nj = j + dy[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]
            answer.append(total)

    for i in range(N):
        for j in range(N):
            total = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    nx = i + di[k] * l
                    ny = j + dj[k] * l
                    if 0 <= nx < N and 0 <= ny < N:
                        total += arr[nx][ny]
            answer.append(total)
    print(f'#{tc}', (max(answer)))

