N = int(input())
for i in range(N):
    stack = []
    arr = input()
    for j in range(len(arr)):
        if arr[j] == "(":
            stack.append(arr[j])
        elif len(stack) !=0 and arr[j] == ")" and stack[-1] == "(":
                stack.pop()
        elif arr[j] == ")":
             stack.append(arr[j])
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")