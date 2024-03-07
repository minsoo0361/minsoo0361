import sys
sys.stdin = open('input.txt', 'r')
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
    for n in range(len(h)//2-1, 0,  -1):
        if N % 2 == 0:
            h[N//2] = h[N]
            if n < (N//2):
                h[n] = h[n*2] + h[n*2+1]
        elif N % 2 == 1:
            h[n] = h[n*2]+h[n*2+1]
    print(f'#{tc}', h[L])
