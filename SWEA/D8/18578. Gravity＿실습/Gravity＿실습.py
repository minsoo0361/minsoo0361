T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    boxes_lst = []

    for i in range(N):
        cnt = 0
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                cnt += 1
        boxes_lst.append(cnt)
    print(f'#{tc} {max(boxes_lst)}')