T = int(input())
for tc in range(1, T+1):
    N, h = input().split()
    n = int(N)
    bi = ['0000', '0001', '0010','0011', '0100', '0101', '0110', '0111', '1000',
          '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A','B','C',
           'D','E','F']
    dic = dict(zip(hex, bi))
    arr = []
    for i in range(len(h)):
        arr.append(dic[h[i]])
    print(f'#{tc}', end = ' ')
    print(*arr, sep= '')


