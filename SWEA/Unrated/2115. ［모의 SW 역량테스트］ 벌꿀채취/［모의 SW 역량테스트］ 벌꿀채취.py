def dfs(n, cnt, sm, ci, cj):
    global mx
    # 가지치기
    if cnt > C:
        return

    if n == M:
        mx = max(mx, sm)
        return

    dfs(n + 1, cnt + arr[ci][cj + n], sm + arr[ci][cj + n] ** 2, ci, cj)
    dfs(n + 1, cnt, sm, ci, cj)


T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 두 일꾼이 각각 탐색하도록 일꾼 1이 탐색하는 범위를 x1, y1, 일꾼 2가 탐색하는 범위를 x2, y2로 잡고 탐색
    ans = mx = sm1 = 0

    for x1 in range(N):  # x1은 N 전범위 탐색
        for y1 in range(N - M + 1):  # y1은 끝의 두 범위부터
            mx = 0
            dfs(0, 0, 0, x1, y1)
            sm1 = mx
            for x2 in range(x1, N):
                if x1 == x2:
                    sj = y1 + M
                else:
                    sj = 0
                for y2 in range(sj, N - M + 1):
                    mx = 0
                    dfs(0, 0, 0, x2, y2)
                    ans = max(ans, sm1 + mx)
    print(f'#{tc} {ans}')










