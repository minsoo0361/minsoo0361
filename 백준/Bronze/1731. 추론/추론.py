N = int(input())
arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)
arr_sort = arr.sort()
cha = arr[1] - arr[0]
bee = arr[1] // arr[0]

lst = []
lst_2 = []

for i in range(1, N):
    if arr[i] - arr[i-1] == cha:
        lst.append(arr[-1]+ cha)
    elif arr[i] // arr[i-1] == bee:
        lst_2.append(arr[-1] * bee)

if len(lst) > len(lst_2):
    print(lst[0])
else:
    print(lst_2[0])