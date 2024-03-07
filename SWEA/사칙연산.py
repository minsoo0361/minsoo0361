def postorder(n):
    if n:
        postorder(Left[n])  # 왼쪽
        postorder(Right[n])  # 오른쪽
        # 부모
        if value[n].isdigit():
            stack.append(int(value[n]))
        else:
            b = stack.pop()
            a = stack.pop()
            if value[n] == '+':
                stack.append(a + b)
            elif value[n] == '-':
                stack.append(a - b)
            elif value[n] == '*':
                stack.append(a * b)
            elif value[n] == '/':
                stack.append(a // b)

T = 10
for tc in range(1, T + 1):
    stack = []

    N = int(input())
    Left = [0] * (N + 1)
    Right = [0] * (N + 1)
    value = [0] * (N + 1)
    for _ in range(N):
        ipt = list(input().split())
        if len(ipt) == 4:
            Left[int(ipt[0])]= int(ipt[2])
            Right[int(ipt[0])] = int(ipt[3])

        value[int(ipt[0])] = ipt[1]

    postorder(1)
    print(f'#{tc}', *stack)