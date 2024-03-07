import sys
sys.stdin = open('in.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    answer = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            total = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                total += arr[ni][nj]
            total -= arr[i][j]
            if total % 2 == 0:
                total *= 2
            if answer < total:
                answer = total
    print(f'#{test_case} {answer}')


