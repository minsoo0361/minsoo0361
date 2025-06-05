T = int(input())
for _ in range(T):
    N, M = map(str, input().split())
    cnt = 0
    for i in range(int(N), int(M)+1):
        for j in str(i):
            if j == '0':
                cnt += 1
    print(cnt)