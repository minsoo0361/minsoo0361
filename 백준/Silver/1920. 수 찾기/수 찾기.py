N = int(input())
N_lst = list(map(int, input().split()))
N_lst.sort()
M = int(input())
M_lst = list(map(int, input().split()))

    
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        if target < arr[mid]:
            end = mid - 1
        if target > arr[mid] : 
            start = mid + 1
    return False

for i in range(M):
    if binary_search(N_lst, M_lst[i]):
        print(1)
    else:
        print(0)


