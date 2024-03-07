import sys
sys.stdin = open('input.txt', 'r')
def inorder(T):

    if T:
        inorder(c1[T])
        print(word[T], end='')
        inorder(c2[T])

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [[] * (N+1)]
    num_N = [] * (N+1)
    word = [] * (N + 1)
    left = [] * (N + 1)
    right = [] * (N + 1)
    for i in range(1, N+1):
        arr.append(list(input().split()))
    for k in range (1, len(arr)):
        for j in range(0,1):
            if len(arr[k]) == 4:
                num_N.append(arr[k][j])
                word.append(arr[k][j + 1])
                left.append(arr[k][j + 2])
                right.append(arr[k][j + 3])
            elif len(arr[k]) == 3:
                num_N.append(arr[k][j])
                word.append(arr[k][j + 1])
                left.append(arr[k][j + 2])
            elif len(arr[k]) == 2:
                num_N.append(arr[k][j])
                word.append(arr[k][j + 1])
    num = list(map(int, num_N))
    c1 =  list(map(int, left))
    c2 = list(map(int, right))
    word = [0] + word
    c1 = [0] + c1 + [0] * (N-len(c1))
    c2 = [0] + c2 + [0] * (N-len(c2))
    print(f'#{tc}', end=' ')
    inorder(1)
    print()

