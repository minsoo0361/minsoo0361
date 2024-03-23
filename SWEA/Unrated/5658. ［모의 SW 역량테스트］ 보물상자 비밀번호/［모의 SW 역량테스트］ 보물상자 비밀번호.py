def make_set(n):

    # 기저조건
    if n == N // 4:
        return
    # word 리스트를 생성해주는 함수
    for i in range(0, len(arr), N // 4):
        tmp = int(''.join(arr[i:i + N // 4]), 16)
        ten_nm.append(tmp)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(input())
    ten_nm = []
    for i in range(N // 4):
        make_set(i)
        arr = [arr[-1]] + arr[:-1]

    ans = sorted(set(ten_nm), reverse=True)

    print(f'#{tc} {ans[K - 1]}')