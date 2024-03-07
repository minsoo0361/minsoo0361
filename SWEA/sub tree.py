def dfs(i):
    global cnt
    cnt += 1
    if arr[i] != 0:
        for nm in arr[i]:
            dfs(nm)

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = [[] for _ in range(E+2)]
    num_list = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        p, c = num_list[i], num_list[i+1]
        arr[p].append(c)
    cnt = 0
    dfs(N)
    print(f'#{tc} {cnt}')