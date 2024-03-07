import sys
sys.stdin = open('input.txt', 'r')
T = 10
for tc in range(1, T+1):
    N = int(input())
    num_lst = str(input())
    stack = []
    nm = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9'
    for i in range(N):
        if num_lst[i] in nm:
            stack.append(num_lst[i])
    stc = list(map(int, stack))
    print(f'#{tc}', sum(stc))




