N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
answer = N * M
# 첫번째 줄은 어짜피 White로 고정, 마지막 줄도 똑같이 R로 고정.
# 둘의 바꿔야 될 갯수를 answer에 더해줌
# 그담은 i가 인덱스 1부터 N-2까지 돌면서 B가 가장 많은 행을 찾고
cnt_w = 0
for w in range(0, N - 2):
    for j in range(M):
        if arr[w][j] != 'W':
            cnt_w += 1

    cnt_b = 0
    for b in range(w + 1, N - 1):
        for j in range(M):
            if arr[b][j] != 'B':
                cnt_b += 1

        cnt_r = 0
        for r in range(b + 1, N):
            for j in range(M):
                if arr[r][j] != 'R':
                    cnt_r += 1

        total = cnt_w + cnt_b + cnt_r
        if answer > total:
            answer = total
print(answer)