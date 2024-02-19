A, B = map(int, input().split())
result = A*B

while B:
    if A > B:
        A, B = B, A
    B %= A


print(result//A)