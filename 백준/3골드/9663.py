N = int(input())
arr = [[0]* N for _ in range(N)]
right = [1, 1]
left = [-1, 1]
result = 0
for i in range(1, N):
    arr[0][0] = 0
    arr[i][0] = 1
    for j in range(1, N):
        arr[0][j] = 1
        arr[i][j] = 1
print(arr)    


        

        