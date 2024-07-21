def row_check(row, num):
    for x in range(9):
        if num == arr[row][x]:
            return False
    return True

def col_check(col, num):
    for x in range(9):
        if num == arr[x][col]:
            return False
    return True

def square(row, col, num):
    nr = (row//3)*3
    nc = (col//3)*3
    for x in range(3):
        for j in range(3):
            if arr[nr+x][nc+j] ==num:
                return False
    return True

def dfs(depth):
    if depth >= len(zero_lst):
        for k in range(9):
            print(''.join(map(str, arr[k])))
        exit()

    nr, nc = zero_lst[depth]
    for j in range(1, 10):
        if row_check(nr, j) and col_check(nc, j) and square(nr, nc, j):
            arr[nr][nc] = j
            dfs(depth+1)
            arr[nr][nc] = 0


arr = [list(map(int, input())) for _ in range(9)]
zero_lst = []
visited = [[0] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero_lst.append((i, j))
dfs(0)