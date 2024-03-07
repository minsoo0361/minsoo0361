import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    corridor = [0] * 200
    for _ in range(N):
        up, down = map(int, input().split())
        up, down = (up-1)//2, (down-1)//2
        if up > down:
            up, down = down, up

        for i in range(up, down + 1):
            corridor[i] += 1


    print(f'#{tc}', max(corridor))