import sys
input = sys.stdin.readline
N = int(input())

arr = list(map(int, input().split()))
arr.reverse()

stack = []
result = []

for i in arr:
    while len(stack) != 0:
        if stack[-1] <= i:
            stack.pop()
        else:
            result.append(stack[-1])
            break

    if len(stack) == 0:
        result.append(-1)
    stack.append(i)

result.reverse()
print(*result)