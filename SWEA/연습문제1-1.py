# 1. 피연산자
# 2. 여는괄호
# 3. ( , */, +-, )
# 피연산자 => 즉시 출력
# 연산자는 우선순위에 따라 stack 삽입, 삭제
# stck 안의 모든 연산자를 pop해서 마무리.
text = "(1+(1+3)*4/5)"
# 중위식  > 후위식 (스택)
stack = []  # push : append(x) / pop : pop()
result = ''   # 후위식을 넣을 result 변수

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # 입력될 때의 연산자 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 내에 있을 때의 연산자 우선순위
# 스택의 상태가 항상 내가 넣으려고 하는 연산자가,
# 기존에 있었던 연산자보다 우선순위가 높도록 유지!
# 중위식을 순회하며 후위식 만들어야 한다.
for ch in text:
    # 1. 숫자(피연산자)가 나오면 그대로 출력
    if ch.isdigit():
        result += ch
    # 2. 연산자  * / + - ( 포함이 된다면...
    if ch in '*/+-(':
        # 2-1. 입력된 연산자가 > 스택 맨 위의 연산자보다 우선순위
        if len(stack) == 0 or icp[ch] > isp[stack[-1]]:
            stack.append(ch)
        # 2-2. 입력된 연산자가 <= 스택 맨 위의 연산자보다 우선순위
        else:
            while len(stack) > 0 and icp[ch] <= isp[stack[-1]]:
                result += stack.pop()
            stack.append(ch)
    # 5. ) 닫는 괄호가 나오면
    elif ch == ')':
        # ( 여는 괄호가 나올때까지 pop 해줘라!
        while stack[-1] != '(':
            result += stack.pop()
        stack.pop()  # '('
# 순회가 끝난 후, stack의 내용을 모두 pop
while len(stack) > 0:
    result += stack.pop()
print(result)
