N = int(input())
arr = []
stack = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(len(arr[i])):
        if arr[i][0] == 1:
            stack.append(arr[i][j + 1])
            arr[i][j] = 100
        elif arr[i][0] == 2:
            if len(stack) != 0:
                print(stack.pop())
            else:
                print(-1)
        elif arr[i][0] == 3:
            print(len(stack))
        elif arr[i][0] == 4:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif arr[i][0] == 5:
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)