# def right_down(x, y):
#     lst.append(arr[x][y])
#     dx, dy = 1, 1
#     for k in range(1, N-1):
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < N and 0 <= ny < N:
#             if arr[nx][ny] in lst or arr[nx][ny] == arr[x][y]:
#                 left_down(nx, ny)
#             else:
#                 lst.append(arr[nx][ny])
#         left_down(nx, ny)
#
# def left_down(x, y):
#     if arr[x][y] in lst:
#         return
#     dx, dy = -1, 1
#     for k in range(1, N-1):
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < N and 0 <= ny < N:
#             if arr[nx][ny] in lst or arr[nx][ny] == arr[x][y]:
#                 left_up(nx, ny)
#             else:
#                 lst.append(arr[nx][ny])
#         left_up(nx, ny)
#
#
# def left_up(x, y):
#     if arr[x][y] in lst:
#         return
#     dx, dy = -1, -1
#     for k in range(1, N - 1):
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < N and 0 <= ny < N:
#             if arr[nx][ny] in lst or arr[nx][ny] == arr[x][y]:
#                 right_up(nx, ny)
#             else:
#                 lst.append(arr[nx][ny])
#         right_up(nx, ny)
#
# def right_up(x, y):
#     global start_x, start_y
#     if arr[x][y] in lst:
#         return
#     dx, dy = -1, 1
#     for k in range(1, N - 1):
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < N and 0 <= ny < N:
#             if arr[nx][ny] in lst or arr[nx][ny] == arr[x][y]:
#                 if start_x == nx and start_y == ny:
#                     print(lst)
#                 else:
#                     continue
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     lst = []
#     for i in range(N):
#         for j in range(1, N-1):
#             start_x, start_y = i, j
#             right_down(i,j)
di = [1, 1, -1, -1, 1]
dj = [-1, 1, 1, -1, -1]
def dfs(n, ci, cj, v):
    global ans
    # 가지치기 : 절반을 돌았는데 *2 해도 정답 갱신 불가능
    if n == 2 and ans>= len(v)*2:
        return
    # 종료조건
    if n > 3:
        return
    if n == 3 and (si, sj) == (ci, cj):
        ans = max(ans, len(v))
        return

    for k in range(n, n+2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            dfs(k, ni, nj, v)
            v.pop()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for si in range(N-2):
        for sj in range(1, N-1):
            dfs(0, si, sj, [])
    print(f'#{tc} {ans}')

