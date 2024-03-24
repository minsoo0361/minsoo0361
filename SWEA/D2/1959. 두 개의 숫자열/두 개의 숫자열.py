T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_lst = list(map(int, input().split()))
    M_lst = list(map(int, input().split()))
    sum_lst = []
    if N < M:
        for i in range(M-N+1):
            tmp = 0
            for j in range(N):
                tmp += N_lst[j] * M_lst[i+j]
            sum_lst.append(tmp)
        print(f'#{tc} {max(sum_lst)}')

    else:
        for i in range(N-M+1):
            ans = 0
            for j in range(M):
                ans += N_lst[i+j] * M_lst[j]
            sum_lst.append(ans)
        print(f'#{tc} {max(sum_lst)}')


