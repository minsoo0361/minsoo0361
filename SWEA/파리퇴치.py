import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range (1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range (N)]
    answer = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    cnt += arr[x][y]
            if answer < cnt:
                answer = cnt
    print(f'#{test_case} {answer}')