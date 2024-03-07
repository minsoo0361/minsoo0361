import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range (1, T+1):
    bit = list(str(input()))
    cnt = 0
    for i in range(1, len(bit)):
        if bit[0] == '0' and (bit[i-1] != bit[i]):
            cnt += 1
        elif bit[0] == '1' and (bit[i-1] != bit[i]):
            cnt += 1
    if bit[0] == '0':
        print(f'#{tc} {cnt}')
    else:
        print(f'#{tc} {cnt+1}')
