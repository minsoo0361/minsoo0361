T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    dec = ''
    bi = 1

    while N != 0:
        bi /= 2
        if N >= bi:
            dec += '1'
            N -= bi
        else:
            dec += '0'

    print(f'#{tc}', end=' ')
    if len(dec) > 12:
        print('overflow')
    else:
        print(dec)