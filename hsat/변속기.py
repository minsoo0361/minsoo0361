import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
cnt = 0
for i in range(1, len(arr)):
    if arr[i-1]+1 == arr[i]:
        cnt += 1
        if cnt == len(arr)-1:
            print("ascending")
    elif arr[i-1] -1 == arr[i]:
        cnt += 1
        if cnt == len(arr)-1:
            print("descending")
    else:
        print("mixed")

