T = 10
for tc in range(1, T + 1):
    N = int(input())
    infix = input().rstrip()
    stack = []
    postfix = ''
    for ch in infix:
        if ch.isdigit():
            postfix += ch

        elif ch == '*':
            while len(stack) > 0 and stack[-1] == '*':
                postfix += stack.pop()
            stack.append(ch)

        elif ch == '+':
            while len(stack) > 0:
                postfix += stack.pop()
            stack.append(ch)
    while len(stack) > 0:
        postfix += stack.pop()

    stack = []
    for ch in postfix:
        if ch.isdigit():
            stack.append(ch)
        elif ch == '*':
            b = int(stack.pop())
            a = int(stack.pop())
            temp = a * b
            stack.append(temp)
        elif ch == '+':
            b = int(stack.pop())
            a = int(stack.pop())
            temp = a + b
            stack.append(temp)
    result = stack.pop()
    print(f'#{tc} {result}')