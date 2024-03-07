postfix = "113+4*5/+"
# 연산자들을 딕셔너리에 람다식으로!
oper = { # "연산자 - 람다식" 쌍
    '*': lamda a, b : a * b,
    '/': lamda a, b : a // b,
    '+': lamda a, b : a + b,
    '-': lamda a, b : a - b,

}

# 계산기 2 (후위식 -> 계산하여 결과)
stack = []
for ch in postfix:
    # 피연산자를 스택에 넣겠다
    if ch.isdigit():
        stack.append(ch)

    # 연산자를 만나면 피연산자를 두개 빼서 연산! stack 에 push
    else:  # 연산자 * / + -
        b = int(stack.pop())
        a = int(stack.pop())
        # if ch == '*':
        #     stack.append(a * b)
        # elif ch == '/':
        #     stack.append(a / b)
        # elif ch == '+':
        #     stack.append(a + b)
        # elif ch == '-':
        #     stack.append(a - b)
        temp = oper[ch](a, b)
        stack.append(temp)
# 순회가 완료되면 스택에 단 하나의 결과값이 남게 된다
result = stack.pop()
print(result)


