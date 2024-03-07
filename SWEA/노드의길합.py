T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    h = [0] * (N + 1)
    arr = []
    for i in range(M):
        arr.append(list(map(int, input().split())))
    for k in range(len(arr)):
        for j in range(0,1):
            h[arr[k][j]] = arr[k][j+1]
    print(h)