N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
number = list(map(int, input().split()))

for i in number:
    low = 0
    high = N-1
    idx = False    
    while low <= high:
        middle = (low + high) // 2
        if card[middle] > i:
            high = middle - 1
        elif card[middle] < i:
            low = middle + 1
        else:
            idx = True
            break    
    if idx:
        print(1, end = ' ')
    else:
        print(0, end = ' ')    