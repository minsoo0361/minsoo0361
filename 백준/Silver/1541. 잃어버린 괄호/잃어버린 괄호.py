modify = input().split('-')

lst = []

for i in modify:
    cnt = 0
    arr = i.split('+')
    for j in arr:
        cnt += int(j)
    lst.append(cnt)


N = lst[0]

for i in range(1, len(lst)):
    N -= lst[i]
print(N)
