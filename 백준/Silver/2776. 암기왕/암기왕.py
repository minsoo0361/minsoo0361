def binarySearch(note1, target):
    low = 0
    high = len(note1) - 1

    while low <= high:
        mid = (low+high) // 2
        if note1[mid] == target:
            return 1
        elif note1[mid] > target:
            high = mid - 1
        elif note1[mid] < target:
            low = mid + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    note1 = sorted(list(map(int, input().split())))
    M = int(input())
    note2 = list(map(int, input().split()))
    for i in note2:
        print(binarySearch(note1, i))