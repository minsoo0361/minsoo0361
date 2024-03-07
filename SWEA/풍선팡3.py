T = int(input())
for tc in range (1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range (N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    answer = []
    for i in range(N):
        for j in range(N):
            total = arr[i][j]
            for k in range(4):
                for x in range(1, arr[i][j]+1):
                    nx = i + dx[k] * x
                    ny = j + dy[k] * x
                    if 0 <= nx < N and 0 <= ny < N:
                        total += arr[nx][ny]

            answer.append(total)
    print(f'#{tc}', max(answer)-min(answer))

