def shf():
    a = 0
    b = ((len(card) + 1) // 2)

    for i in range(len(card)):
        if i % 2 == 0:
            print(card[a], end = ' ')
            a += 1
        else:
            print(card[b], end = ' ')
            b += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(input().split())
    print(f'#{tc}', end = ' ')
    shf()
    print()