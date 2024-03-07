N = int(input())
nm = list(map(int, input().split()))

stack = []
cnt = 1
while nm:
    if cnt == nm[0]:
        cnt += 1
        nm.pop(0)
    else:
        stack.append(nm.pop(0))

    while stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt += 1
        else:
            break
if len(stack) == 0:
    print('Nice')
else:
    print('Sad')


