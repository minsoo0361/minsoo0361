T = int(input())
for tc in range (1, T + 1):
    N, M = map(int, input().split())
    n_lst = list(map(int, input().split()))
    m_lst = list(map(int, input().split()))
    stack = []
    n_lst.sort()
    m_lst.sort()
    for i in range(N):
        if len(n_lst) == 0 or len(m_lst) == 0:
            break
        elif n_lst[-1] <= m_lst[-1]:
            stack.append(n_lst[-1])
            n_lst.pop()
            m_lst.pop()
        elif n_lst[-1] > m_lst[-1]:
            n_lst.pop()
    print(f'#{tc}', sum(stack))