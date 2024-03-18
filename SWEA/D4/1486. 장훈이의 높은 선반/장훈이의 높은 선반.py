T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    lst = []
    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1<<j):
                subset.append(height[j])
        lst.append(sum(subset))
    nm_lst = sorted(set(lst))
    for i in nm_lst:
        if i >= B:
            print(f'#{tc} {i-B}')
            break



