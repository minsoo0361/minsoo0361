def conquer(x, y, N):
    color = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != arr[i][j]:
                conquer(x, y, N//3)
                conquer(x, y+N//3,N//3)
                conquer(x, y+(N//3*2), N//3)
                conquer(x + N//3, y, N//3)
                conquer(x + N//3, y+ N//3, N//3)
                conquer(x + N//3, y+ (N//3*2), N//3)
                conquer(x + (N//3*2), y, N//3)
                conquer(x + (N//3*2), y + N//3, N//3)
                conquer(x + (N//3*2), y + (N//3*2), N // 3)
                return
    if color == 0:
        answer.append(0)
    elif color == -1:
        answer.append(-1)
    elif color == 1:
        answer.append(1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = []
conquer(0, 0, N)
print(answer.count(-1))
print(answer.count(0))
print(answer.count(1))
