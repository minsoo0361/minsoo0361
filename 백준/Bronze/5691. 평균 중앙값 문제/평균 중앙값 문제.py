while True:
    A, B = map(int, input().split())
    if A == B == 0:
        break
    C = B - A
    print(A - C)
