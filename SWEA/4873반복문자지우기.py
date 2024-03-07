# 이 문제는 스택을 사용하여 푸는 문제입니다
# 스택은 한 쪽 끝에서만 자료를 넣거나 뺄 수 있도록 제한된 선형으로 나열된 자료구조를 의미하며 실 생활에선 비어있는 프링글스 통에 비유할 수 있다!
# push를 통해 요소를 삽입하고 pop을 통해 제거할 수 있는데, 이때 push는 파이썬 내장함수인 append를 사용하여 리스트 안에 추가할 수 있고,
# pop은 내장함수 pop을 통해 요소를 제거할 수 있다. 이때 append는 가장 마지막에 추가되고 pop은 가장 마지막 요소를 꺼내고 리스트에서 삭제한다.
# FILO 또는 LOFI(후입선출)의 형태를 띤다고 말할 수 있다.
T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input()))
    stack = []
    for i in range(len(arr)):
        if len(stack) == 0:
            stack.append(arr[i])
        elif len(stack) != 0:
            if arr[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(arr[i])

    print(f'#{tc} {len(stack)}')

