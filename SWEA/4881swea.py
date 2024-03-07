# 순열 만들기
def f(i, k, s): # i - 1 까지 선택한 원소의 합
    global min_v

    if i == k:  # 종료조건(기저조건)
        # print(*P)
        if min_v > s:   # 최솟값을 갱신하는 부분
            min_v = s
    elif s >= min_v:     # 백트래킹을 위한 코드
        return   # 가지치기 당신은 손절이야 익절하는 부분
    else:    # 이 부분은 중복없는 순열을 위한 코드
        for j in range(i, k):   # P[i]자리에 올 원소 P[j
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i + 1, k, s + arr[i][P[i]])
            P[i], P[j] = P[j], P[i]     # 교환전으로 복구

T = int(input())  # 테스트 케이스
for tc in range(1, T + 1):  # 범위 설정

    N = int(input())  # 갯수
    arr = [list(map(int, input().split())) for _ in range(N)]  # 2차원배열로 만들어 주는 부분
    P = [i for i in range(N)]  # 설정한 배열이 index를 나타내는 것으로 더이상 세로에서 중복할 수없다는 것을 표현
    min_v = 9999

    f(0, N, 0)

    print(f'#{tc}', min_v)