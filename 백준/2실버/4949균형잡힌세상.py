while True:
    word = input()
    stack = []
    if word == '.':
        break
    for i in word:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break

    if stack:
        answer = 'no'
    else:
        answer = 'yes'
    print(answer)
