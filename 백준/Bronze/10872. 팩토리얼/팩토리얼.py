def fact(n):
    # 기저조건
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

n = int(input())
print(fact(n))