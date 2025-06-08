a, b = map(int, input().split())
if a != b:
    if a > b:
        print(a)
    else:
        print(b)
elif a == b:
    print(a)