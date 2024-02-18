k = int(input())
stack = []
for _ in range(k):
    nm = int(input())
    if nm != 0:
        stack.append(nm)
    else:
        stack.pop()
print(sum(stack))