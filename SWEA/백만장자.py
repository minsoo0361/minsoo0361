
T = int(input())
for test_case in range (1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    mx_nm = price[-1]
    profit = 0
    for i in range(N-1, -1, -1):
        if mx_nm <= price[i]:
            price[i] = mx_nm
        else:
            profit += mx_nm - price[i]
    print(f'#{test_case} {profit}')

