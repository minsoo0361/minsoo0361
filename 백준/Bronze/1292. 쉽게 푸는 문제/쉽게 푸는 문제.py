A, B = map(int, input().split())
arr = [[i] for i in range(1001)]
lst = []
for i in range(1, 1001):
    arr[i] = arr[i] * i
    for j in arr[i]:
        lst.append(j)
print(sum(lst[A-1:B]))
