T = int(input())
for tc in range (1, T+1):
    N = int(input())
    arr_lst = []
    for n in range(1, N+1):
        arr = [1 for _ in range (n)]
        arr_lst.append(arr)
    for i in range(2, N):
        for j in range(1, i):
            arr_lst[i][j] = arr_lst[i-1][j] + arr_lst[i-1][j-1]
    print(f'#{tc}')
    for i in range(N):
        print(*arr_lst[i])
