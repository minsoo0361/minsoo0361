T = int(input())
for tc in range (1, T+1):
    N = int(input())
    arr = [list(input())for _ in range(N)]
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]
    answer = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    cnt = 0
                    nx = i
                    ny = j
                    while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[k]
                        ny += dy[k]

                    if cnt == 5:
                        answer += 1
    if answer >= 1:
        print(f'#{tc}', 'YES')
    else:
        print(f'#{tc}', 'NO')
