import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(input())
    cnt = 0
    result = []
    for i in range(N):
        if arr[i] == '0':
            cnt = 0
        else:
            cnt += 1
            result.append(cnt)
    print(f'#{test_case}', max(result))

