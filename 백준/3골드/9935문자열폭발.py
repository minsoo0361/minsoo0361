import sys
input = sys.stdin.readline
word = list(input().strip())
boom = list(input().strip())
stack = []
for i in range(len(word)):
    stack.append(word[i])
    if boom[::-1] == stack[-1:-len(boom)-1:-1]:
        for j in range(len(boom)):
            stack.pop()
if len(stack) != 0:
    print(*stack, sep = '')
else:
    print('FRULA')
