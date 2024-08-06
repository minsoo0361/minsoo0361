N = int(input())
lst = list(map(int, input().split()))
arr = sorted(list(set(lst)))
dic = {arr[i] : i for i in range(len(arr))}
for i in lst:
    print(dic[i], end= ' ')
