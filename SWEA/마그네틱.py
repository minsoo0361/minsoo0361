import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    table =[list(map(int, input().split())) for _ in range(N)]
    table = list(map(list, zip(*table)))

    for i in table:
        arr = []
        for k in i:
            if k != 0:
                arr.append(k)

        for j in range(len(arr)-1):
            if arr[j] == 1 and arr[j+1] == 2:
                cnt += 1
    print(f'#{tc}', cnt)


