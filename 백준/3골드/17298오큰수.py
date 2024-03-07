import sys
input = sys.stdin.readline
N = int(input())

arr = list(map(int, input().split()))
# ex ) = 9 5 4 8
# 역순으로 정렬
arr.reverse()
# 담아놓을 stack과 답을 넣을 result 두개를 만들어놓기
stack = []
result = []
# arr에서 하나씩 수를 꺼내오면서 큰지 작은지 비교하기
for i in arr:
    # len(stack)이 0이 아니라면 계속 돌도록 설정
    while len(stack) != 0:
        # 스택에 담겨있는 값. ex에서는 8이므로 8과 i = 4를 비교
        # 8이 4보다 크므로 result에 8을 append
        if stack[-1] <= i:
            stack.pop()
        else:
            result.append(stack[-1])
            break
    # 스택이 비어있다면 역순으로 했기 때문에 8값을 기준으로
    # -1을 result에 append 그후에 stack에는 i값 append
    if len(stack) == 0:
        result.append(-1)

    stack.append(i)

result.reverse()
print(*result)