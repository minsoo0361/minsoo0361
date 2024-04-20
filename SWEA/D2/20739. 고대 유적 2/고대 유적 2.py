T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = []
    # 가로
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == M-1:
                answer.append(cnt)
                cnt = 0
    # 세로
    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or i == N-1:
                answer.append(cnt)
                cnt = 0
    if max(answer) <= 1:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {max(answer)}')



