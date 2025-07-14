T = int(input())
for _ in range(T):
    num = int(input())
    a = 0
    for i in range(1, num+1):
        if i % 2 != 0:
            a += i
    print(a)
    