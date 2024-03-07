import sys

sys.stdin = open('sample_input.txt', 'r')
# 입력
T = int(input())


def method_name():
    for i in range(N):
        for j in range(N):
            if omok[i][j] == 'o':
                for k in range(4):
                    cnt = 0
                    nx = i
                    ny = j
                    while 0 <= nx < N and 0 <= ny < N and omok[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[k]
                        ny += dy[k]

                    # while True:
                    #     if omok[nx][ny] == '.' or 0 > nx or nx >= N or 0 > ny or ny >= N:
                    #         break
                    #     else:

                    if cnt >= 5:
                        return 'YES'
    return 'NO'


for tc in range(1, T + 1):
    N = int(input())
    # dx dy를 생성해서 우측, 좌하, 우하, 하를 입력
    dx = [0, -1, 1, 1]
    dy = [1, 1, 1, 0]
    answer = 0
    # 오목 배열을 2차원 배열로 입력
    omok = [list(input()) for _ in range(N)]

    # 로직
    # 이동하는 nx, ny > cnt에 1을 추가
    # cnt가 5이면 Yes를 출력 아니면 no를 출력

    print(f'#{tc} {method_name()}')
