T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            K = 1
            while K < 2 * N - 1:
                cost = K * K + (K-1) ** 2
                cnt = 0
                # 절반을 나눠서 계산. 그중 위
                for x in range(1-K, 1):
                    for y in range(-(K-1)-x, x+(K-1)+1):
                        nx = i + x
                        ny = j + y
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                            cnt += 1

                # 아랫 부분
                for x in range(1, K):
                    for y in range(x-K+1, K - x):
                        nx = i + x
                        ny = j + y
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                            cnt += 1

                if cnt * M - cost >= 0:
                    if max_cnt < cnt:
                        max_cnt = cnt
                K += 1

    print(f'#{tc} {max_cnt}')


