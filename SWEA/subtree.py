lst = []
def pre_order(T):
    if T:
        #print(T, end = ' ')
        lst.append(T)
        pre_order(left[T])
        pre_order(right[T])


T = int(input())
for tc in range(1, T+1):
    E, k = map(int, input().split())
    arr = list(map(int, input().split()))
    N = E + 1   # 정점은 간선의 개수보다 1개 많음
    left = [0] * (N + 1)  # 부모를 인덱스로 왼쪽 자식번호 저장
    right = [0] * (N + 1)  # 부모를 인덱스로 오른쪽 자식번호 저장
    par = [0] * (N + 1)  # 자식을 인덱스로 부모 저장

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        par[c] = p
    c = N


    while par[c] != 0:  # 부모가 있으면
        c = par[c]  # 부모를 새로운 자식으로 두고

    root = c

    pre_order(root)

    print(lst)