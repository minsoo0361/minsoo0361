T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = []
    for i in word:
        if i == '(':
            stack.append(i)
        elif stack and i ==')' and stack[-1] == '(':
            stack.pop()

        elif i == ')' :
            stack.append(i)
    if stack:
        answer = 'NO'
    else:
        answer = 'YES'
    print(answer)

