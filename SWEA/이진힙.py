def enq(num):
    global last
    last += 1
    h[last] = num
    c = last
    p = c // 2
    while p > 0 and h[p] > h[c]:  # 부모가 더 크면 바꿔준다
        h[p], h[c] = h[c], h[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr =  list(map(int, input().split()))
    last = 0
    h = [0] * (N + 1)
    for num in arr:
        enq(num)

    anc = last // 2
    total = 0
    while anc:
        total += h[anc]
        anc //= 2
    print(f'#{tc} {total}')













