T = int(input())
for tc in range (1, T+1):
    station = [0] * 5001
    stop = []
    nm = []
    N = int(input())
    for _ in range(N):
        a1, b1 = map(int, input().split())
        for i in range(a1, b1+1):
            station[i] += 1
    P = int(input())
    for j in range(1, P+1):
        stop.append(int(input()))
    for k in stop:
        nm.append(station[k])
    print(f'#{tc}',*nm)










