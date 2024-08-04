def conquer(i, j, size):
    if size == 3:
        arr[i][j] = '*'
        arr[i + 1][j - 1] = arr[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            arr[i + 2][j - k] = "*"
    
    else:
        newSize = size//2
        conquer(i, j, newSize)
        conquer(i + newSize, j - newSize, newSize)
        conquer(i + newSize, j + newSize, newSize)

N = int(input())

arr = [[' ']*2*N for _ in range(N)]

conquer(0, N - 1, N)

for star in arr:
    print("".join(star))