T = int(input())
for tc in range(1, T+1):
    n = int(input())
    result = round(pow(n, 1 / 3))

    if result ** 3 == n:
        print(f'#{tc}', result)
    else:
        print(f'#{tc}', -1)