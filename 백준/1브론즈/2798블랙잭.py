N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_lst = []
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and i != k:
                sum_lst.append(arr[i]+arr[j]+arr[k])
pos_lst = []
for i in set(sum_lst):
    if i <= M:
        pos_lst.append(i)
print(max(pos_lst))
