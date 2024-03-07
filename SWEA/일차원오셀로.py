T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j, sol = map(int, input().split())
        if sol == 1:  # 1번 경우일 경우 뒤집는다고 했는데 0>1,
            # 1>0으로 만드는방법은 -1을 하거나 +1을 하면 된다.
            for k in range(i - 1, i + j - 1):
                if k < 0 or k >= len(arr):
                    break
                if arr[k] == 1:  # arr[k]가 1일 경우엔 -1을 해줘서 0으로 만들고
                    arr[k] -= 1
                elif arr[k] == 0:  # arr[k]가 0일 경우엔 +1을 해줘서 1로 만든다
                    arr[k] += 1

        elif sol == 2:  # 2번 경우일 경우 arr[i]번 돌을 기준으로 j번째 공까지
            # 같은색으로 바꾼다고 했으니 arr[k]에 해당하는 공을
            for k in range(i - 1, i + j - 1):
                if k < 0 or k >= len(arr):
                    break
                # arr[i-1]공으로 맞춰준다.
                arr[k] = arr[i - 1]

        elif sol == 3:  # 가장 까다로운 3번 조건

            for k in range(1, j + 1):
                if (i - k + 1) < 0 or (i - k + 1) >= len(arr) or (i + k - 1) < 0 or (i + k - 1) >= len(arr):
                    break
                if arr[i - k - 1] == arr[i + k - 1] == 0:
                    arr[i - k - 1] += 1
                    arr[i + k - 1] += 1
                elif arr[i - k - 1] == arr[i + k - 1] == 1:
                    arr[i - k - 1] -= 1
                    arr[i + k - 1] -= 1
    print(f'#{tc}', *arr)
