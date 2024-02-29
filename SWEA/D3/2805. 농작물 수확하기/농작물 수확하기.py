T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input()))for _ in range(N)]
    total = 0
    n = N // 2
    answer = []
    for i in range(N):
        total = 0
        for j in range(N):
            total += farm[n][j]
            answer.append(total)
        for k in range(1, n+1):
            for l in range(k, N-k):
                total += farm[n-k][l]
                total += farm[n+k][l]
    print(f'#{tc} {total}')