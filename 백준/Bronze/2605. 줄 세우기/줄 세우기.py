N = int(input())
arr = list(map(int, input().split()))
stack = []
tmp = []
stack.append(1)
for i in range(2, N+1):
    for _ in range(arr[i-1]):
        tmp.append(stack.pop())
    stack.append(i)
    for _ in range(arr[i-1]):
        stack.append(tmp.pop())
print(*stack)


