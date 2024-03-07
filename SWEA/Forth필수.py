T = int(input())
for test_case in range(1, T + 1):
    formula = list(input().split())
    stack = []
    postfix = ''
    for f in formula:
        if f.isdigit():
            stack.append(int(f))
        elif f == '+' and len(stack) >= 2:
            a = stack.pop(-2) + stack.pop()
            stack.append(a)
        elif f == '-' and len(stack) >= 2:
            b = stack.pop(-2) - stack.pop()
            stack.append(b)
        elif f == '*' and len(stack) >= 2:
            c = stack.pop(-2) * stack.pop()
            stack.append(c)
        elif f == '/' and len(stack) >= 2:
            d = stack.pop(-2) // stack.pop()
            stack.append(d)
        elif f == '.' and len(stack) == 1:
            print(f'#{test_case} {stack[-1]}')
        elif f in '*/+-' and len(stack) < 2 or (f == '.' and len(stack) >= 2):
            print(f'#{test_case} error')
            break


