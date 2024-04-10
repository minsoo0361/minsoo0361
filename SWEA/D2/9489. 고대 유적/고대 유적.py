T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = []
    # 우로 가는것과 아래로 가는것 두 방향만...
    # 우, 아래로 갈때
    dr, dd = [0, 1], [1, 0]
    row_max = 0
    col_max = 0
    # 우로 갈 때
    for i in range(N):
        cnt = 0
        for j in range(M-1):
            if arr[i][j] == 1:
                if arr[i][j+1] == 1:
                    nx = i + dr[0]
                    ny = j + dr[1]
                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                        cnt += 1
                else:
                    row_max = max(cnt, row_max)
        answer.append(cnt)
    # 아래로 갈 때
    for j in range(M):
        tmp = 0
        for i in range(N-1):
            if arr[i][j] == 1:
                if arr[i+1][j] == 1:
                    nx = i + dd[0]
                    ny = j + dd[1]
                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                        tmp += 1
                else:
                    col_max = max(tmp, col_max)
        answer.append(tmp)
    print(f'#{tc} {max(answer)+1}')
