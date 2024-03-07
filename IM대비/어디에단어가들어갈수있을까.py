T  = int(input())
for tc in range (1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            if arr[i][j] == 0:
