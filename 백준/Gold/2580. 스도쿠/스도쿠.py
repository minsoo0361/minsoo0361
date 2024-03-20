def row_check(x, n):
    # 행을 체크하는 함수
    # 행에 해당하는 변수 x와 0에 해당하는 변수 n 설정
    for i in range(N):
        if n == arr[x][i]:  # 0 값이 이미 있다면
            return False
    return True

def col_check(y, n):
    # 열을 체크하는 함수
    # 열에 해당하는 변수 y
    for i in range(N):
        if n == arr[i][y]:
            return False
    return True

def rect_check(y, x ,n):
    # 3*3 배열을 체크하는 함수
    for i in range(3):
        for j in range(3):
            if n == arr[y//3 * 3 + i][x//3*3 + j]: # 0 값이 있으면
                return False
    return True

def dfs(n):
    # 가지치기, 기저조건
    if n == len(lst): # 0값의 개수와 lst길이 값이 같다면
        for i in arr:
            print(*i)
        exit()

    for i in range(1, 10):
        y = lst[n][0]   # 0인 좌표값의 열
        x = lst[n][1]   # 0인 좌표값의 행
        if col_check(x, i) and row_check(y, i) and rect_check(y, x, i):
            arr[y][x] = i
            dfs(n+1)
            arr[y][x] = 0

import sys
input = sys.stdin.readline
N = 9
arr = [list(map(int, input().split())) for _ in range(N)]
lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            # arr[i][j]가 0이라면 lst에 그 좌표값을 추가
            # 0인 위치를 lst에 저장
            lst.append([i, j])
dfs(0)

