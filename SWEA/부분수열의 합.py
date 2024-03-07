T = int(input())
for tc in range (1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(1 << N):
        series_nm = 0
        for j in range(N):
            if i & (1 << j):
                series_nm += arr[j]
        if series_nm == K:
            cnt += 1
    print(f'#{tc} {cnt}')



