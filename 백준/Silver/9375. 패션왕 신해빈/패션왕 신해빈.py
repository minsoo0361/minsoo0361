T = int(input())
for tc in range(1, T+1):
    N = int(input())
    item_lst = dict()
    for j in range(N):
        clothes = list(input().split())
        if clothes[1] in item_lst:
            item_lst[clothes[1]].append(clothes[0])
        else:
            item_lst[clothes[1]] = [clothes[0]]

    cnt = 1
    for i in item_lst:
        cnt *= (len(item_lst[i]) + 1)
    print(cnt - 1)






