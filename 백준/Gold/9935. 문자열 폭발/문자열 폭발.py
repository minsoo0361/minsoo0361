word = input()
reduce = input()
stack = []
for i in range(len(word)):
    stack.append(word[i])
    if word[i] ==reduce[-1]:
        if len(stack) >= len(reduce):
            if reduce[-2:-len(reduce)-1:-1] == ''.join(stack[-2:-len(reduce)-1:-1]): 
                for j in range(len(reduce)):
                    stack.pop()
if stack:
    print(*stack, sep="")
else:
    print("FRULA")