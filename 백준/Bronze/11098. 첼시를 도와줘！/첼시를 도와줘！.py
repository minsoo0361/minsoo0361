T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    for _ in range(n):        
        pr, name = input().split()
        price = int(pr)
        arr.append([price, name])
        arr = sorted(arr, key=lambda x : -x[0])
    print(arr[0][1])