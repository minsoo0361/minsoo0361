T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    multi_lst = []
    danjo = []

    for i in range(N - 1):
        for j in range(i + 1, N):
            multi_lst.append(arr[i] * arr[j])
    for k in multi_lst:
        K = str(k)
        result = True

        for j in range(0, len(K) - 1):
            if K[j] > K[j + 1]:
                result = False
        if result == True:
            danjo.append(k)

    if len(danjo) == 0 :
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', max(danjo))