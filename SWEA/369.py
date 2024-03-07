N = int(input())
lst = ['3', '6', '9']
for i in range(1, N+1):
    check = 0
    cnt = 0
    for j in str(i):
        if j in lst:
            cnt += 1
            check = 1


    if check:
        print('-'*cnt, end = ' ')
        continue
    print(i, end =' ')