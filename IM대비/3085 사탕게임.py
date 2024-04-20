N = int(input())
arr = [list(input()) for _ in range(N)]
answer = []
answer2 = []

row_max = 0
col_max = 0
# 행검사
for i in range(N):
    for j in range(N-1):
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            # 행에서 행 검사
            for x in range(N):
                tmp = 0
                for y in range(N-1):
                    if arr[x][y] == arr[x][y+1]:
                        tmp += 1
                    else:
                        tmp = 0
                    row_max = max(tmp, row_max)
                answer.append(row_max)
            # 행에서 열 검사
            for y in range(N):
                cnt = 0
                for x in range(N-1):
                    if arr[x][y] == arr[x+1][y]:
                        cnt += 1
                    else:
                        cnt = 0
                    col_max = max(cnt, col_max)
                answer2.append(col_max)
            arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]
# 열검사
for j in range(N):
    for i in range(N-1):
        if arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            # 열에서 행검사
            for x in range(N):
                tmp = 0
                for y in range(N-1):
                    if arr[x][y] == arr[x][y+1]:
                        tmp += 1
                    else:
                        tmp = 0
                    row_max = max(tmp, row_max)
                answer.append(row_max)
            # 열에서 열 검사
            for y in range(N):
                cnt = 0
                for x in range(N-1):
                    if arr[x][y] == arr[x+1][y]:
                        cnt += 1
                    else:
                        cnt = 0
                    col_max = max(cnt, col_max)
                answer2.append(col_max)
            arr[i+1][j], arr[i][j] = arr[i][j], arr[i+1][j]

answer = max(answer)
answer2 = max(answer2)
if answer > answer2:
    print(answer+1)
else:
    print(answer2+1)

